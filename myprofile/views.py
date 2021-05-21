from django.shortcuts import render
from .forms import FeedbackForm

# Create your views here.

def home_view(request):
    context = {}
    return render(request, 'index.html',context)


def feedback_form(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = FeedbackForm()
    context = {
        'form' : form
    }
    return render(request, 'forms.html', context)
