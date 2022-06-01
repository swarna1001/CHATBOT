from email import message
from django.shortcuts import render, HttpResponse
from .models import UserInteraction, Degree, Preference, Interest, Experience
from time import time
# Create your views here.

def home(request):
    user_input = request.POST.get('input_test')
    degree_choices = Degree.objects.all()
    interest_choices = Interest.objects.all()
    preference_choices = Preference.objects.all()
    experience_choices = Experience.objects.all()

    show_degrees = 1
    show_interests = 2
    show_experiences = 3
    show_preferences = 4

    if user_input:
        milliseconds = int(time() * 1000)
        user_input_transformed = user_input.lower()
        input_arr = user_input_transformed.split(" ")


        for word in input_arr:
            if (word == "hello"):
                bot_reply = "hello, let's begin then. Please choose your highest degree of education:"
                user_interaction = UserInteraction(message=user_input, reply=bot_reply, associated_choice_field=show_degrees, created_at=milliseconds)
                user_interaction.save()


            elif word == "btech" or word == "bca" or word =="mca" or word == "mba":
                bot_reply_2 = "Please choose your interested area:"
                user_interaction_2 = UserInteraction(message=user_input, reply=bot_reply_2, associated_choice_field=show_interests, user_choice=word, created_at=milliseconds)
                user_interaction_2.save()


            elif word == "it":
                bot_reply = "Please choose your job preference:"
                user_interaction = UserInteraction(message=user_input, reply=bot_reply, associated_choice_field=show_preferences, user_choice=word, created_at=milliseconds)
                user_interaction.save()

            
            elif word == "marketing" or word == "product" or word == "customer" or word == "testing" or word == "support" or word == "science" or word == "devops" or word == "cyber" or word == "development":
                bot_reply = "Please choose your experience level:"
                user_interaction = UserInteraction(message=user_input, reply=bot_reply, associated_choice_field=show_experiences, user_choice=word, created_at=milliseconds)
                user_interaction.save()




            #elif word == "fresher" or word == "0-1" or word == "2-5":
            #    bot_reply = "Please choose your experience level:"
            #    user_interaction = UserInteraction(message=user_input, reply=bot_reply, associated_choice_field=show_preferences, user_choice=word, created_at=milliseconds)
            #    user_interaction.save()

            elif word == "fresher" or word == "0-1" or word == "2-5": 
                #bot_reply = "What was your last assigned job position?"
                #user_interaction = UserInteraction(message=user_input, reply=bot_reply, user_choice=word, created_at=milliseconds)
                #user_interaction.save()
                pass

        

        

                










        print(input_arr)

        user_interactions = UserInteraction.objects.all()
        print(user_interactions)


        for word in input_arr:
            if (word == "thanks"):
                UserInteraction.objects.all().delete()
    
    else:
        user_interactions = UserInteraction.objects.all()

    #user_interactions = UserInteraction.objects.all().order_by('created_at')
    #if len(user_interactions) != 0:
        #print(user_interactions)


    
    context = {
        'user_interactions': user_interactions,
        'degree_choices': degree_choices,
        'preference_choices': preference_choices,
        'interest_choices': interest_choices,
        'experience_choices': experience_choices,
        'show_degrees': show_degrees,
        'show_interests': show_interests,
        'show_experiences': show_experiences,
        'show_preferences': show_preferences

    }

    

    

    

    


        
    return render(request,"home.html", context)
