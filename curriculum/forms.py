from django import forms
from .models import Lesson


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('lesson_id', 'name', 'chapter_no', 'video', 'ppt', 'notes')