import sys, json, urllib.request, urllib.error
K=open(sys.argv[5] if len(sys.argv)>5 else ".el_key").read().strip(); out,model,text=sys.argv[1],sys.argv[2],sys.argv[3]; vs=json.loads(sys.argv[4])
body={"text":text,"model_id":model,"voice_settings":vs}
req=urllib.request.Request("https://api.elevenlabs.io/v1/text-to-speech/TX3LPaxmHKxFdv7VOQHJ?output_format=mp3_44100_128",data=json.dumps(body).encode(),headers={"xi-api-key":K,"Content-Type":"application/json"})
try: open(out,"wb").write(urllib.request.urlopen(req,timeout=180).read()); print("ok",out,len(text),"znaków")
except urllib.error.HTTPError as e: print("ERR",e.code,e.read()[:300])
