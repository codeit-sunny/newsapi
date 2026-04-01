from django.shortcuts import render
import requests
API_KEY = 'pub_b62b5c84ef37410e89446128a72fd9dd'

def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')


    if country:
        url = f'https://newsdata.io/api/1/latest?country={country}&apikey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['results']
    elif category:
        url = f'https://newsdata.io/api/1/latest?country=us&category={category}&apikey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['results']
    else:
        url = f'https://newsdata.io/api/1/latest?country=us&category=us&apikey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['results']

    context = {
        'articles':articles
    }
    return render(request, 'home.html', context)


