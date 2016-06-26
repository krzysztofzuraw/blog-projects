from django.forms import ModelForm
from sample_forms.models import Question, Answer


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'date_questioned']


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'date_answered']
        
