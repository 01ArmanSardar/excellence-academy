from django.shortcuts import render
from Tution import models
from ClassCtg.models import Category
def home(request,category_slug=None):
    data = models.Tution.objects.all()
    if category_slug is not None:
        category =Category.objects.get(slug=category_slug)
        data=models.Tution.objects.filter(category=category)
    catgories=Category.objects.all()
    return render(request,'home.html',{'data':data,'category':catgories})