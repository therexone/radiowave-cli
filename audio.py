import vlc
from time import sleep
import os
import sys
import subprocess
from gif_for_cli.execute import execute
import requests
import random
from termcolor import colored


audio_url = "https://air.radiorecord.ru:805/synth_320"

# Setup vlc player
def playAudio(url):
     os.system("clear")
     print("------------------RADIOWAVE-CLI-------------------")
     print("# Loading VLC player")
     player = vlc.MediaPlayer(url)
     player.play()
     print("# Done")
     print(colored("# Playing: RADIORECORD.RU", "green"))
     print(colored("# Getting Visuals...", "blue"))

url = "https://api.tenor.co/v1/search?tag=synthwave%20aesthetic&key=LIVDSRZULELA"


gif_list = [
    "https://tenor.com/view/dangiuz-cyberpunk-outrun-synthwave-vaporwave-gif-15605661",
    "https://tenor.com/view/cyberpunk-dangiuz-outrun-synthwave-vaporwave-gif-15605667",
    "https://tenor.com/view/aesthetics-synthwave-wave-gif-13842018",
    "https://tenor.com/view/donal-trump-synthwave-gif-9490543",
    "https://tenor.com/view/synthwave-train-dance-cool-gif-15576627",
    "https://tenor.com/view/80s-retro-new-wave-synthwave-gif-9224660",
    "https://tenor.com/view/new-retro-wave-fm84-synthwave-gif-9224646",
    "https://tenor.com/view/retro-new-wave-80s-fm84-synth-wave-gif-9224658",
    "https://tenor.com/view/synthwave-retrowave-sunset-80s-gif-11771421",
    "https://tenor.com/view/street-cleaner-synthwave-outrun-keytar-rainbow-gif-13305861",
    "https://tenor.com/view/synth-wave-vapor-wave-car-80s-1980-gif-14121139",
    "https://tenor.com/view/psychedelic-trippy-future-synthwave-electro-gif-13956950",
    "https://tenor.com/view/neon-car-cruise-synthwave-80s-gif-12569562",
    "https://tenor.com/view/synthwave-meme-ministry-of-memes-gif-16160313",
    "https://tenor.com/view/totally-rad-disco-synthwave-vaporwave-gif-14777004",
    "https://tenor.com/view/fm84-sunset-drive-80s-new-retro-gif-9224659",
    "https://tenor.com/view/apex-legends-apex-wattson-cyberpunk-synthwave-gif-17121251",
    "https://tenor.com/view/retrowave-synthwave-city-night-city-night-gif-17179282",
    "https://tenor.com/view/hyasynth-keeping-up-appearances-sheridan-hello-wave-gif-4939851",
    "https://tenor.com/view/seb-cat-love-secret-society-cat-meme-gif-15496312",
]

# fetch random gifs with keyword
# response = requests.get(url)
# gif_list = [x['itemurl'] for x in response.json()['results']]


def playGif(url):
    cols = os.get_terminal_size().columns
    rows = os.get_terminal_size().lines
    execute(
        os.environ,
        [
            "--display-mode",
            "256",
            "--rows",
            f"{rows}",
            "--cols",
            f"{cols}",
            "-l",
            "20",
            url,
        ],
        sys.stdout,
    )

if __name__ == '__main__':
     playAudio(audio_url)
     while True:
          try:
               print(colored("\r\n # Press CTRL + C to exit", "yellow"))
               playGif(gif_list[random.randint(0, 19)])
          except KeyboardInterrupt:
               print(colored("\r---------------EXITING----------------", "red"))
               exit(0)
          except FileNotFoundError as e:
               subprocess.call(["rm", "-rf", "~/.cache/gif-for-cli/1.1.2"])

