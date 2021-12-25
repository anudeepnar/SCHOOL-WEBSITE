from os import spawnv
from django.db import models
from django.db.models.aggregates import Max
from django.db.models.fields.related import ForeignKey
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

# Create your models here.

class Standard(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, null=True)
    image = models.ImageField(default='default.jpg', upload_to = 'standards/', blank=True)
    description = models.TextField(max_length=200, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Standard, self).save(*args, **kwargs)

        # img = Image.open(self.image.path)

        # if img.height > 300 or img.width >300:
        #     output_size =(300, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)

#related_name='subjects' is used to access Subject objects from Standard Model. i.e. selecting each subjects present in standards 
class Subject(models.Model):
    subject_id = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, blank=True)
    standard = models.ForeignKey(Standard, on_delete = models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to= 'subjects/', blank=True)
    description = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject_id)
        super().save(*args, **kwargs)

class Lesson(models.Model):
    lesson_id = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, blank=True)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="lessons")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    chapter_no = models.PositiveSmallIntegerField(verbose_name="chapter_no.")
    video = models.FileField(upload_to='lessons/', verbose_name="Video", blank=True, null=True)
    ppt = models.FileField(upload_to='ppt/', verbose_name="Presentation", blank=True, default='ppt')
    notes = models.FileField(upload_to='notes/', verbose_name="Notes", blank=True)

    class Meta:
        ordering = ['chapter_no']

    def __str__(self):
        return self.name

# <!-- Bad -->
# <a href="/language/category/product/{{product.pk}}">Link</a>

# <!-- Good -->
# <a href="{{product.get_absolute_url}}">Link</a>

    def get_absolute_url(self):
        return reverse('curriculum:lesson_detail', kwargs={'slug': self.slug, 'subject': self.subject.slug, 'standard': self.standard.slug})
      

    def save(self, *args, **kwargs):
        self.slug = slugify(self.lesson_id)
        super().save(*args, **kwargs)

        