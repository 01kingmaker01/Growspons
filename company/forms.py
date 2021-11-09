from django.db.models import fields
from app.models import Sponsor
from django.forms import ModelForm

class SponserForm(ModelForm):
    class Meta:
        model=Sponsor
        # fields=["sponsor_id","field","profile_img","pancard","cin_no","mode_of_transaction","phone_no","address","website_link","facebook","instagram","twitter","other_link"]
        fields=["sponsor_id","field","pancard","cin_no","mode_of_transaction","phone_no","address","website_link","facebook","instagram","twitter","other_link"]