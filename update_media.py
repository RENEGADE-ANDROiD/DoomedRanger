import argparse, concurrent.futures, hashlib, json, sys
from fractions import Fraction
from pathlib import Path
from PIL import Image

parser=argparse.ArgumentParser(description="Refresh website clips from the approved mod GIFs.")
parser.add_argument("--media-directory",type=Path,required=True)
parser.add_argument("--readme",type=Path,required=True)
parser.add_argument("--runtime-directory",type=Path)

args=parser.parse_args()
if args.runtime_directory:sys.path.insert(0,str(args.runtime_directory))
import av
root=Path(__file__).resolve().parent
names={
 "blaster":"Blaster","boomer":"Boomer","machine-gun":"Machine Gun","super-shotgun":"Super Shotgun",
 "chaingun":"Chaingun","nailgun":"Nailgun","grenade-launcher":"Grenade Launcher",
 "qcon-rocket-launcher":"QCon Rocket Launcher","homing-launcher":"Homing Launcher",
 "tribolt":"Tribolt","hyperblaster":"Hyperblaster","thunderbolt":"Thunderbolt",
 "plasma-disruptor":"Plasma Disruptor","eelsbane":"Eelsbane","railgun":"Railgun",
 "hellraiser":"Hellraiser","bfg10k":"BFG10K","chainsaw-gauntlet":"Chainsaw Gauntlet",
 "flamethrower":"Flamethrower","tormentor":"Tormentor","dire-orb":"Dire Orb"}
sources={slug:args.media_directory/(name+" - Left Centered Right.gif") for slug,name in names.items()}
sources["dire-orb-gameplay"]=args.media_directory/"DireOrb.gif"
assert all(p.is_file() for p in sources.values()),"Missing source GIF"
manifest_path=root/"media-manifest.json"
previous=json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
def refresh(item):
 slug,source=item
 digest=hashlib.sha256(source.read_bytes()).hexdigest()
 if previous.get(slug,{}).get("source_sha256")==digest and (root/"media"/(slug+".mp4")).exists():
  return slug,previous[slug]
 out=root/"media"/(slug+".mp4")
 with Image.open(source) as image:
  frames=image.n_frames;duration=0
  target_height=round(image.height*640/image.width/2)*2
  with av.open(str(out),"w",options={"movflags":"+faststart"}) as video:
   stream=video.add_stream("libx264",rate=100)
   stream.width=640;stream.height=target_height;stream.pix_fmt="yuv420p"
   stream.codec_context.time_base=Fraction(1,1000)
   stream.codec_context.thread_count=2
   stream.codec_context.max_b_frames=0
   stream.options={"crf":"18","preset":"fast","bf":"0"}
   for i in range(frames):
    image.seek(i);delay=image.info.get("duration",100)
    rgb=image.convert("RGB").resize((640,target_height),Image.Resampling.LANCZOS)
    if i==0:rgb.save(root/"media"/(slug+".jpg"),quality=90,optimize=True)
    frame=av.VideoFrame.from_image(rgb);frame.pts=duration;frame.time_base=Fraction(1,1000)
    for packet in stream.encode(frame):video.mux(packet)
    duration+=delay
   if delay>10:
    frame=av.VideoFrame.from_image(rgb);frame.pts=duration-10;frame.time_base=Fraction(1,1000)
    for packet in stream.encode(frame):video.mux(packet)
   for packet in stream.encode():video.mux(packet)
 with av.open(str(out)) as check:
  decoded=sum(1 for f in check.decode(video=0))
  actual=check.duration/1000
  assert decoded>=frames and abs(actual-duration)<=50,(slug,decoded,actual,duration)
 return slug,dict(source=source.name,source_sha256=digest,source_frames=frames,duration_ms=duration,video_bytes=out.stat().st_size)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 manifest=dict(pool.map(refresh,sources.items()))
manifest_path.write_text(json.dumps(manifest,indent=2)+"\n")
readme=args.readme.read_text(encoding="utf-8-sig").replace("The crosshair follows that firing line;",
 "The crosshair stays stable as you look around, with alignment for the selected weapon and hand;")
(root/"mod-readme.md").write_text(readme,encoding="utf-8")
print("Verified",len(manifest),"current clips;",sum(m["video_bytes"] for m in manifest.values()),"video bytes total")
