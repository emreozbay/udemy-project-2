from django.shortcuts import render
from . import forms
from basicapp.forms import NewUserForm


# Create your views here.

def index(request):
    context_dict = {'text':'hello world','number':100}
    return render(request,'basicapp/index.html',context_dict)

def other(request):
    return render(request,'basicapp/other.html')

def relative(request):
    return render(request,'basicapp/relative_url_templates.html')









def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("validation success!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])
    return render(request,'basicapp/form_page.html',{'form':form})

def users(request):
    form = NewUserForm()
    if request.method =="POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('ERROR FORM INVALID')

    return render(request,'basicapp/users.html',{'form':form})

