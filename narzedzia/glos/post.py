# squeeze long silences only, then gentle leveling. Usage: post.py in out
import sys, numpy as np, subprocess, wave
src,dst=sys.argv[1],sys.argv[2]; SR=44100
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
# natural voice: NO pitch/tempo DSP (it sounds like a voice changer); only gentle leveling
af="acompressor=threshold=-20dB:ratio=2:attack=10:release=150:makeup=3dB,alimiter=limit=0.9"
subprocess.run(["ffmpeg","-y","-loglevel","error","-f","s16le","-ar",str(SR),"-ac","1","-i","_tmp.raw","-af",af,dst],check=True)
