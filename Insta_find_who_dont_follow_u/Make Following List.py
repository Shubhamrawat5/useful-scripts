from bs4 import BeautifulSoup
#r = open('fullhtml.txt','r',encoding='utf-8') 

with open('htmlFollowing.txt', encoding="utf8", errors='ignore') as r:
    content=r.read()
    #print(content)
    soup = BeautifulSoup(content, 'html.parser')
    #print(soup.h2)
    #print(soup.head)
    #print(soup.li)
    cl = soup.findAll(class_='d7ByH') #enpQJ
    l=[]
    for i in cl:
        #print(i.text)
        l.append(i.text)

    print(len(l))
    print(str(l))
    list='\n'.join(l)
    w=open('following.txt','w',encoding='utf-8')
    w.write(list)
    w.close()
