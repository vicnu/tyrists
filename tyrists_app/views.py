from django.shortcuts import render,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .filters import TyrsFilter
from .models import Tyrs

# Create your views here.
def page_not_found(request,exception):
    context =None
    if "tried" in str(exception):

        context={"exception":"Page not found"}
    else:
            context = {"exception": exception}
            print(exception)
    return render(request,'blog_app/404.html',context)


def error403(request, exception):
    context = {"exception": exception}
    return render(request,'blog_app/404.html', context)


def error500(request):
    context = {}
    return render(request,'blog_app/500.html', context)

def index(request):
    tyrss = Tyrs.objects.all()
    context={"title":"Главная страница с",
             "tyrss":tyrss
    }
    return render(request,"tyrists_app/index.html",context)



def dabout(request):
    return render(request,"tyrists_app/about.html")
def contacts(request):
    return render(request,"tyrists_app/contacts.html")
def faq(request):
    return render(request,"tyrists_app/faq.html")

# class TyrsListView(ListView):
#     model=Tyrs
#     filter_class = TyrsFilter
#     template_name = "tyrists_app/index.html"
#     context_object_name = "tyrss"
#     paginate_by = 5

class TyrsDetailView(DetailView):
    model=Tyrs


# #проверка от класса на залогиненого пользователя
class TyrsCreateView(LoginRequiredMixin,CreateView):
    model=Tyrs
    fields=['TyrName','TyrType','TyrPrice',"TyrPoint"]


    def form_valid(self, form):
        form.instance.Author=self.request.user
        return super().form_valid(form)

class TyrsUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Tyrs
    fields=['TyrName','TyrType','TyrPrice','image']

    def form_valid(self, form):
        form.instance.Author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        tyr=self.get_object()
        return self.request.user==tyr.Author
#
class TyrsDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Tyrs
    success_url = "/"

    def test_func(self):
        tyr=self.get_object()
        return self.request.user==tyr.Author


class FilterTyrsListView(ListView):
    filter_class = None

    def get_queryset(self):
        qs=super().get_queryset()
        req=self.request.GET
        self.filtered=self.filter_class(req,qs)
        return self.filtered.qs.distinct()

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["filter"]=self.filtered
        return context

class TyrsListView(FilterTyrsListView):

    model=Tyrs
    filter_class = TyrsFilter
    template_name = "tyrists_app/index.html"
    context_object_name = "tyrss"
    paginate_by = 5