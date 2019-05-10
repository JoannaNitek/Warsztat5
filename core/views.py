from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, FormView
from core.forms import PhotoForm
from core.models import Photo


class IndexView(View):
    def get(self, request):
        photos = Photo.objects.all()
        return render(request, 'index.html', {'photos': photos})

class AddPhotoView(FormView):
    template_name = 'add_photo.html'
    success_url = '/'
    form_class = PhotoForm
    def form_valid(self, form):
        form.save()
        return super(AddPhotoView, self).form_valid(form)