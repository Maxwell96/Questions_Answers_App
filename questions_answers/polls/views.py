from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from django.urls import reverse

# Get questions and display them
def index(request):

    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_questions_list}

    return render(request, 'polls/index.html', context)

# Get a specific question and display it 
def detail(request, pk):
    question = Question.objects.get(id=pk)
    context = {'question': question}

    return render(request, 'polls/detail.html', context)

# Get question and display results
def results(request, pk):
    question = get_object_or_404(Question, id=pk)

    context = {'question': question}
    return render(request, 'polls/results.html', context)

# Vote for a question choice 
def vote(request, pk):
    question = get_object_or_404(Question, id=pk)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question for voting from.
        return render(request, 'polls/detail.html', {
            'question':question, 'error_message':"You didn't select any choice."
            
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with POST data.
        # This prevents data from being posted twice if a use hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.pk,)))

