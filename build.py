import html
W=[("1","Blaster","blaster","Unlimited glowing bolts. Your starting gun."),
("2","Boomer","boomer","Eight-pellet shotgun."),
("3","Machinegun","machine-gun","Quake 2-style hitscan."),
("4","Super Shotgun","super-shotgun","20-pellet double blast."),
("5","Chaingun","chaingun","Spins up, then shreds."),
("5","Nailgun","nailgun","10 nails a second. Kills can pin bodies to walls."),
("6","Grenade Launcher","grenade-launcher","Lobbed grenades. Good for grenade jumps."),
("6","QCon Rocket Launcher","qcon-rocket-launcher","Quake-tuned rockets and rocket jumps."),
("6","Homing Launcher","homing-launcher","Seeker rockets that track targets."),
("6","Tribolt","tribolt","Three-bolt explosive volley with kickable casings."),
("7","Hyperblaster","hyperblaster","Three red energy bolts per shot."),
("8","Thunderbolt","thunderbolt","Lightning beam. Discharges if you fire it underwater."),
("8","Plasma Disruptor","plasma-disruptor","Rapid plasma. Kills vaporize."),
("8","Eelsbane","eelsbane","Green acid plasma. Uses Fuel; drops only from Toxic Fatso/Mancubus enemies."),
("9","Railgun","railgun","Piercing 100-damage rail."),
("9","Tormentor","tormentor","Green acid stream. Uses Fuel; drops only from Toxic Fatso/Mancubus enemies."),
("9","Hellraiser","hellraiser","Fiery piercing rail that ignites every target it hits. Rare Arch-vile drop."),
("0","BFG10K","bfg10k","Green energy orb, electrical arcs, blast ring, and BFG spray."),
("0","Chainsaw Gauntlet","chainsaw-gauntlet","Alternating chainsaw swings."),
("0","QCon Flamethrower","flamethrower","Flame stream that leaves enemies burning. Uses Fuel.")]
NEW={"eelsbane","tormentor","hellraiser","chainsaw-gauntlet","flamethrower","blaster"}
V="?v=20261005d"
def vid(f,label):
    q=V if f in NEW else ""
    return f'<video autoplay muted loop playsinline preload="none" poster="media/{f}.jpg{q}" aria-label="{html.escape(label)}"><source src="media/{f}.mp4{q}" type="video/mp4"></video>'
cards="\n".join(f'''<figure class="weapon">{vid(f,n+" held left, centered and right")}<figcaption><h3>{n}<span class="slot">Slot {s}</span></h3><p>{d}</p></figcaption></figure>''' for s,n,f,d in W)
t=open("index.template.html",encoding="utf-8").read().replace("{{WEAPONS}}",cards)
open("index.html","w",encoding="utf-8").write(t)
print("ok",len(W))
