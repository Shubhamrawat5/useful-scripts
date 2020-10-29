r1 = open('followers.txt','r',encoding='utf-8')
r2 = open('following.txt','r',encoding='utf-8')

followers=r1.readlines()
following=r2.readlines()
l=[]

r1.close()
r2.close()

for i in following:
    if i not in followers:
        l.append(i)


print(l)
s=''.join(l)
w=open('instaResult.txt','w',encoding='utf-8')
w.write(s)
w.close()