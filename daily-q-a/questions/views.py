from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, FormView

from braces.views import LoginRequiredMixin

from .forms import DailyPromptForm
from .models import Question

import time

class TodayView(LoginRequiredMixin, FormView):
    template_name = "questions/today.html"
    form_class = DailyPromptForm
    success_url = reverse_lazy("questions:today_success")


    def get_context_data(self, **kwargs):
        context = super(TodayView, self).get_context_data(**kwargs)

        context["today_date"] = time.strftime("%m/%d")
        context['today_question'] = Question.objects.get(date=context["today_date"])

        return context

    def form_valid(self, form):
        response = form.save(commit=False)
        response.user = self.request.user

        response.question = Question.objects.get(date=time.strftime("%m/%d"))
        response.save()
        return HttpResponseRedirect(self.get_success_url())

class TodaySuccessView(LoginRequiredMixin, TemplateView):
    template_name = "questions/today_success.html"
