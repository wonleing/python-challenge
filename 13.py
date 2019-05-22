#!/usr/bin/python
import xmlrpclib,httplib,urllib
h1 = httplib.HTTPConnection('www.pythonchallenge.com')

#header={"phone":"5","Content-Length":"0"}
body1="""
<methodCall>
  <methodName>system.listMethods</methodName>
  <params></params>
</methodCall>"""
h1.request("POST","/pc/phonebook.php",body1)
res=h1.getresponse()
print res.status,res.read()

body2="""
 <methodCall>
   <methodName>phone</methodName>
   <params>
      <param>
        <value><string>Bert</string></value> 
      </param>
    </params>
 </methodCall>"""
h1.request("POST","/pc/phonebook.php",body2)
res=h1.getresponse()
print res.status,res.read()
h1.close()
print "=================================="
conn = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print conn.system.listMethods()
print conn.phone("Bert")
