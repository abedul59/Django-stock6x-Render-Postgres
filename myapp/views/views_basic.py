from django.shortcuts import render
###
def index3(request):  #首頁
    

	return render(request, "index3.html", locals())