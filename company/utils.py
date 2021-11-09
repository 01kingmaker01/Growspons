from app.models import Sponsor

def context_addition(request, content):
    content['sponsor']=Sponsor.objects.get(sponsor_id=request.user.id)