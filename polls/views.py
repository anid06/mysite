from django.shortcuts import render, get_object_or_404, redirect
from django.utils.datastructures import MultiValueDictKeyError

from .models import Question, Choice

#1. widok wszystkich opublikowanych pytań
def index(request):
    questions = Question.objects.all()
    title = 'Lista wszystkich pytań'

    context = {
        'questions': questions,
        'title': title,
    }

    return render(request,'polls/index.html', context)

#2. widok szczegółowy danego pytania
def detail(request, question_id):
    #question = Question.objects.get(id = question_id)
    question = get_object_or_404(Question, id = question_id)
    title = f'Pytanie: {question.question_text}'

    context = {
        'question': question,
        'title': title,
    }

    return render(request,'polls/detail.html', context)


#3. widok, który reaguje na zagłosowanie przez usera
def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    # if request.method == "POST": # usuwamy gdyż poniżej implementujemy, że niechciane wartości będą puste
        # choice_form = request.POST['choice']
    choice_form = request.POST.get('choice')
    #jeśli nie ma przyjmie wartosc NaN czyli Null

        # try:
        #     choice_form = request.POST['choice']
        # except MultiValueDictKeyError:
        #     return redirect('polls:detail', question_id)

    try:
        selected_choice = question.choice_set.get(id=choice_form)
    except Choice.DoesNotExist:
        return redirect('polls:detail', question_id)

    selected_choice.votes += 1
    selected_choice.save()

    return redirect('polls:results', question_id)

#4. widok z wynikami dla danego pytania
def results(request, question_id):
    #question = Question.objects.get(id = question_id)
    question = get_object_or_404(Question, id = question_id)
    title = f'Wyniki: {question.question_text}'

    context = {
        'question': question,
        'title': title,
    }

    return render(request,'polls/results.html', context)




