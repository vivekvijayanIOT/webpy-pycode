#!/usr/bin/python
# Created by VivekIOT 
# My package for all my projects      **** DO NOT EDIT else ADMIN *****
import random
import string
import cgi,cgitb
class vivek:
	def gender_of_(self,name):
	    check_name=('a','e','i','o','u','y','l','un','um')
	    double_check=('mu','ky','ul','aja','ari','hnu','run','urya','babu','bu','ence','anjay','ee','opi','ravana','eeva','jai','jay','rishna','uriya')
	    if name.endswith(double_check):
	        return "Male"
	    elif name.endswith(check_name):
	        return "Female"
	    else:
	        return "Male"
	def time(self):
		times=['Good Time','Bad Time','Nalla kaalam','Kasta Kaalam']
		return random.choice(times)	

   	def friends(self):
   		friends=['punniyam','nallathu','Kettathu','Keduthal','Paavam']
   		return random.choice(friends) 

   	def studies(self):
   		studies=['Konjam dull ah padipeenga','Sammaya padipa','Fail aavenga','copy adichu than pass eh pannuvenga','Kadaisi varaikum puriyamaley padipenga']
		return random.choice(studies)

	def going_to(self,me):
		wife=['kuda Santhoshama iruppa','Kitta setthhha','Kita adi vanguva','sollama odi poyiduva']
		hus=['kuda Santhoshama iruppa','Kitta setthhha...haha','Kita adi vanguva..sooo usharr','innoruthiyoda odi poyiduva... better luck next time']
		if (me=='Female'):
			status=random.choice(hus)
		else:
			status=random.choice(wife)
		return status

	def img_select(self):
		num=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']#'27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50']
		return random.choice(num)

	def comedy(self):
		com=['Rice 1Rs ku iruku..atha kuda unnala vangamudiyathu','Ne elam poranthathey oru sabakedu..','Un Life nalla irukuma nu doubt than','Un life paravala','Ne oru comedy piece']
		return random.choice(com)

	def love(self,me):
		loveb=['athu Set agathu','Success agidum','athu Nasamapoidum','it Last for ever ','Avaley unaku pondati ah varuval','She will be ur Wife...jamaai']
		loveg=['athu Set agathu','Success agidum','athu Nasamapoidum','it Last for ever ','Avaney unaku Purushan ah varuvan','he will be your Husband']
		if (me=='Female'):
			status=random.choice(loveg)
		else:
			status=random.choice(loveb)
		return status
		