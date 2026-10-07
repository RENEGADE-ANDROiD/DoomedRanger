# Doomed Ranger

The Ranger from the Quake series drops into Doom with 20 Quake Champions weapons, his Dire Orb, and Quake movement.

The weapons use actual Quake Champions Blender source files and textures, reanimated in Blender with ambient weapon movements inspired by Quake 2.

> **Release: Coming Soon** on itch.io.
>
> Website: https://renegade-android.github.io/DoomedRanger/

## Arsenal

Doom weapon spots roll from pools of Quake guns, so each run plays differently. Alt-fire on any gun gives a light zoom.

| Slot | Weapon | Notes |
|---|---|---|
| 1 | Blaster | Unlimited glowing bolts. Your starting gun. |
| 2 | Boomer | Eight-pellet shotgun. |
| 3 | Machine Gun | Quake 2-style hitscan. |
| 4 | Super Shotgun | 20-pellet double blast. |
| 5 | Chaingun | Spins up, then shreds. |
| 5 | Nailgun | 10 nails a second. Kills can pin bodies to walls. |
| 6 | Grenade Launcher | Lobbed grenades. Good for grenade jumps. |
| 6 | QCon Rocket Launcher | Quake-tuned rockets and rocket jumps. |
| 6 | Homing Launcher | Seeker rockets that track targets. |
| 6 | Tribolt | Three-bolt explosive volley with kickable casings. |
| 7 | Hyperblaster | Three red energy bolts per shot. |
| 7 | Thunderbolt | Lightning beam. Discharges if you fire it underwater. |
| 8 | Plasma Disruptor | Rapid plasma. Kills vaporize. |
| 8 | Eelsbane | Green acid plasma. Uses Fuel; rare Arachnotron drop. |
| 9 | Railgun | Piercing 100-damage rail. |
| 0 | Tormentor | Green acid stream. Uses Fuel; rare Mancubus drop. |
| 9 | Hellraiser | Fiery piercing rail that ignites every target it hits. Rare Arch-vile drop. |
| 0 | BFG10K | Green energy orb, electrical arcs, blast ring, and BFG spray. |
| 0 | Chainsaw Gauntlet | Alternating chainsaw swings. |
| 0 | QCon Flamethrower | Flame stream that leaves enemies burning. Uses Fuel. |

Fuel is a separate ammo pool shared by the Flamethrower, Tormentor, and Eelsbane: 300 maximum, or 600 with a backpack. Quake 4 napalm canisters give 60 Fuel; large tanks give 120. One in four Cell/Cell Pack map spots supplies Fuel, while the rest retain Cells. Mappers can place Fuel using editor numbers 27016 and 27017.

Mancubi have a 15% chance to drop Tormentor. Arachnotrons have a 15% chance to drop Eelsbane. Arch-viles have a 20% chance to drop Hellraiser. Ordinary Doom II monsters and compatible replacement subclasses can supply these weapons; Champions Lite is not required. Friendly monsters never roll these drops, and resurrection cannot repeat a drop roll. Server settings `dr_tormentor_drop_chance`, `dr_eelsbane_drop_chance`, and `dr_hellraiser_drop_chance` adjust the chances.

The three monster weapons do not appear in normal map weapon pools. Pick up the dropped weapon to unlock it, then use its slot key to cycle to it.

Tormentor sprays a visible stream of falling acid droplets with approximately the Flamethrower’s reach, green barrel smoke, and no muzzle flash. Eelsbane fires fast green acid plasma. Both apply a brief corrosion effect. Tormentor impacts leave green wall splashes and drips plus temporary floor pools, using original Quake 4 acid artwork. Eelsbane has compact green plasma bolts and a downrange energy trail; Railgun and Hellraiser use red flashes. Hellraiser fires a piercing fiery rail that sets every enemy it hits alight; it uses the Railgun’s existing ammo, rather than Fuel.

