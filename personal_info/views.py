from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from personal_info.forms import PersonCreateForm, PersonUpdateForm
from personal_info.models import Person


class PersonList(ListView):
    model = Person  # 从Model取数据
    template_name = 'personal_info/person_list.html'  # 模板，用于渲染

    # 定义一个返回值，定义一个列表，里面是数字 用filter把数字加起来
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context.update({'lst': [1.23, 2.34, 3.45, 4.56]})
        return context


# 这里使用的是View的方法
"""
class PersonCreate(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'personal_info/person_create.html')

    def post(self, request, *args, **kwargs):
        # 验证数据
        data = request.POST  # QueryDict
        form = PersonCreateForm(data=data)
        if form.is_valid():
            # 保存数据
            person = Person(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                gender=form.cleaned_data['gender'],
                id_card=form.cleaned_data['id_card'],
                address=form.cleaned_data['address'],
                temperature=form.cleaned_data['temperature'],

            )
            person.save()
        else:
            raise Exception

        # 跳转
        return HttpResponseRedirect(reverse('personal_info:person_list'))
"""


class PersonCreate(CreateView):
    form_class = PersonCreateForm
    model = Person
    template_name = 'personal_info/person_create.html'
    success_url = reverse_lazy('personal_info:person_list')


class PersonDetail(DetailView):
    model = Person
    template_name = 'personal_info/person_detail.html'


class PersonUpdate(UpdateView):
    model = Person
    form_class = PersonUpdateForm
    template_name = 'personal_info/person_update.html'
    success_url = reverse_lazy('personal_info:person_list')


class PersonDelete(DeleteView):
    model = Person
    template_name = 'personal_info/person_delete.html'
    success_url = reverse_lazy('personal_info:person_list')
