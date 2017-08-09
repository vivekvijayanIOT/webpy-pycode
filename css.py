import cgi,cgitb
import random
class CSS:
	mystyle='''<style> 

	@import url('https://fonts.googleapis.com/css?family=Bangers|Faster+One|Nosifer');
body {
  background:none repeat scroll 0 0 #d3d3d3;
  font-size:16px;
  font-family:"Open Sans",Arial,sans-serif;
  color:#444;
}
h1,h2,h3,h4,h5,h6 {
  color:#152732;
  font-weight: normal;
  line-height: 1.3;
  margin:0.5rem 0;  
}
.st
{
	font-family: 'Nosifer', cursive;
	font-size:30;
	text-align:center;
}

h1 {font-size:2.7rem;}
h2 {font-size:2.2rem;}  
h3 {font-size:1.8rem;}  
h4 {font-size:1.4rem;}  
h5 {font-size:1.1rem;}  
h6 {font-size:0.9rem;}    
a, a:link, a:visited, a:hover, a:active {
  text-decoration:none;
  color:#9BB800;
  transition:color 0.20s linear 0s;
  -o-transition:color 0.20s linear 0s;
  -ms-transition:color 0.20s linear 0s;
  -moz-transition:color 0.20s linear 0s;
  -webkit-transition:color 0.20s linear 0s;
}  
a:hover {color:#B6C900;}
p,li,dl,blockquote,table,kbd {
   line-height: 1.6;
}
b,strong {font-weight:700;}
.text-center {text-align:left!important;}
.text-right {text-align:right!important;}
img {
  border:0;
  display:block;
  height:auto;
  max-width:100%;
  
}
.h2
{
  color: white;
  text-align: left;
}
.owl-item img, .full-img {
  max-width: none;
  width:100%;
}  
body {
	background: url("../img/background.jpg") no-repeat fixed center center / 100% auto rgba(0, 0, 0, 0);
}
nav {
	background: none repeat scroll 0 0 rgba(0, 0, 0, 0);
	position: absolute;
	top: 0;
	z-index: 500;
}
.top-nav {
	background: none repeat scroll 0 0 rgba(0, 30, 34, 0.85);
}
.top-nav ul {
	padding: 0;
}
.logo {
	margin: 0;
	text-align: center;
	width: 100%;
}
.top-nav li a {
	font-size: 0.9rem;
	text-transform: uppercase;
}
.top-nav .logo a, .top-nav .logo.active-item a {
	color: #fff;
	font-size: 1.4rem;
	font-weight: 400;
	line-height: 1rem;
}
.top-nav .logo a strong {
  font-weight: 800;
  line-height: 1.5;
}
.top-nav {
	text-align: center;
}
.top-nav li a:hover, .top-nav li.active-item a, .top-nav .logo.active-item a:hover {
	background: none repeat scroll 0 0 #00464f;
}
.top-nav li.logo a, .top-nav li.logo.active-item a, .top-nav .logo {
	background: none repeat scroll 0 0 #c53791;
}
nav ul li ul li {
	text-align: left;
}
.top-nav ul ul {
	background: none repeat scroll 0 0 rgb(0, 30, 34);
}
.top-nav li ul li a {
	background: none repeat scroll 0 0 rgb(0, 30, 34);
}
#fourth-block h2 {
	color: #fff;
}
#fourth-block p {
	color: #fff;
}
#first-block, #second-block, #third-block, #fourth-block {
	text-align: center;
	padding: 4.5rem 0;
}
#carousel {
	background: #fff;
}
#first-block {
	background: #fff;
}
#second-block {
	background: none repeat scroll 0 0 rgba(0, 30, 34, 0.85);
}
#third-block {
	background: #fff;
}
#fourth-block {
	background: rgb(0, 30, 34);
}
footer {
	background: none repeat scroll 0 0 #2fcbe0;
	padding: 1.5em 0;
}
footer p, footer a:link, footer a:visited, footer a:hover {
	color: #fff;
}
.carousel-text {
	display: block;
	position: absolute;
	top: 25%;
	width: 100%;
	z-index: 999;
}
.carousel-text h2 {
	background: none repeat scroll 0 0 #fff;
	color: rgb(0, 30, 34);
	display: inline-block;
	padding: 0.3125rem 0.625rem;
	font-size: 2em;
}
.carousel-text p {
	background: none repeat scroll 0 0 rgba(0, 30, 34, 0.85);
	color: #fff;
	display: inline-block;
	font-size: 1.2rem;
	padding: 0.625rem 0.8rem;
}
#first-block i {
	background: none repeat scroll 0 0 #2fcbe0;
	border-radius: 100px;
	color: #fff;
	display: block;
	line-height: 100px;
	margin: 0 auto;
	width: 100px;
}
section h2 {
	font-size: 2.5rem;
	font-weight: 300;
	margin: 0;
	text-transform: uppercase;
}
p.subtitile {
	color: #999;
	margin: 0 0 3.5rem;
}
section h3 {
	font-size: 1.3rem;
	font-weight: 300;
	margin: 0.8rem 0;
	text-transform: uppercase;
}
section p {
	font-size: 0.8rem;
}
section h1 {
	color: #fff;
	font-size: 2.5rem;
	font-weight: 300;
	text-transform: uppercase;
}
#second-block p {
	color: #fff;
}
a.button {
	background: none repeat scroll 0 0 #2fcbe0;
	border: 0 none;
	border-radius: 5px;
	color: rgb(0, 30, 34);
	font-size: 0.8rem;
	font-weight: 600;
	padding: 0.625rem;
	text-transform: uppercase;
}
#head {
	background: none repeat scroll 0 0 rgba(0, 30, 34, 0.85);
	padding: 9rem 0 5rem;
	text-align: center;
}
#content {
	background: none repeat scroll 0 0 #fff;
	padding: 5rem 0;
	text-align: center;
	border-bottom: 1px solid #f0f0f0;
}
#content h2 {
	font-size: 1.5rem;
	font-weight: 400;
	margin: 1rem 0 0.3rem;
	text-transform: none;
}
.content-block {
	background: none repeat scroll 0 0 rgb(0, 30, 34);
	padding: 2.5rem;
}
.content-block h3 {
	color: #fff;
}
.content-block p {
	color: #fff;
}
#content.left-align {
	text-align: left;
}
#content.contact-page h2 {
	margin: 0 0 0.625rem;
}
.contact-page p {
	font-size: 1rem;
	font-style: normal;
}
.contact-page i {
	background: none repeat scroll 0 0 rgb(0, 30, 34);
	border-radius: 100px;
	display: inline-block;
	height: 35px;
	line-height: 35px;
	margin: 0.3125rem 0.3125rem 0.3125rem 0;
	text-align: center;
	width: 35px;
}
form.customform button {
	background: none repeat scroll 0 0 rgb(0, 30, 34);
	border-radius: 5px;
	transition: background 0.20s linear 0s;
	-o-transition: background 0.20s linear 0s;
	-ms-transition: background 0.20s linear 0s;
	-moz-transition: background 0.20s linear 0s;
	-webkit-transition: background 0.20s linear 0s;
}
form.customform button:hover {
	background: none repeat scroll 0 0 #2fcbe0;
}
form.customform input, form.customform select, form.customform textarea {
	border-radius: 5px;
}
#map-block iframe {
	display: block;
}
@media screen and (max-width: 768px) {
  body {
  	background: none repeat scroll 0 0 rgb(0, 30, 34);
  }
  nav {
  	background: none repeat scroll 0 0 rgb(0, 30, 34);
  	line-height: 1rem;
  	position: relative;
  }
  .top-nav {
  	text-align: left;
  }
  .top-nav li {
  	line-height: 3rem;
  }
  .top-nav .logo {
  	padding: 1.25rem;
  }
  .carousel-text h2 {
  	font-size: 1.3rem;
  }
  .carousel-text p {
  	font-size: 1rem;
  }
  ul.top-ul {
  	padding: 0;
  }
  ul.top-ul.right {
  	float: none;
  }
  footer {
  text-align: center;
  }
  footer .right {
  float: none;
  }
}
 .button {
  display: inline-block;
  padding: 15px 25px;
  font-size: 24px;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  outline: none;
  color: #fff;
  background-color: #c53791;
  border: none;
  border-radius: 15px;
  box-shadow: 0 9px #000;
}

.button:hover {background-color: #c53794}

.button:active {
  background-color: #c53794;
  box-shadow: 0 5px #666;
  transform: translateY(4px);
}
.text
{
   font-size:12px;
   color: white;
   text-align: center;
}
.names
{
   font-size:20px;
   color: #c53791;
   text-align: center;
}

</style>
'''