from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app.models import *
# Create your views here.
from app.decorators import allowed_users

group_cmp = 'Company'

@login_required(login_url='login')
@allowed_users(allowed_roles=[group_cmp])
def index(request):
    posts=InfluencerPost.objects.all()
    contents=Content.objects.filter(is_accepted=False)
    
    content={"posts":posts,"contents":contents}
    return render(request,"company/index.html",content)

def posted(request,id):
    post=InfluencerPost.objects.get(id=id)
    content={"post":post}
    return render(request,"company/posted.html",content)