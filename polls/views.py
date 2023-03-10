
from django.http import HttpResponse, HttpResponseRedirect
from . models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.views import generic

'''
def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {
        'question_list' : question_list,
    }
    # output = ','.join([q.question_text for q in question_list])
    return render(request, 'polls/index.html',context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html',{'question':question})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("doesn't exist")
    return render(request, 'polls/detail.html',{'question': question})

'''

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', { 'question':question, 'error_message':"didn't slect a choice" })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# Create your views here.
