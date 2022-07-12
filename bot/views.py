from email import message
from unittest import result
from django.shortcuts import render, HttpResponse
from .models import UserInteraction, Degree, Preference, Interest, Experience
from time import time

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
            if word == "hello" or word == "hey":
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

            elif word == "marketing" or word == "product" or word == "customer" or word == "testing" or word == "support" or word == "science" or word == "devops" or word == "cyber" or word == "development" or word == "data":
                bot_reply = "Please choose your experience level:"
                user_interaction = UserInteraction(message=user_input, reply=bot_reply, associated_choice_field=show_experiences, user_choice=word, created_at=milliseconds)
                user_interaction.save()

            elif word == "fresher" or word == "1-2" or word == "2-5": 
                interactions = UserInteraction.objects.all()
                if UserInteraction.objects.filter(message = "fresher").exists():
                    continue
                else:

                    bot_reply = "Alright, that is all the information that we require at this moment. Please hold on for a moment!"
                    user_interaction = UserInteraction(message=user_input, reply=bot_reply, user_choice=word, created_at=milliseconds)
                    user_interaction.save()

                    result = calculate_result()

                    if result:
                        bot_reply = "You have been assigned {} domain. Congratulations!".format(result)
                        user_interaction = UserInteraction(message='last', reply=bot_reply, user_choice=result, created_at=milliseconds, is_last=True)
                        user_interaction.save()
                    
                    else:
                        bot_reply = "Sorry, we are not able to assign you to your requested Domain!"
                        user_interaction = UserInteraction(message='last', reply=bot_reply, user_choice=result, created_at=milliseconds, is_last=True)
                        user_interaction.save()

        user_interactions = UserInteraction.objects.all()

        for word in input_arr:
            if word == "thanks" or word == "bye":
                UserInteraction.objects.all().delete()
    
    else:
        user_interactions = UserInteraction.objects.all()

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


def calculate_result():

    if UserInteraction.objects.filter(message = "mba").exists() and UserInteraction.objects.filter(message="marketing").exists():
        return "marketing"

    elif UserInteraction.objects.filter(message="btech").exists() and UserInteraction.objects.filter(message="it").exists() and UserInteraction.objects.filter(message="development").exists():
        return "Development"

    elif UserInteraction.objects.filter(message="btech").exists() and UserInteraction.objects.filter(message="it").exists() and UserInteraction.objects.filter(message="cyber security").exists():
        return "Cyber Security"

    elif UserInteraction.objects.filter(message="btech").exists() and UserInteraction.objects.filter(message="it").exists() and UserInteraction.objects.filter(message="devops").exists():
        return "DevOps"

    elif UserInteraction.objects.filter(message="btech").exists() and UserInteraction.objects.filter(message="it").exists() and UserInteraction.objects.filter(message="support").exists():
        return "Support"

    elif UserInteraction.objects.filter(message="btech").exists() and UserInteraction.objects.filter(message="it").exists() and UserInteraction.objects.filter(message="testing").exists():
        return "Testing"

    elif (UserInteraction.objects.filter(message="bca").exists() or UserInteraction.objects.filter(message="mca").exists()) and UserInteraction.objects.filter(message="it").exists() and UserInteraction.objects.filter(message="development").exists() and (UserInteraction.objects.filter(message="1-2").exists() or UserInteraction.objects.filter(message="2-5").exists()) :
        return "Development"

    elif (UserInteraction.objects.filter(message="btech").exists() or UserInteraction.objects.filter(message="bca").exists() or UserInteraction.objects.filter(message="mca").exists()) and UserInteraction.objects.filter(message="product management").exists() and (UserInteraction.objects.filter(message="1-2").exists() or UserInteraction.objects.filter(message="2-5").exists()) :
        return "Product Management"

    elif (UserInteraction.objects.filter(message="mba").exists() or UserInteraction.objects.filter(message="bca").exists() or UserInteraction.objects.filter(message="mca").exists()) and UserInteraction.objects.filter(message="product management").exists() and (UserInteraction.objects.filter(message="1-2").exists() or UserInteraction.objects.filter(message="2-5").exists()) :
        return "Product Management"

    else:
        return 
