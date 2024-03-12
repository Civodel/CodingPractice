from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Game
import bs4
import requests




class Login(LoginView):
    template_name = 'base/login.html'
    field = '__all__'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('games')


class LoginCreateView(FormView):
    template_name = 'base/sign.html'
    form_class = UserCreationForm
    redirect_authenticated_user= True
    success_url = reverse_lazy('games')
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(LoginCreateView,self).form_valid(form)

    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('games')

        return super(LoginCreateView,self).get(*args, **kwargs)
# Create your views here.
class GamesList (LoginRequiredMixin,ListView):
    model = Game
    context_object_name ='games'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games']=context['games'].filter(user=self.request.user)
        context['count'] = context['games'].filter(complete=False).count()
        search_values = self.request.GET.get('searh-area') or ''
        if search_values:
            context['games'] = context['games'].filter(title__icontains=search_values)
        context['search_values']=search_values
        return context



class GameDetail (LoginRequiredMixin,DetailView):
    model = Game
    context_object_name = 'game'



class GameCreateView (LoginRequiredMixin,CreateView):
    model = Game
    fields =['title', 'description', 'complete']
    success_url = reverse_lazy('games')

    def image(self,title):
        resultado = requests.get(f'https://www.google.com/search?q={title}&tbm=isch&ved=2ahUKEwjsqLjw2uGEAxWc7skDHYYaBBMQ2-cCegQIABAA')
        soup = bs4.BeautifulSoup(resultado.text, 'html.parser')
        url = soup.select('.DS1iW')[0]['src']
        return url

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.image =self.image(form.instance.title)
        return super(GameCreateView,self).form_valid(form)



class GameEditView (LoginRequiredMixin,UpdateView):
    model = Game
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('games')


class GameDeleteView (LoginRequiredMixin,DeleteView):
    model = Game
    context_object_name='game'
    success_url = reverse_lazy('games')