# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 10:00:35 2023

@author: PCUSER
"""


from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.conf import settings
#from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

'''from module import func0
from module import func
from module import func2
from module import func2x
from module import func2t
from module import func3
from module import func3x
from module import func4
from module import func4x
from module import func5
from module import func5x2
from module import func6
from module import func7
from module import func8, func_usbond'''
##################函式位置改寫，一個函式一個檔案，棄用func
#from module_PERseg import Price5yDB, Price5y, PERseg, PERsegPEG, PERsegPEGxDB, PERsegStable, PERsegx, PERsegxDB, NetCapDB, PERseg3
#from module_Kn import KnQuery, Kn8yPrice

#################
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User


from myapp.models import Stock6Sign202404

from django.contrib.auth.decorators import permission_required


from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse





#@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202404(request):

    
    signs = Stock6Sign202404.objects.all().order_by('cStockID')
    return render(request, "stock6listall202404.html", locals())
####################################分隔線#########################################

#@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202404score(request):

    signs = Stock6Sign202404.objects.all().order_by('-cAverageScore')
    return render(request, "stock6listall202404score.html", locals())