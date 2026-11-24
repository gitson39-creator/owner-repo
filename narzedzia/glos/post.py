# squeeze silences, then tempo/pitch with formant preservation, then compression; prints wpm + centroid
import sys, numpy as np, subprocess, wave
src,dst,semi,tempo=sys.argv[1],sys.argv[2],float(sys.argv[3]),float(sys.argv[4]); SR=44100
a=np.frombuffer(subprocess.run(["ffmpeg","-loglevel","error","-i",src,"-ac","1","-ar",str(SR),"-f","s16le","-"],capture_output=True).stdout,np.int16).astype(np.float32)/32768
win=int(.01*SR); env=np.array([np.abs(a[i:i+win]).max() for i in range(0,len(a)-win,win)]); q=env<0.012
out=[]; i=0; prev=0; MAXP=0.20
while i<len(q):
    if q[i]:
        j=i
        while j<len(q) and q[j]: j+=1
        if (j-i)*.01>MAXP:
            c0=i*win+int(MAXP/2*SR); c1=j*win-int(MAXP/2*SR)
            if i==0: c0=max(0,j*win-int(.03*SR))
            if j>=len(q): c1=len(a); c0=i*win+int(.15*SR)
            seg=a[prev:c0].copy(); f=int(.004*SR)
            if len(seg)>2*f: seg[-f:]*=np.linspace(1,0,f)
            out.append(seg); prev=c1
        i=j
    else: i+=1
out.append(a[prev:]); b=np.concatenate(out)
open("_tmp.raw","wb").write((np.clip(b,-1,1)*32767).astype(np.int16).tobytes())
af=f"rubberband=tempo={tempo}:pitch={2**(semi/12):.5f}:formant=preserved:pitchq=quality,acompressor=threshold=-22dB:ratio=4:attack=5:release=80:makeup=6dB,highshelf=f=3500:g=2,alimiter=limit=0.9"
subprocess.run(["ffmpeg","-y","-loglevel","error","-f","s16le","-ar",str(SR),"-ac","1","-i","_tmp.raw","-af",af,dst],check=True)
