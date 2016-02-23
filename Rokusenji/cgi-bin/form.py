#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import cgi
from simple_template import SimpleTemplate
import template
import smtplib
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email.Header import Header
#from email import charset
import sys

def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

def create_message(from_addr,to_addr,subject,form):
	text=""
	charset="ISO-2022-JP"
	text=text+"お名前 = "+form["お名前"].value+"\n"
	text=text+"ふりがな = "+form['ふりがな'].value+"\n"
	if form.has_key('郵便番号'):
		text=text+"郵便番号 = "+form["郵便番号"].value+'\n'
	if form.has_key('住所'):
		text=text+"住所 = "+form["住所"].value+'\n'
	if form.has_key('e-Mail'):
		text=text+"e-Mail = "+form["e-Mail"].value+'\n'
	if form.has_key('性別'):
		text=text+"性別 = "+form["性別"].value+'\n'
	if form.has_key('年齢'):
		text=text+"年齢 = "+form["年齢"].value+'\n'
	if form.has_key('歯の状況'):
		text=text+"お問い合わせ内容 = "+form["歯の状況"].value+'\n'
	#msg = MIMEText(text.encode(charset),"plain",charset)
	msg = MIMEText(text.decode("utf-8"),"plain",charset)
	msg['Subject']=Header(subject,'utf-8')
	msg['From']=from_addr
	msg['To']=to_addr
	msg['Date']=formatdate()
	return msg

def create_message_patient(from_addr,to_addr,subject,body):
	text=body
	charset="ISO-2022-JP"
	msg = MIMEText(text.decode("utf-8"),"plain",charset)
	#msg['Subject']=subject.encode(charset,'ignore')
	msg['Subject']=Header(subject,'utf-8')
	msg['From']=from_addr
	msg['To']=to_addr
	msg['Date']=formatdate()
	return msg

def send_message(from_addr,to_addr,msg):

	charset="ISO-2022-JP"
	s=smtplib.SMTP('localhost:25')
	s.set_debuglevel(True)

	s.connect()
	s.sendmail(from_addr,[to_addr],msg.as_string())
	s.close()

class sendGmail():
	username,password="rokusenji.shika@gmail.com",'RokusenjiShika0130'
	def __init__(self,from_addr,to_addr,sub,body):
		host,port='smtp.gmail.com',465
		if type(body)==type("str"):
			warning("in patient")
			warning(type(body))
			msg=create_message_patient(from_addr,to_addr,sub,body)
		else:
			warning("in doctor")
			warning(type(body))
			msg=create_message(from_addr,to_addr,sub,body)

		smtp=smtplib.SMTP_SSL(host,port)
		smtp.ehlo()
		smtp.login(self.username,self.password)
		smtp.mail(self.username)
		smtp.rcpt(to_addr)
		smtp.data(msg.as_string())
		smtp.quit()

form = cgi.FieldStorage()
form_check=0
if form.has_key("お名前") and form.has_key("e-Mail"):
	form_check=1
if form_check==0:
	print("error")
else:
	warning(form["お名前"].value)
	warning(form["e-Mail"].value)
	me="rokusenji.shika@gmail.com"
	you=form["e-Mail"].value
	#相手に送る
	message=""
	message=message+form["お名前"].value+"様\n"
	message=message+"""
この度は「六泉寺歯科」にお問い合わせ頂きありがとうございます。
折り返しご連絡致しますので、しばらくお待ち下さい。

お急ぎの場合はお手数ですが、下記電話番号までお問い合わせ下さい。
よろしくお願いします。

電話番号 088-833-6406
「六泉寺歯科」
	"""
	sendGmail(me,you,"「六泉寺歯科」お問合わせありがとうございます",message)

	#msg=create_message(me,me,"「六泉寺歯科」お問い合わせフォームより",form)
	#send_message(me,you,msg)
	#for i in range(5):
	sendGmail(me,me,"「六泉寺歯科」お問い合わせフォームより",form)
	pass
	#print "<h2>PRINT</h2><hr>"
	#print "<b>name: </b>", form["お名前"].value
	#print "<b>mail: </b>", form["e-Mail"].value


print("Content-Type : text/html\n")
print(template.header())
print("""
<h2 id="title01">お問い合わせ</h2>
<div class="section">
    <h3 id="title02">お問い合わせ</h3>
    <div class="section">
    	<p>お問い合わせありがとうございました。</br>
    		正常に送信されました。
    	</p>
    	<form>
    		<fieldset>
    			<p class="center"><input type="button" class="button" value="前のページへ" onClick="window.open("http://www.rokusenji-sika.com/","_top")" style="" /></p>
    		</fieldset>
    	</form>
	</div>
</div>
""")

"""
<div id="app">
	<div>
		<input v-model="agree" type="checkbox"/>利用規約に同意します
		<button v-attr="disabled: !agree">Submit</button>
	</div>
	<div>
        <input v-model="textValue" />
        <button v-attr="disabled: textValue == ''">Submit</button>
      </div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/vue/1.0.16/vue.min.js"><script/>
<script type="text/javascript">
	var app=new Vue({
		el:'#app',
		data:{
			agree:false,
			textValue:''
		}
	});
</script>
"""
print(template.footer())

'''
print "Content-Type : text/html\n"
print "<html><body>"

form = cgi.FieldStorage()
form_check=0
if form.has_key("お名前") and form.has_key("e-Mail"):
	form_check=1
if form_check==0:
	print "<h1>ERROR!</h1>"
else:
	print "<h2>PRINT</h2><hr>"
	print "<b>name: </b>", form["お名前"].value
	print "<b>mail: </b>", form["e-Mail"].value
	t=SimpleTemplate("""
<select name="fruit">
$for val in ["Apple", "Banana", "Melon"]:
    <option value="${val}">${val}</option>
$endfor
</select>
""")
	print t.render()

#print template.footer()
print "<p>あ<p/>"
print "</body></html>"
'''
