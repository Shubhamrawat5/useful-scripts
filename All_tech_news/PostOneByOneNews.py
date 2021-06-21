import requests
import keyboard
import time


def getNews():
    print("Getting news from api!")
    url = 'https://news-pvx.herokuapp.com/'
    page = requests.get(url)
    dict = eval(page.text)

    List = []
    count = 0
    for sites in dict.keys():
        List.append("\n\n=== "+sites.upper()+" ===")
        for heading in dict[sites]:
            count += 1

            # if count==11:
            #List.append("\n\n🌐 Join @pvxtechnews for daily tech news !")
            # List.append("\n\n🌐")

            List.append(heading)

    print(count)
    return List


List = getNews()
# List.insert(0,'☆☆☆☆☆💥 Tech News 💥☆☆☆☆☆')

# text = " ".join(List)
# print(text)
print(List)
count = 0

time.sleep(2)
for news in List:
    count += 1
    # if count == 5:
    #     break
    keyboard.write(news)
    keyboard.press_and_release('enter')
    time.sleep(5)
