from django.shortcuts import render
from app.models import *
# Create your views here.
def index(request):
    posts=InfluencerPost.objects.all()[:2]
    content={"posts":posts}
    return render(request,"company/index.html",content)