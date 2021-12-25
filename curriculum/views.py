from django.db.models.base import Model
from django.shortcuts import redirect, render
from django.views.generic import ListView , DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from curriculum.models import Standard, Subject, Lesson
from .forms import LessonForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def home(request):
    return render(request, 'curriculum/home.html')

class StandardListView(ListView):
    context_object_name = 'standards'
    Model = Standard
    template_name = 'curriculum/standard_list_view.html'
    
    def get_queryset(self):
            return Standard.objects.all()

class SubjectListView(DetailView):
    context_object_name = 'standards'
    Model = Standard
    template_name = 'curriculum/subject_list_view.html'

    def get_queryset(self):
            return Standard.objects.all()

class LessonListView(DetailView):
    context_object_name = 'subjects'
    Model = Subject
    template_name = 'curriculum/lesson_list_view.html'

    def get_queryset(self):
        return Subject.objects.all()

class LessonCreateView(CreateView):
    form_class = LessonForm
    context_object_name = 'subject'
    Model = Subject
    template_name = 'curriculum/lesson_create_view.html'

    def get_queryset(self):
        return Subject.objects.all()

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('curriculum:lesson', kwargs={'standard':standard.slug, 'slug':self.object.slug })  

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.standard = self.object.standard
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

class LessonDetailView(DetailView):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'curriculum/lesson_detail_view.html'

    def get_queryset(self):
        return Lesson.objects.all()

class LessonUpdateView(UpdateView):
    fields = ('name', 'chapter_no', 'video', 'ppt', 'notes')
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'curriculum/lesson_update_view.html'


class LessonDeleteView(DeleteView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = 'curriculum/lesson_delete_view.html'

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        subject = self.object.subject
        return reverse('curriculum:lesson', kwargs={'standard':standard.slug,'slug':subject.slug

        } )

def contactus(request):
    return render(request, 'curriculum/contactus.html')