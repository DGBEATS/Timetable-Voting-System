from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Option

# Render the Questions
def Home(request):
    recent_question = Question.objects.order_by('publish_date')[:5] # order by earliest question # specify the number of the most recent questions to see
    context = {'recent_question': recent_question}
    return render(request, 'votes/Home.html', context)

# Render the question choices
def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    context = {'question': question, 'error_message': "You have not selected an option"}

    if request.method == 'POST':
        option_id = request.POST.get('option')
        if option_id:
            try:
                selected_option = question.option_set.get(pk=option_id)
            except Option.DoesNotExist:
                # Handle the case where the selected option does not exist
                pass
            else:
                selected_option.votes += 1
                selected_option.save()
                return HttpResponseRedirect(reverse('votes:results', args=(question_id,))) # moves the user to the results page
        else:
            # Handle the case where no option is selected
            return render(request, 'votes/detail.html', context)
    
    return render(request, 'votes/detail.html', context)






    # try:
    #     selected_option = obj.option_set.get(pk = request.POST['option'])
    # except (KeyError, Option.DoesNotExist):
    #     return render(request, 'votes/detail.html', context)
    # else:
    #     selected_option.votes += 1
    #     selected_option.save()
    #     return HttpResponseRedirect(reverse('votes:results', args=(question_id,))) # prevents data from being posted twice if a user goes back



# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk = question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     context = {'question': question}
#     return render(request, 'votes/detail.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    context = {'question': question}
    return render(request, 'votes/detail.html', context)


# Render the question results

def results(request, question_id):
    obj = get_object_or_404(Question, pk = question_id)
    context = {'obj': obj}
    return render(request, 'votes/results.html', context)