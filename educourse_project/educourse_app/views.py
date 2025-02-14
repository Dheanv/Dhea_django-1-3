from django.shortcuts import render
from django.http import HttpResponse
from educourse_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict ={'access_records': webpages_list}
    return render(request, 'educourse_app/index.html', context=date_dict)
