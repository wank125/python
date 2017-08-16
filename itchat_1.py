#coding=utf8
import itchat
itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)[0:]

print type(friends)
#print friends[0:100]
ac=['sss','sasasas']
f = open('itchat_1.txt','w')  
f.writelines(ac)  
f.close()  