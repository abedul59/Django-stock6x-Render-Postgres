import math

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.conf import settings
#from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from myapp import models

def usersmain_common(request, username=None, pageindex=None):  #使用者功能首頁
	global page1u
	pagesize = 20  #8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1u = 1
		newsunits0 = models.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1u-2)*pagesize
		if start >= 0:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u -= 1
	elif pageindex=='2':
		start = page1u*pagesize
		if start < datasize:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u += 1
	elif pageindex=='3':
		start = (page1u-1)*pagesize
		newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1u

######################################################
    #if username=='test168':
        #DB = StockFavs_test168
	'''
	if username==None: #注意分行和空格 不要複製
		
		DB = StockFavs_test168
	elif username=='test168':
		DB = StockFavs_test168  
		'''  

	global page1
	pagesize = 20  #8
	newsall = DB.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = DB.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = DB.objects.order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = DB.objects.order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = DB.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1
    
    
    #MacroWaveA
    
	global page1m
	pagesize = 5 #8
	newsall = models.MacroWaveA.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1m = 1
		newsunitsm = models.MacroWaveA.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunitsm = models.MacroWaveA.objects.order_by('-id')[start:(start+pagesize)]
			page1m -= 1
	elif pageindex=='2':
		start = page1m*pagesize
		if start < datasize:
			newsunitsm = models.MacroWaveA.objects.order_by('-id')[start:(start+pagesize)]
			page1m += 1
	elif pageindex=='3':
		start = (page1m-1)*pagesize
		newsunitsm = models.MacroWaveA.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1m    
    
    #MacroWaveB
	global page1m2
	pagesize = 5 #8
	newsall = models.MacroWaveB.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1m2 = 1
		newsunitsm2 = models.MacroWaveB.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunitsm2 = models.MacroWaveB.objects.order_by('-id')[start:(start+pagesize)]
			page1m2 -= 1
	elif pageindex=='2':
		start = page1m2*pagesize
		if start < datasize:
			newsunitsm2 = models.MacroWaveB.objects.order_by('-id')[start:(start+pagesize)]
			page1m2 += 1
	elif pageindex=='3':
		start = (page1m2-1)*pagesize
		newsunitsm2 = models.MacroWaveB.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1m2


    #MacroWaveC
	global page1m3
	pagesize = 5 #8
	newsall = models.MacroWaveC.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1m3 = 1
		newsunitsm3 = models.MacroWaveC.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunitsm3 = models.MacroWaveC.objects.order_by('-id')[start:(start+pagesize)]
			page1m3 -= 1
	elif pageindex=='2':
		start = page1m3*pagesize
		if start < datasize:
			newsunitsm3 = models.MacroWavec.objects.order_by('-id')[start:(start+pagesize)]
			page1m3 += 1
	elif pageindex=='3':
		start = (page1m3-1)*pagesize
		newsunitsm3 = models.MacroWaveC.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1m3   
    
	return render(request, "usersmain_common.html", locals())