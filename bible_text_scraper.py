from bs4 import BeautifulSoup
import requests
import gtts
from playsound import playsound

for i in range(34, 35):
    textString = ""
    req = requests.get(
        f"https://wol.jw.org/es/wol/b/r4/lp-s/nwtsty/5/{i}#study=discover"
    )
    soup = BeautifulSoup(req.text, "html.parser")

    article = soup.find_all("article", {"id": "article"})

    paragraphs = soup.find_all("span", {"class": "v"})

    for paragraph in paragraphs:
        textString += paragraph.get_text()

    textString = textString.replace("+", "")
    textString = textString.replace("*", "")

    textString = "".join([i for i in textString if not i.isdigit()])

    tts = gtts.gTTS(textString, lang="es")

    tts.save(f"deutoronomio_{i}.mp3")
