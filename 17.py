#!/usr/bin/python
#import cookielib
#cookie = cookielib.CookieJar()
#ckhandler = urllib2.HTTPCookieProcessor(cookie)
#opener = urllib2.build_opener(ckhandler, pwhandler)
#request = urllib2.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345')
#response = urllib2.urlopen(request)
#cookies = cj.make_cookies(response, request)

import urllib,urllib2,bz2,xmlrpclib
#url17 = 'http://www.pythonchallenge.com/pc/return/romance.html'
url4 = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
#password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
#password_mgr.add_password(None, url17, 'huge', 'file')
#pwhandler = urllib2.HTTPBasicAuthHandler(password_mgr)
#opener = urllib2.build_opener(pwhandler)
response = urllib2.urlopen(url4)
print response.info()['Set-Cookie'].split(";")[0]
seed = "12345"
data = ""
while seed:
    link = url4 + "?busynothing=" + seed
    res = urllib2.urlopen(link)
    body = res.read()
    cookie = res.info()['Set-Cookie'].split(";")[0].split("=")[1]
    if "busynothing" in body:
        seed = body.split(" ")[-1]
        data += cookie
        #print seed
    else:
        print body
        data += cookie
        break

print bz2.decompress(urllib.unquote_plus(data))
print "please google who is HIS father, can CALL him" # mozart's father is Leopold
conn = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print conn.phone("Leopold")

header = {'cookie' : 'info=%s' %urllib2.quote('the flowers are on their way')}
req = urllib2.Request("http://www.pythonchallenge.com/pc/stuff/violin.php", headers=header)
print urllib2.urlopen(req).read()
