# Doomed Ranger website

Source for the Doomed Ranger website: https://renegade-android.github.io/DoomedRanger/

Doomed Ranger is an unofficial fan mod for UZDoom that brings the Quake Ranger into Doom. The mod release is coming soon on itch.io. This repo holds only the website, not the mod.

The published pages are generated from index.template.html and build.py.
mod-readme.md is the current mod documentation used for Fuel and drop details.
Run update_media.py --media-directory <approved GIF folder> --readme <mod README> to refresh the clips and documentation, then run python build.py.
Media conversion requires Pillow and PyAV. Use --runtime-directory to reuse an existing runtime.
The media manifest records the source GIF hashes; unchanged clips are reused.
