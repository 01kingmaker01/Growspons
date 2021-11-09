import re
from .models import Influencer

def password_val(password):
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    c_pass = re.compile(regex)
    matrix = re.search(c_pass, password)

    return matrix

def context_addition(request, content):
    content['influencer']=Influencer.objects.get(influencer_id=request.user.id)
    content['all_influencer']=Influencer.objects.all()[:3]