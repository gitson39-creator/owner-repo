import sys, numpy as np, parselmouth
def stats(path, fmin=75, fmax=500):
    snd=parselmouth.Sound(path).convert_to_mono()
    p=snd.to_pitch_ac(time_step=0.01,pitch_floor=fmin,pitch_ceiling=fmax,voicing_threshold=0.5)
    f=p.selected_array['frequency']; f=f[f>0]
    st=12*np.log2(f/np.median(f))
    # local pitch movement: semitones per second of voiced speech (absolute slope)
    ff=p.selected_array['frequency']; v=ff>0; s2=np.where(v,12*np.log2(np.where(v,ff,1)/np.median(f)),np.nan)
    d=np.abs(np.diff(s2)); d=d[~np.isnan(d)]; d=d[d<3]
    inten=snd.to_intensity(); I=inten.values[0]; I=I[I>np.percentile(I,40)]
    return dict(median=np.median(f), sd_st=st.std(), range_st=np.percentile(st,95)-np.percentile(st,5), move=d.mean()*100, int_sd=I.std())
for a in sys.argv[1:]:
    s=stats(a); print(f"{a.split('/')[-1][:28]:28s} F0 {s['median']:5.0f} Hz | SD {s['sd_st']:4.2f} st | zakres 5-95% {s['range_st']:4.1f} st | ruch {s['move']:4.1f} st/s | dyn {s['int_sd']:4.1f} dB")
