import time
import telegram
import requests

ID = "-4102112110"
API = "6970653338:AAHyKFuhqJyoHgn1Vgi30HN6SHSfH2eksYw"


def test():
    locationtime = time.localtime()
    requesrtime = time.strftime("%Y-%m-%d %H:%M:%S", locationtime)
    # print(requesrtime)
    tele = requests.post("https://api.telegram.org/bot" + API +
                         "/sendMessage?chat_id=" + ID + "&text=" + requesrtime + "+GMT+8")
    print(tele.text)


test()

