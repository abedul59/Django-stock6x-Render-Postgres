from django.shortcuts import render
import os

from module import func2x, tseotcid
#from .views_tseotc_id import *
###################################################################
#################################判斷是否為數字的自創函數
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
####################################台股代號

def stock6x(request):  #查詢六大指標，給付費使用者使用

        
    if request.method == "POST":  #假如是以POST方式才處理
        mess0 = request.POST['stockid']  #取得表單輸入內容
        
        if is_number(mess0) == True:  #是數字
            mess = mess0
        else:
            mess = tseotcid.tseotc_dict[mess0]
        
        result2, ProfitN, Profit, b1N, b2N, b3N, b4N, b5N, b6N, b7N, b8N, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b10p, result5, InvTON, InvTO, e1N, e2N, e3N, e4N, e5N, e6N, e7N, e8N, e1, e2, e3, e4, e5, e6, e7, e8, newest_Fin_Q = func2x.stock_Prof2_InvTO5(mess)
        result3, NetIncomeN, NetIncome, c1N, c2N, c3N, c4N, c5N, c6N, c7N, c8N, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, pc9, pc10, pc11, result4, EPSN, EPS, d1N, d2N, d3N, d4N, d5N, d6N, d7N, d8N, d1, d2, d3, d4, d5, d6, d7, d8 = func2x.stock_NetInc3_EPS4(mess)
        result6, CashFlowN, CashFlow, f1N, f2N, f3N, f4N, f5N, f6N, f7N, f8N, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10 = func2x.stock_Cashflow6(mess)
        result1, RevN, Rev, a1N, a2N, a3N, a4N, a5N, a6N, na1, na2, na3, na4, na5, na6, na9, na10, a7N, na7, newest_Rev_month, luX, nluX_MoM = func2x.stock_Rev1(mess)

        average6stock = func2x.stock6score(mess, result1, result2, result3, result4, result5, result6) #取得六大指標平均

        stock_name = func2x.GetStockName(mess)
        
    else:
        mess = "台股代號尚未送出！"
        stock_name = "台股名稱尚未查到！"
        result1 = "營收指標尚未計算出來！"
        result2 = "營益率指標尚未計算出來！"
        result3 = "淨利指標尚未計算出來！"
        result4 = "EPS指標尚未計算出來！"
        result5 = "存貨週轉率指標尚未計算出來！"
        result6 = "現金流量指標尚未計算出來！"
        average6stock = "總平均尚未計算出來！"
        #mess2 = "該表單尚未送出！2"
    return render(request, "stock6x.html", locals())