from django.shortcuts import render
from urllib.request import build_opener, HTTPCookieProcessor, Request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.views import generic 
from django.views.generic import View
from kiteconnect import KiteConnect
from django.contrib.sessions.backends.db import SessionStore
from urllib.parse import urlencode
import requests
import json
import time
import collections

class work(View):
	
	def login_test(request):
	        x = request.GET.get('status', '')
	        if x == "success":
	            token = request.GET.get('request_token','None')
	            kite = KiteConnect(api_key="XXXXXX")
	            
	            try:
	                user = kite.request_access_token(request_token=token,secret="XXXXXXX")
	                kite.set_access_token(user["access_token"])
	                request.session['token no']=user
	            except:
	                return render(request, 'topper/login.html',{'reason':'Authentication failed'})
	            
	            
	            return render(request, 'topper/index.html',{})
	        else:
	            return render(request, 'topper/login.html')
	def volume(request):
	        check=request.session['token no'] 
	        dic={}
	        script = ['WIPRO','RELIANCE','ZEEL','COALINDIA','KOTAKBANK','TCS','AMBUJACEM','IOC','HCLTECH','INFY','INFRATEL','TATAMOTORS','TECHM','ICICIBANK','ULTRACEMCO','TATAMTRDVR',
	        'ADANIPORTS','INDUSINDBK','MARUTI','TATAPOWER','HINDUNILVR','YESBANK','HINDALCO','DRREDDY','AXISBANK','ASIANPAINT','BPCL','SBIN','BANKBARODA','ACC','BAJAJ-AUTO','NTPC','ITC','VEDL','HDFCBANK','GAIL','BOSCHLTD','HDFC','LT',
	        'AUROPHARMA','M&M','ONGC','TATASTEEL','CIPLA','SUNPHARMA','EICHERMOT','LUPIN','POWERGRID','IBULHSGFIN','BHARTIARTL']
	        url_code='https://api.kite.trade/instruments/NSE/'
	        encoded_args = urlencode([('api_key', 'XXXXXX'), ('access_token', check["access_token"])])
	        for item in script:
	            result = url_code+item+'?'+encoded_args
	            response = requests.get(result).json()
	            check=response['data']['volume']
	            dic[check]=item 
	            time.sleep(0.7)

	        checkhard=collections.OrderedDict(sorted(dic.items(),reverse=True)[:10])

	        return render(request, 'topper/result.html',{'gainer':checkhard,}) 


	def change(request):
	        check=request.session['token no'] 
	        dic={}
	        script = ['WIPRO','RELIANCE','ZEEL','COALINDIA','KOTAKBANK','TCS','AMBUJACEM','IOC','HCLTECH','INFY','INFRATEL','TATAMOTORS','TECHM','ICICIBANK','ULTRACEMCO','TATAMTRDVR',
	        'ADANIPORTS','INDUSINDBK','MARUTI','TATAPOWER','HINDUNILVR','YESBANK','HINDALCO','DRREDDY','AXISBANK','ASIANPAINT','BPCL','SBIN','BANKBARODA','ACC','BAJAJ-AUTO','NTPC','ITC','VEDL','HDFCBANK','GAIL','BOSCHLTD','HDFC','LT',
	        'AUROPHARMA','M&M','ONGC','TATASTEEL','CIPLA','SUNPHARMA','EICHERMOT','LUPIN','POWERGRID','IBULHSGFIN','BHARTIARTL']
	        url_code='https://api.kite.trade/instruments/NSE/'
	        encoded_args = urlencode([('api_key', 'XXXXX'), ('access_token', check["access_token"])])
	        for item in script:
	            result = url_code+item+'?'+encoded_args
	            response = requests.get(result).json()
	            check=response['data']['change_percent']
	            dic[check]=item 
	            time.sleep(0.7)

	        checkhard=collections.OrderedDict(sorted(dic.items(),reverse=True)[:10])

	        return render(request, 'topper/change.html',{'gainer':checkhard,}) 

	def loser(request):
	        check=request.session['token no'] 
	        dic={}
	        script = ['WIPRO','RELIANCE','ZEEL','COALINDIA','KOTAKBANK','TCS','AMBUJACEM','IOC','HCLTECH','INFY','INFRATEL','TATAMOTORS','TECHM','ICICIBANK','ULTRACEMCO','TATAMTRDVR',
	        'ADANIPORTS','INDUSINDBK','MARUTI','TATAPOWER','HINDUNILVR','YESBANK','HINDALCO','DRREDDY','AXISBANK','ASIANPAINT','BPCL','SBIN','BANKBARODA','ACC','BAJAJ-AUTO','NTPC','ITC','VEDL','HDFCBANK','GAIL','BOSCHLTD','HDFC','LT',
	        'AUROPHARMA','M&M','ONGC','TATASTEEL','CIPLA','SUNPHARMA','EICHERMOT','LUPIN','POWERGRID','IBULHSGFIN','BHARTIARTL']
	        url_code='https://api.kite.trade/instruments/NSE/'
	        encoded_args = urlencode([('api_key', 'XXXXX'), ('access_token', check["access_token"])])
	        for item in script:
	            result = url_code+item+'?'+encoded_args
	            response = requests.get(result).json()
	            check=response['data']['change_percent']
	            dic[check]=item 
	            time.sleep(0.7)

	        checkhard=collections.OrderedDict(sorted(dic.items())[:10])

	        return render(request, 'topper/loser.html',{'gainer':checkhard,})               
