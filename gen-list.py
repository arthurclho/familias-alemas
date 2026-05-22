import os

LIST_ITEM_TEMPLATE = """        <li class="list-item">
          <h3>{nome}</h3>
          <button type="button" onclick="playAudio(this, '{audio_file}')"/>
        </li>
"""

for _, _, files in os.walk('./audios'):
    for f in sorted(files):
        if not f.endswith(".m4a"):
            continue
        
        print(LIST_ITEM_TEMPLATE.format(nome=f[:-4], audio_file=f), end='')
