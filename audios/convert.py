import os

for _, _, files in os.walk("."):
    for f in files:
        if not f.endswith(".m4a"):
            continue

        os.system(f"ffmpeg -i {f} -c:a libvorbis {f[:-4]}.ogg")
