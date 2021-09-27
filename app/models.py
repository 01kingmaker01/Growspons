from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields
# In user Email id and User are same

fields_list=sorted({
    ("Commentary","Commentary"),("ProductReview","ProductReview"),("Comedy","Comedy"),("Reaction","Reaction"),("Q&A","Q&A"),("Interview","Interview"),("Educational","Educational"),("Music","Music"),("Gaming","Gaming"),("Sport","Sport"),("Food","Food"),("Fashion","Fashion")
})
class Sponsor(models.Model):
    sponsor_id=models.OneToOneField(User,on_delete=models.CASCADE)
    field=models.CharField(max_length=50,choices=fields_list)
    profile_img=models.ImageField(upload_to="media/profileImg/sponsor")
    pancard=models.CharField(max_length=12,null=True)
    cin_no=models.CharField(max_length=21,null=True)
    mode_of_transation=models.CharField(max_length=25,choices=sorted({
        ("1","NetBanking"),("2","Card"),("3","UPI"),("4","Other")
    }))
    bank_name=models.CharField(max_length=25,null=True)
    IFSC_code=models.CharField(max_length=15,null=True)
    account_no=models.CharField(max_length=15,null=True)
    phone_no=models.CharField(max_length=13)
    address=models.TextField(max_length=300)
    website_link=models.URLField(null=True)
    facebook=models.URLField(null=True)
    instagram=models.URLField(null=True)
    twitter=models.URLField(null=True)
    other_link=models.URLField(null=True)
    is_verified=models.BooleanField(null=True)

class Influencer(models.Model):
    influencer_id=models.OneToOneField(User,on_delete=models.CASCADE)
    field=models.CharField(max_length=50,choices=fields_list)
    profileImg=models.ImageField(upload_to="media/profileImg/influencer")
    pancard=models.CharField(max_length=12,null=True)
    mode_of_transation=models.CharField(max_length=25,choices=sorted({
        ("1","NetBanking"),("2","Card"),("3","UPI"),("4","Other")
    }))
    bank_name=models.CharField(max_length=25,null=True)
    IFSC_code=models.CharField(max_length=15,null=True)
    account_no=models.CharField(max_length=15,null=True)
    phone_no=models.CharField(max_length=13)
    address=models.TextField(max_length=300)
    website_link=models.URLField(null=True)
    facebook=models.URLField(null=True)
    instagram_name=models.CharField(max_length=30)
    instagram=models.URLField(null=True)
    follower=models.IntegerField()
    twitter=models.URLField(null=True)
    youtube_name=models.CharField(max_length=30)
    youtube=models.URLField(null=True)
    subscriber=models.IntegerField()
    other_link=models.URLField(null=True)
    is_verified=models.BooleanField(null=True)

class InfluencerPost(models.Model):
    influencer=models.ForeignKey(Influencer,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    discreption=models.TextField(max_length=500,null=True)
    field=models.CharField(max_length=50,choices=fields_list)
    post_img=models.ImageField(upload_to="media/profileImg/influencer")

class Posted(models.Model):
    influencer=models.ForeignKey(Influencer,on_delete=models.CASCADE)
    content_link=models.URLField()
    is_accepted=models.BooleanField()
    comment=models.CharField(max_length=300)

class Sponsored(models.Model):
    influencer=models.ForeignKey(Influencer,on_delete=models.CASCADE)
    sponsor=models.ForeignKey(Sponsor,on_delete=models.CASCADE)
    posted=models.ForeignKey(Posted,on_delete=models.CASCADE)
    mode_of_sponsorship=models.CharField(max_length=50,choices=sorted({

    }))
    transation_id=models.CharField(max_length=50)
    amount=models.IntegerField(null=True)


