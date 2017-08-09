#!/usr/bin/env python
import cgi,cgitb
from vivekiot import *
from css import *
viot=vivek()
css=CSS()
form=cgi.FieldStorage()

val1=form.getvalue('my_name')
name="q"
name1="hhii"
print "Content-type:text/html\r\n\r\n"
print '''<!DOCTYPE html>
<html lang="en-US">
   <head>   
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Py Genie</title>
      <!-- CUSTOM STYLE -->
      <link rel="stylesheet" href="css/template-style.css">
      <link href='http://fonts.googleapis.com/css?family=Open+Sans:400,300,600,700,800&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
      <script type="text/javascript" src="js/jquery-1.8.3.min.js"></script>
      <script type="text/javascript" src="js/jquery-ui.min.js"></script>
   </head>
 <body class="size-1140"> '''
print css.mystyle
print '''
      <!-- TOP NAV WITH LOGO -->
      <header>
         <nav>
            <div class="line">
               <div class="top-nav">
                  <div class="logo hide-l">
                    <a href="index.html"><table ><tr><td>'''
data_uri = open('genie.png', 'rb').read().encode('base64').replace('\n', '')
img_tag = '<img height="50" width="50" src="data:image/png;base64,{0}">'.format(data_uri)
print(img_tag)
print '''
</td><td><h3><strong><font color="white">Py</font> </strong><param>Genie</param></h3><h6> Online<font color="white"><i> josiyum </i></font>for you</h6></a></td></tr>
                     </table></a>'''
print '''
                  </div>
                 <a ><br> <p align="center"  >'''
print '''<div align="center"><a href="/webpy/sindex.html"><button>Go Back </button></a></div>'''
name=val1
gg=viot.gender_of_(name)
if (gg=='Male'):
	gen="Brother"
	spouse="Wife"
else:
	gen="Sister"									#<font color='#c53791'> </font>
	spouse="Husband"

time=viot.time()
std=viot.studies()
done=viot.friends()
doing=viot.going_to(gg)
comedy=viot.comedy()
love=viot.love(gg)
but=""
solve=""

if ((time.find('Good')>=0 or time.find('Nalla')>=0 ) and (doing.find('Santhoshama')>=0 )):
	butb="So"
else:
	butb="But"

if ((time.find('Bad')>=0 or time.find('Kasta')>=0 ) and (doing.find('Santhoshama')>=0 )):
	buta="Analum  "
else:
	buta="Athanala "

if (time.find('Bad')>=0 or time.find('Kasta')>=0 ):
	but=buta
elif (time.find('Good')>=0 or time.find('Nalla')>=0 ):
	but=butb 

if ((done.find('punniyam')>=0 or (done.find('nallathu')>=0))):
	solve=" Anathanala onnum nadakaporathu illa.. "


if (name.find('.')>=0 or name.find(' ')>=0):
	print '''<h6 class="text"> Take the Screenshot of your josiyum and put in your status <b><font color='#c53791'>SHARE THIS TO YOUR FRIENDS </font></b> </h6><hr>'''
	print '''<b><div class='sta'><font color='white'>Hey... %s ..  Rules paathiya ...illaya..... </font><font color='#c53791'> Last name and Initial podatha  </font>
<font color='white'> nu potruku la..... ipo soldren nalla ketuko.... </font><font color='#c53791'>unaku matum illa..un street la iruka yarukum Marriage eh agathu</font> 
<font color='white'> Apdiye Oodi poidu
</div></b><br><br><div align="center">'''%(name)
	imgsrc='error'+'.jpg'
	data_uri = open(imgsrc, 'rb').read().encode('base64').replace('\n', '')
	img_tag = '<img height="300" width="300" src="data:image/png;base64,{0}">'.format(data_uri)
	print(img_tag)
	print '''</div>'''

else:
	print '''<h6 class="text"> Take the Screenshot of your josiyum and put in your status <b><font color='#c53791'>SHARE THIS TO YOUR FRIENDS </font></b> </h6><hr>'''
	print "<b><div class='sta'><font color='#c53791'>Hi </font><font color='white'> %s </font></div></b><br>"%gen

	print '''<b><div class='sta'><font color='white'>Hey... %s .. Unoda Time </font><font color='#c53791'> ipo romba  %s </font>
<font color='white'> , %s Ne unnoda %s </font><font color='#c53791'>%s</font> 
<font color='white'> 
,ana <font color='#c53791'>%s</font><font color='white'> ...
 Unnoda Friends eh unaku <font color='#c53791'>%s</font> pannuvanga... Nenga love paniruntha <font color='#c53791'>%s</font>
</div></b>'''%(name,time,but,spouse,doing,comedy,done,love)
	print '''
                  </p>
                  
<font color='white'> <br>Your Future %s will be like  </font><br><br>
                  '''%spouse
	print ''' <div align="center">'''
	img= viot.img_select()
	if (gg=='Male'):
		src='heroine'
	else:
		src='hero'

	imgsrc='pics/'+src+'/'+img+'.jpg'
	data_uri = open(imgsrc, 'rb').read().encode('base64').replace('\n', '')
	img_tag = '<img height="200" width="200" src="data:image/png;base64,{0}">'.format(data_uri)
	print(img_tag)
print '''    <br><br><br><hr>
                  <div align="center">
                <font color="white">Stay connect with us for </font><font color="#c53791">Website and Mobile App Development</font> <br><font color="white"><a href="http://status200.state200ok.com"><b>status200.state200ok.com</b></a></font> 
                <br><br><br><div align="center">
                <font color="white"> - VIOT CREATIONS - </font></div>
         </div>
	            </div></div>
	         </nav>
	      </header>
	      <section>
	         <!-- CAROUSEL -->
	         
	         <!-- FIRST BLOCK -->
	         
	      <script type="text/javascript" src="js/responsee.js"></script>
	      <script type="text/javascript" src="owl-carousel/owl.carousel.js"></script>
	      <script type="text/javascript">
		     jQuery(document).ready(function($) {
		       $("#owl-demo").owlCarousel({
		       	slideSpeed : 300,
		       	autoPlay : true,
		       	navigation : false,
		       	pagination : false,
		       	singleItem:true
		       });

		       $("#owl-demo2").owlCarousel({
		       	slideSpeed : 300,
		       	autoPlay : true,
		       	navigation : false,
		       	pagination : true,
		       	singleItem:true
		       });
		     });</script>
	   </body>
	</html>'''

