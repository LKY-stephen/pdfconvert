# -*- coding:utf-8 -*-
import os
import sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
#this is the kern of my new convert software.
#now flag means the type of image bmp:1,png:2,jpg:3
#
#version 3.0 author:Stephen


def get_file(path,filelist):
	files = os.listdir(u"%s"%path)
	dict={".png":2,".jpg":3,".bmp":1}
	for f in files:
		if(os.path.isfile(path + '/' + f)):   
			flag=dict.get(f[-4:],0)
			if flag:
				filelist.append(path + '\\' + f)
				
def draw_pic(filelist):
	l=len(filelist)
	c = canvas.Canvas('result.pdf', pagesize = landscape(A4))
	for i in range(l):
		f=filelist[i]
		(w, h) = landscape(A4)
		c.drawImage(f, 0, 0, w, h)
		c.save()
		
	