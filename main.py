import time

from playsound import playsound
from requests_html import HTML
from requests_html import HTMLSession
from mail import send_email


def check_apartment():
    print("Check apartment...")
    file = "mixkit-beast-long-roar-306.wav"
    session = HTMLSession()
    r = session.get(
        'https://trouverunlogement.lescrous.fr/tools/flow/21/search?bounds=2.2241_48.9022_2.4698_48.8156&page=1&price=60000')
    r.html.render(sleep=3)

    about = r.html.xpath('//*[@id="SearchResultsList"]', first=True)
    list = about.html
    html = HTML(html=list)
    if len(html.find(".SearchResults-item")) > 0:
        print("Found one.")
        send_email()
        playsound(file)


if __name__ == '__main__':
    while True:
        try:
            check_apartment()
        except:
            print("error")
        print("Sleeping...")
        time.sleep(200)  # In seconds
