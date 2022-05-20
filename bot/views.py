from django.shortcuts import render, HttpResponse
#from home import models

# Create your views here.

def home(request):
    user_inputs = []
    text = request.POST.get('input_test')
    print(text)
    
    if (user_inputs.__contains__(text)):
        return
    else:
        user_inputs.append(text)

    print("user_inputs : ", user_inputs)


        
    return render(request,"home.html", {'text': text})
