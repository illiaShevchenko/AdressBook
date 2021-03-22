from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm
from django.http import HttpResponseNotFound
from django.db.models import Q



def index(request):
    return render(request, 'homepage/index.html', {'title': 'Домашняя страница'})


def list(request):
    persons = Person.objects.order_by('-id')
    search_input = request.GET.get('search-area')
    if search_input:
        persons = Person.objects.filter(Q(surname__icontains=search_input) | 
            Q(name__icontains=search_input) | 
            Q(country__icontains=search_input) | 
            Q(city__icontains=search_input) | 
            Q(street__icontains=search_input) | 
            Q(phone__icontains=search_input) | 
            Q(email__icontains=search_input))
        output_data = {'title': f'Результаты поиска по запросу {search_input}',
             'persons': persons,
             }        
        if not persons:    
            output_data = {'title': 'Результаты поиска',
             'search_input': search_input,
             'result': f'Нет результатов по запросу {search_input}'
             }
    else:
        persons = Person.objects.all()
        search_input = ''
        if persons:
            output_data = {'title': 'Список',
             'persons': persons,
             }
        else:
            output_data = {'title': 'Пустой список',
             'result':'Пока список пуст, нажмите "Добавление", чтобы заполнить!'
             }
    return render(request, 'homepage/list.html', output_data)


def add(request):
    error = ''
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('test')
            return redirect('list')
        else:
            print(form.errors)
            error = 'Ошибка ввода, проверьте данные.'
    form = PersonForm()
    context = {
        'form': form,
        'title': 'Добавление',
        'error': error
    }
    return render(request, 'homepage/main_form.html', context)


def edit(request,id):
    try:
        person = Person.objects.get(id=id)
        error = ''
        if request.method == "POST":
            form = PersonForm(request.POST, request.FILES, instance = person)
            if form.is_valid():
                person.surname = request.POST.get("surname")
                person.name = request.POST.get("name")
                person.phone = request.POST.get("phone")
                person.email = request.POST.get("email")
                person.image = request.FILES.get("image")
                person.save()
                return redirect('list')
            else:
                error = 'Ошибка ввода, проверьте данные.'
        form = PersonForm(instance = person)
        context = {
            'form': form,
            'title': 'Редактирование',
            'error': error
         }
        return render(request, 'homepage/main_form.html', context)
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return redirect('list')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
