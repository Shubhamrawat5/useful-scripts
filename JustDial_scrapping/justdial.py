from bs4 import BeautifulSoup as bs

r=open("jd.txt",'r')

code=r.readlines()
r.close()
#print(type(code))
soup=bs("".join(code),"lxml") #creating soup object

#print(soup)

def makePhoneNumb(p_tag):
    numb="" #to store phone number

    digits=p_tag.findAll("span") #each digit of phone numb are in different span tag
    for digit in digits:
        #print(digit)
        n=digit['class'][1][5:] #in class attribute the phone code is given
        #print(n)
        try:
            numb+=d[n]
        except:
            break
    return (numb)
    
names=soup.findAll("span",class_="lng_cont_name")   #name
p_tags=soup.findAll("p",class_="contact-info")  #phone numbers
addresses=soup.findAll("span",class_="cont_fl_addr")    #address
#list is created
print(len(names))
print(len(p_tags))
print(len(addresses))

#phone number digit 0 to 9 codes in justdial
d={"acb":"0","yz":"1","wx":"2","vu":"3","ts":"4","rq":"5","po":"6","nm":"7","lk":"8","ji":"9"}

numbList=[]
for i in range(len(p_tags)):
    p_tag=p_tags[i].span #getting one by one values from list 
    t=makePhoneNumb(p_tag) #getting and making phone number as phone numbers are not directly available, instead they are in differnet tags and written in code
    #address and names are given directly
    #if t != '':
    #    numbList.append(names[i].text+' \n '+t+'\n '+addresses[i].text)
        
    if t != '':
        numbList.append(names[i].text+' \n '+t[:7]+'XXX'+'\n '+addresses[i].text)
    
print(numbList)
w=open("list1.txt",'w')
txt="\n\n".join(numbList)
w.writelines(txt)
w.close()