from django.shortcuts import render

# Create your views here.
def alerts(request):
    return render(request,'alerts.html')

def Badges(request):
    return render(request,'Badges.html')

def buttons(request):
    return render(request,'buttons.html')

def Dropdowns(request):
    return render(request,'Dropdowns.html')

def forms(request):
    return render(request,'forms.html')

def List_group(request):
    return render(request,'List_group.html')