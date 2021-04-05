from bs4 import BeautifulSoup
import requests
import gtts

num_book = 9

for i in range(1, 32):
    textString = ""
    req = requests.get(
        f"https://wol.jw.org/es/wol/b/r4/lp-s/nwtsty/{num_book}/{i}#study=discover"
    )
    soup = BeautifulSoup(req.text, "html.parser")

    article = soup.find_all("article", {"id": "article"})

    paragraphs = soup.find_all("span", {"class": "v"})

    for paragraph in paragraphs:
        textString += paragraph.get_text()

    textString = textString.replace("+", "")
    textString = textString.replace("*", "")
    textString = textString.replace("  ", " ")

    textString = "".join([i for i in textString if not i.isdigit()])

    try:
        tts = gtts.gTTS(textString, lang="es")

        tts.save(f"{num_book}_{i}.mp3")
    except:
        print(f"{num_book}_{i} has been saved")