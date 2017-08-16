#coding=utf8
import itchat
itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)[0:]


print type(friends)

#print friends[0:100]
#ac=['sss','sasasas']
#values = ','.join(str(v) for v in value_list)
frid=''.join(str(v) for v in friends)  #list类型转换成str类型
file_frd=open('frd.txt','w')
#f.writelines(frid)  
file_frd.write(frid)
file_frd.close()  

#a=['1','2','3','4','33']
#b=['dd','ddd','d']
#cf={a:b}
#