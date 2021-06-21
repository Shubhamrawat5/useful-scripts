import requests

def getNews():
        print("Getting news from api!")
        url = 'https://news-pvx.herokuapp.com/'
        page = requests.get(url)
        dict = eval(page.text)

        List = []
        count=0
        for sites in dict.keys():
                List.append("\n\n=== "+sites.upper()+" ===")
                for heading in dict[sites]:
                        count+=1

                        #if count==11:
                        #List.append("\n\n🌐 Join @pvxtechnews for daily tech news !")
                        List.append("\n\n🌐")

                        List.append(heading)

        print(count)
        return List



List=getNews()
List.insert(0,'☆☆☆☆☆💥 Tech News 💥☆☆☆☆☆')
#print(List)

text = " ".join(List)
print(text)
