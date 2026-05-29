import os
import sys
import subprocess

SOURCE_FOLDER = sys.argv[1]
DEST_FOLDER = sys.argv[2]

for _, _, files in os.walk(SOURCE_FOLDER):
    for i, f in enumerate(files):
        if not f.endswith(".m4a"):
            continue

        src_path = os.path.join(SOURCE_FOLDER, f)
        dest_path = os.path.join(DEST_FOLDER, f[:-4] + ".ogg")
        if os.path.exists(dest_path):
            continue

        print(f"Converting audio {i} of {len(files)}")
        subprocess.run(["ffmpeg", "-i", src_path, "-c:a", "libvorbis", dest_path],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL,
                       check=True)
