from django.views.generic import TemplateView, FormView
from sample_forms.forms import QuestionForm, AnswerForm
from django.http import HttpResponseRedirect


class MainView(TemplateView):
    template_name = 'sample_forms/index.html'

    def get(self, request, *args, **kwargs):
        question_form = QuestionForm(self.request.GET or None)
        answer_form = AnswerForm(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context['answer_form'] = answer_form
        context['question_form'] = question_form
        return self.render_to_response(context)


class QuestionFormView(FormView):
    form_class = QuestionForm
    template_name = 'sample_forms/index.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        question_form = self.form_class(request.POST)
        answer_form = AnswerForm()
        if question_form.is_valid():
            question_form.save()
            return self.render_to_response(
                self.get_context_data(
                    sucess=True
                )
            )
        else:
            return self.render_to_response(
                self.get_context_data(
                    question_form=question_form,
                    answer_form=answer_form
                )
            )


class AnswerFormView(FormView):
    form_class = AnswerForm
    template_name = 'sample_forms/index.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        answer_form = self.form_class(request.POST)
        question_form = QuestionForm()
        if answer_form.is_valid():
            answer_form.save()
            return self.render_to_response(
                self.get_context_data(
                    sucess=True
                )
            )
        else:
            return self.render_to_response(
                self.get_context_data(
                    answer_form=answer_form,
                    question_form=question_form
                )
            )
