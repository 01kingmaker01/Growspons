from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app.models import *
# Create your views here.
from app.decorators import allowed_users

group_cmp = 'Company'

@login_required(login_url='login')
@allowed_users(allowed_roles=[group_cmp])
def index(request):
    posts=InfluencerPost.objects.all()[:2]
    content={"posts":posts}
    return render(request,"company/index.html",content)