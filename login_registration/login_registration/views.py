from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient

client = MongoClient("mongodb://prasanna1411:mathan100@prasanna-mongodb-shard-00-00.wfmy0.gcp.mongodb.net:27017,prasanna-mongodb-shard-00-01.wfmy0.gcp.mongodb.net:27017,prasanna-mongodb-shard-00-02.wfmy0.gcp.mongodb.net:27017/user-db?ssl=true&replicaSet=atlas-1g0i65-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.get_database('user-db')
cl = db.get_collection('user-details')


def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def home(request):
    return render(request,'homepage.html')

def lg(request):
    if request.method == 'POST': 
        uname = request.POST.get('name')
        pwd = request.POST.get('password')
        validate = cl.find_one({"username": uname, "password": pwd})
        if validate == None:
            return HttpResponse('<h1>Invalid</h1>')
        else:
            return render(request,'homepage.html')

def reg(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        pwd = request.POST.get('password')
        mail = request.POST.get('email')
        doc = {"username" : uname,"password" : pwd,"email" : mail}
        cl.insert_one(doc)
        return render(request,'homepage.html')

def update(request):
    return render(request,'update.html')

def up(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        pwd = request.POST.get('password')
        mail = request.POST.get('email')
        doc = {"age" : age,"password" : pwd,"email" : mail}
        cl.insert_one(doc)
        #update_pwd = {'password' : 'mathan100'}
        #cl.update_one({'username': 'prasanna'}, {'$set' : update_pwd})
        return render(request,'homepage.html')

def delete(request):
    return render(request,'delete.html')

def dele(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        pwd = request.POST.get('password')
        doc = {"username" : uname,"password" : pwd}
        cl.insert_one(doc)
        #cl.delete_one({'username': 'prasanna'})
        return render(request,'homepage.html')