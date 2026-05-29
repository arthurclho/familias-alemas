import os

LIST_ITEM_TEMPLATE = """        <li class="list-item">
          <h3>{nome}</h3>
          <button type="button" onclick="playAudio(this, '{audio_file}')"></button>
        </li>
"""

for _, _, files in os.walk('./audios'):
    for f in sorted(files, key=str.casefold):
        if not f.endswith(".ogg"):
            continue
        
        print(LIST_ITEM_TEMPLATE.format(nome=f[:-4], audio_file=f), end='')
