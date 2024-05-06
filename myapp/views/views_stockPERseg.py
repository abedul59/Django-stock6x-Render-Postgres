from module_PERseg import PERsegx

from django.shortcuts import render
from module import func2, tseotcid
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

def stockPERsegx(request):   #查詢本益比區間，給付費使用者使用。
    if request.method == "POST":  #假如是以POST方式才處理
        #mess = request.POST['stockid']  #取得表單輸入內容
        mess0 = request.POST['stockid']  #取得表單輸入內容
        
        if is_number(mess0) == True:  #是數字
            mess = mess0
        else:
            mess = tseotcid.tseotc_dict[mess0]

        mess2 = request.POST['monthid']

        #import datetime
        #wholetime = str(datetime.datetime.now()) 
        #realtime = wholetime[:16]  #取得獲取資料時間
        #取得股票名稱
        #stock_description, latest_trade_date, open, close, high, low, thisYearGain, newest_Rev_month, stock_id_name, yahoo_latest_tradePrice, stock_name = func2.stockdef(mess)
        stock_name = func2.GetStockName(mess)

        H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(mess, mess2)
        #H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(mess, mess2)

        percent30down_PER_H = round(PER_H*0.7,2)
        percent30down_PER_L = round(PER_L*0.7,2)
        
        
        Predict_high_price_30percentDown = round(Predict_high_price*0.7,2)
        Predict_low_price_30percentDown = round(Predict_low_price*0.7,2)

        
        up_profit2 = round((Predict_high_price_30percentDown - yahoo_latest_tradePrice)/yahoo_latest_tradePrice,2)
        down_loss2 = round((Predict_low_price_30percentDown - yahoo_latest_tradePrice)/yahoo_latest_tradePrice,2)
        

        from decimal import Decimal, ROUND_HALF_UP
        New_up_profit2 = str((Decimal(up_profit2).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
        New_down_loss2 = str((Decimal(down_loss2).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'


        
        
        New_risk_reward = round(abs(up_profit2/down_loss2),2)
        
        #New_up_profit_30percentDown = New_up_profit*0.7
        #New_down_loss_30percentDown = New_down_loss*0.7

        #H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =func3x.PERseg(mess, mess2)
        #, pNet1, pNet2, pNet3, pNet4, pNet4Average
        #, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average
        
        #H0為今年最高價，Satisf算出距離多少
        Satisf = str(round((float(H0) - Predict_high_price)*100/Predict_high_price,2)) + '%'  #今年高點是否出現？滿足比率
        if (float(H0) > Predict_high_price*0.95):
            highif = 'Yes'
        else:
            highif = 'No'

        #try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #seg = models.StockPERseg.objects.get(cStockID=mess)

        #except:  #針對沒有的股票，抓取資料存入資料庫
            #seg = models.StockPERseg.objects.create(cStockID=mess, cStockName=stock_name, cPredict_high_price=Predict_high_price, cPredict_low_price=Predict_low_price, cLatest_price=yahoo_latest_tradePrice, cNew_up_profit=New_up_profit, cNew_down_loss=New_down_loss, cRisk_reward=risk_reward, pubtime=realtime)
            #seg = models.StockPERseg.objects.create(cStockID=mess, cStockName=stock_name, cH1=H1, cL1=L1, cH2=H2, cL2=L2, cH3=H3, cL3=L3, cH4=H4, cL4=L4, cH5=H5, cL5=L5, cEPS1=eps1, cEPS2=eps2, cEPS3=eps3, cEPS4=eps4, cEPS5=eps5, cPER_H1=PER_H1, cPER_L1=PER_L1, cPER_H2=PER_H2, cPER_L2=PER_L2, cPER_H3=PER_H3, cPER_L3=PER_L3, cPER_H4=PER_H4, cPER_L4=PER_L4, cPER_H5=PER_H5, cPER_L5=PER_L5, cPER_H_average=PER_H_average, cPER_L_average=PER_L_average, cPER_H=PER_H, cPER_L=PER_L, cYoY6Average=rYoY6Average, cRevYoY=RevYoY, cNet1=Net1, cNet2=Net2, cNet3=Net3, cNet4=Net4, cNet4Average=Net4Average, cRev_Predict=Rev_Predict, cNet_Predict=Net_Predict, cCapital_stock=capital_stock, cPredict_EPS=Predict_EPS, cPredict_high_price=Predict_high_price, cPredict_low_price=Predict_low_price, cLatest_price=yahoo_latest_tradePrice, cNew_up_profit=New_up_profit, cNew_down_loss=New_down_loss, cRisk_reward=risk_reward, pubtime=realtime)
            #seg.save()

        
        #mess2 = request.POST['xdays']  #取得表單輸入內容
    else:
        mess = "台股代號尚未送出！"
        mess2 = "營收月份代號尚未送出！"

        #mess2 = "該表單尚未送出！2"
    return render(request, "stockPERsegx.html", locals())


