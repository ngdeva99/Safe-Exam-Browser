#!/usr/bin/env python
# coding: utf-8

# In[1]
# In[2]:

import time
import webbrowser
import os
from pathlib import Path
import xml.dom.minidom as md
from shutil import copyfile


def myfun():
	software = 'SEB_3.0.1.163_SetupBundle.exe'

	renamed_software = 'SSN_EXAM.exe'

	seb_software = 'SebClientSettings.seb'

	seb_renamed_software = 'SSN_EXAM_SETTINGS.seb'





	print("WELCOME TO SSN CAMPUS EXAM 2020")

	choices = [False]*2

	#print("The path of Your Download directory is:")
	downloads_path = str(Path.home())+"\\"+"Downloads\\"
	#like C:/Users/Messi/Downloads/
	def repl(downloads_path):
		path = []
		for i in downloads_path:
			if i=="\\":
				path.append('/')
			else:
				path.append(i)

		path = "".join(path)
		return path

	path = repl(downloads_path)
	#print(path)
	


	zoom_path = str(Path.home())+"\\AppData\\Roaming\\Zoom\\bin\\"
	zoom_path1 = repl(zoom_path)
	#print(zoom_path1)


	seb_path = str(Path.home())+"\\AppData\\Roaming\\SafeExamBrowser"

	entry  = True

	####################

	def copy():

		seb_path = str(Path.home())+"\\AppData\\Roaming\\SafeExamBrowser\\"
		seb_path1 = repl(seb_path)
		#print(path+'SebClientSettings.seb',seb_path1+'SebClientSettings.seb')


		copyfile(path+'SSN_EXAM_SETTINGS.seb',seb_path1+'SSN_EXAM_SETTINGS.seb')

	def backend(zoom_path):




		file = md.parse(path+"SSN_EXAM_SETTINGS.seb")
		value = file.getElementsByTagName("string")[ 28 ].childNodes[ 0 ].nodeValue
		#print(value)
		file.getElementsByTagName( "string" )[ 28 ].childNodes[ 0 ].nodeValue=zoom_path
   
		with open(path+"SSN_EXAM_SETTINGS.seb", "w" )as fs:
			fs.write(file.toxml())
			fs.close()

		copy()

	def install():
		#print("Kindly cross-check if "+software+" file is Downloaded in the location "+path)

		choices[1] = True
		os.startfile(path+renamed_software)
		return 

	def install1():
		#print("Kindly cross-check if "+software+" file is Downloaded in the location "+path)

		choices[1] = True
		os.startfile(path+renamed_software)

		print("Was the Installation succesful? Type (y/n) letter y for Yes and n for no and hit Enter")
		i = input()
		if i=='y':
			return
		else:
			print('Kindly delete the '+renamed_software+' file available in location '+path+' and restart this application again.')
			return 

	####################


	while entry or choice!=3:
		entry = False


		print("Press number 1 and hit enter for Downloading the software.")

		choice = input()
		choice = int(choice)

		if choice == 1:
			if os.path.isfile(path+renamed_software):
				print("Already Downloaded")
				install1()
				choice = 3
				continue 

			choices[0] = True
			#webbrowser.open('https://sourceforge.net/projects/seb/files/latest/download')
			webbrowser.open('https://drive.google.com/file/d/1uOVFdDlYzn-nwdTj9Kt59pwBjr151VZN/view?usp=sharing')
			webbrowser.open('https://drive.google.com/file/d/1XVzUmcVThWhi-EIuVfC-gpuIifZ_kZtS/view?usp=sharing')
		#elif choice ==2:


			print("\n Please wait for the Download to finish!")
			while not os.path.isfile(path+software) or not os.path.isfile(path+seb_software):
				#if not choices[0]:
				#else:
				
				continue

			#if choices[1]:
			#	print("Kindly Check if the software is already installed")
			#	continue


			os.rename(path+seb_software,path+seb_renamed_software)
			os.rename(path+software,path+renamed_software)

			install()

		print("Was the Installation succesful? Type (y/n) letter y for Yes and n for no and hit Enter")
		i = input()
		if i=='y':
			choice = 3
			continue
		else:
			install()

		if i!='n':
			choice = 3

	print("\n Do not exit. Background processes running.")
	backend(zoom_path)


	print("\n Thank You for choosing SSN.")
	time.sleep(5)

myfun()
# In[ ]:




