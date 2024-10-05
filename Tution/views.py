from django.shortcuts import render ,redirect
from . import forms
from django.urls import reverse_lazy
from . import models
from django.http import HttpResponse
from  django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from ClassCtg.models import Category

def home(request,category_slug=None):
    data = models.Tution.objects.all()
    if category_slug is not None:
        category =Category.objects.get(slug=category_slug)
        data=models.Tution.objects.filter(category=category)
    catgories=Category.objects.all()
    return render(request,'home.html',{'data':data,'category':catgories})

def apply_for_tution(request):
    if request.method == 'POST':
        form = forms.ApplicatioForm(request.POST)
        if form.is_valid():
            application =form.save(commit=False)
            application.user=request.user
            application.save()
            # return redirect('application_success')
            return HttpResponse ('application success')
    else:
        form=forms.ApplicatioForm()
    tuitions = models.Tution.objects.all()
    return render(request,'apply_tution.html',{'form':form})

# class BlogDetailsView(DetailView):
#     model=models.Tution
    # template_name='home.html'
    # pk_url_kwarg='id'
    # context_object_name= 'post'

    # def post(self,request,*args,**kargs):
    #     comment_form=form.ComentForm(data=self.request.POST)
    #     post=self.get_object()
    #     if comment_form.is_valid():
    #         new_comment=comment_form.save(commit=False)
    #         new_comment.post=post
    #         new_comment.save()
    #     return self.get(request,*args,**kargs)
    
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     post = self.object #post model er object ekhnae store korlam
    #     comments = post.comments.all()
    #     # if self.request.method == 'POST':
    #         # comment_form=form.ComentForm(data=self.request.POST)
    #         # if comment_form.is_valid():
    #         #     new_comment=comment_form.save(commit=False)
    #         #     new_comment.post=post
    #         #     new_comment.save()
    #     comment_form=form.ComentForm()
    #     context['comments'] = comments
    #     context['comment_form'] = comment_form
    #     return context
