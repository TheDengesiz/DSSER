#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os as dengesiz
dengesiz.system('clear' if dengesiz.name == 'nt' else 'reset')

print("""
1) Update Source List 
2) Update && Upgrade
3) İnstall SQLiv , XSSER
4) Who Are We ? 
5) Quit
	""")
me = raw_input("Which of the above ? : ")

if(me == "1"):
	cmd1 = dengesiz.system("echo 'deb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/source.list")
	print("Updated Source List ")
	quit()

if(me == "2"):
	mee = raw_input("Are you sure ? E/h:")
	if(mee == "E"):
		cmd2 = dengesiz.system("apt-get upgrade && apt-get update")
		dengesiz.system('clear' if dengesiz.name == 'nt' else 'reset')
		print("Updated the System")
		quit()
	else:
		print("Permission required !")
		quit()

if(me == "3"):
	print("""
1)SQLiv
2)XSSER
3)Setup All
		""")
	wd = raw_input("Which of the above ? : ")
	if(wd == "1"):
		cmd11 = dengesiz.system("git clone https://github.com/the-robot/sqliv.git")
		dengesiz.system('clear' if dengesiz.name == 'nt' else 'reset')
		quit()

	if(wd == "2"):
		cmd12 = dengesiz.system("git clone https://github.com/epsylon/xsser.git")
		dengesiz.system('clear' if dengesiz.name == 'nt' else 'reset')
		quit()		

	if(wd == "3"):
		cmd13 = dengesiz.system("git clone https://github.com/the-robot/sqliv.git && git clone https://github.com/epsylon/xsser.git")
		dengesiz.system('clear' if dengesiz.name == 'nt' else 'reset')
		quit()

if(me == "4"):
	print("""
		Code By Dengesiz
		@rootTheDengesiz >> Twitter
		https://turkdefarmy.com >> TheDengesiz

		""")
	quit()

if(me == "5"):
	quit()

