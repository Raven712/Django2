from django.shortcuts import render
import random

# Create your views here.
def index(request):
    names = ['아이브', '뉴진스', '르세라핌']
    name = random.choice(names)
    context = {
        'name' : name,
        'img' : 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA0MTRfNjAg%2FMDAxNjQ5OTQ3OTM5OTY0.FGGct8U9tXMRFkFTQQKPRQiLJXrDz_OU9LbzXggItHgg.WTioKCkLQn20vJjIlwStY2Nu9gniwDT4fObApeG9Szog.JPEG.yelim369369%2Foutput_2294817902.jpg&type=sc960_832',
    }
    return render(request, 'index.html', context)

def welcome(request, name):
    #위의 name은 urls.py에서 경로지정을 할때 꺾쇠괄호에 들어가는 name임
    context = {
        'name' : name,
        'greetings' : ['안녕하세요', '안녕', '하이'],
    }
    return render(request, 'welcome.html', context)