## Dire Orb

Press **F** to throw a fast orb that passes through enemies, then press **F** again to teleport to it with your momentum kept. Anything standing where you land gets telefragged into gibs. If the orb hits a wall, it holds there for the rest of its 5 seconds. If there's no room to land, the orb stays live so you can try again, and if you never follow it, it detonates on its own. The cooldown is 30 seconds, and enemies can drop a Quake Champions hourglass that cuts 5 seconds off it.

## Movement

- **Quake 2 ground physics** with **CPM air control**: hold forward in the air to steer your speed.
- **Ground slide** from Quake Champions: crouch as you land at speed.
- **Weapon jumps**: rocket and grenade jumps, plasma wall-climbs, nail boosts. Your own splash damage is cut to 25%.
- **Boot kick (R)**: knocks enemies back, opens doors, flips switches, and pushes you off walls.

## Weapon handedness

Press **J** to hold your weapon right, centered, or left, as in Quake 2. Each hand position has its own animations, and shots leave from that muzzle, so the hand you pick changes your line of fire. The crosshair stays stable as you look around, with alignment for the selected weapon and hand; `dr_hand_crosshair false` restores a screen-centered reticle.

## More Quake in your Doom

- Green, Yellow, and Red armor tiers. Megahealth drains back to 100. Quad Damage, Protection, Bandolier, and Adrenaline, with expiry warnings.
- Kills vaporize, burn, or get pinned to walls, and corpses gib when you shoot them.
- A Quake 2-style HUD with a Ranger face and the orb cooldown, plus crosshairs that switch by weapon type.
- 3D weapon and pickup models, first-person legs, custom shaders, dynamic lights, the Ranger's voice, and title music.
- Mapper editor numbers 27001-27017.

## Requirements and install

You need [UZDoom](https://github.com/UZDoom/UZDoom) (the mod's ZScript targets 4.14.0) with OpenGL or Vulkan, and a Doom IWAD. Doom II is recommended so the Super Shotgun spawns. Once it's released, launch it with:

```
uzdoom -iwad doom2.wad -file DoomedRanger.pk3
```

You can rebind the keys under *Customize Controls → Doomed Ranger*. The HUD can be placed at the top or bottom of the screen through the HUD Position option. Mod options are in *Options → Doomed Ranger*. Server CVARs include `dr_dire_orb_enabled`, `dr_dire_orb_cooldown`, `dr_cooldown_drop_chance`, and `dr_body` for the first-person legs.

## Recommended Addon Mods

- [DDS Textures & Super Shaders Suite](https://www.moddb.com/mods/dds-texturespbr-plus)

## Engine & Launcher

- [UZDoom](https://github.com/UZDoom/UZDoom/releases)
- [RENEGADE DOOMER LAUNCHER](https://renegade-android.github.io/rdl/)

## Credits

Created by **RENEGADE ANDROiD (Shawn)**. Third-party material belongs to its owners. Details are in `credits/`.

- **id Software / Bethesda**: Quake Champions weapons, hourglass, and HUD art; the Quake Live Ranger voice and effects; Doom 3 BFG artwork; Quake II sounds; Quake nailgun behavior.
- **Raven Software / id Software / Bethesda**: Quake 4 flame and acid artwork, flamethrower audio, and napalm canister model, textures, and Fuel HUD icon.
- **References**: R1Q2 (Quake 2 physics), Xonotic (CPM air control), Brutal Quake Arena (kick distances).

## Permissions

You can play a public release as provided. Reusing this original work requires the modder's explicit permission, and third-party material keeps its own terms. See [PERMISSIONS.md](PERMISSIONS.md).

The Fuel pickup uses the original Quake 4 napalm canister model and textures. Tormentor, Eelsbane, and Hellraiser use their original Quake Champions Blender meshes, textures, UVs, and surface normals. Their acid, ignition, and loot code is authored for Doomed Ranger.
