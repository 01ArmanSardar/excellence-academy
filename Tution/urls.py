from django.urls import path
from .import views
urlpatterns = [
#    path('details/<slug:slug>',views.BlogDetailsView.as_view(),name='tution')
path('category/<slug:category_slug>',views.home,name='category_wise_post'),
path('apply/',views.apply_for_tution,name='apply_tution'),

]