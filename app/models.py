from django.db import models
from django.contrib.auth.models import User

# In user Email id and User are same

fields_list=sorted({
    ("Commentary","Commentary"),("ProductReview","ProductReview"),("Comedy","Comedy"),("Reaction","Reaction"),("Q&A","Q&A"),("Interview","Interview"),("Educational","Educational"),("Music","Music"),("Gaming","Gaming"),("Sport","Sport"),("Food","Food"),("Fashion","Fashion"),("Travel","Travel")
})
class Sponsor(models.Model):
    sponsor_id=models.OneToOneField(User,on_delete=models.CASCADE)
    field=models.CharField(max_length=50,choices=fields_list)
    profile_img=models.ImageField(upload_to="media/profileImg/sponsor")
    pancard=models.CharField(max_length=12,null=True)
    cin_no=models.CharField(max_length=21,null=True)
    mode_of_transaction=models.CharField(max_length=25,choices=sorted({
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

    def __str__(self):
        return str(self.sponsor_id.username)

class Influencer(models.Model):
    influencer_id=models.OneToOneField(User,on_delete=models.CASCADE)
    field=models.CharField(max_length=50,choices=fields_list)
    profileImg=models.ImageField(upload_to="media/profileImg/influencer")
    dob = models.DateField()
    phone_no=models.CharField(max_length=13)
    bio=models.TextField(max_length=300)
    location=models.CharField(max_length=200)
    
    pancard=models.CharField(max_length=12,null=True, default='NA')
    mode_of_transaction=models.CharField(max_length=25, default='NA', choices=sorted({
        ("1","NetBanking"),("2","Card"),("3","UPI"),("4","Other")
    }))
    bank_name=models.CharField(max_length=25,null=True, default='NA')
    IFSC_code=models.CharField(max_length=15,null=True, default='NA')
    account_no=models.CharField(max_length=15,null=True, default='NA')

    facebook=models.URLField(null=True)
    instagram=models.URLField(null=True)
    follower=models.IntegerField()
    twitter=models.URLField(null=True)
    youtube=models.URLField(null=True)
    subscriber=models.IntegerField()
    other_link=models.URLField(null=True)
    is_verified=models.BooleanField(null=True, default=False)

    def __str__(self):
        return str(self.influencer_id.username)


class InfluencerPost(models.Model):
    influencer=models.ForeignKey(Influencer,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    description=models.TextField(max_length=500,null=True)
    field=models.CharField(max_length=50,choices=fields_list)
    post_img=models.ImageField(upload_to="media/profileImg/influencer")

    def __str__(self):
        return str(self.title)+","+str(self.influencer)

class Content(models.Model):
    influencer=models.ForeignKey(Influencer,on_delete=models.CASCADE)
    content_link=models.URLField()
    is_accepted=models.BooleanField()
    comment=models.CharField(max_length=300)
    def __str__(self):
        return str(self.influencer.influencer_id.username)

class Sponsored(models.Model):
    influencer=models.ForeignKey(Influencer,on_delete=models.CASCADE)
    sponsor=models.ForeignKey(Sponsor,on_delete=models.CASCADE)
    posted=models.ForeignKey(Content,on_delete=models.CASCADE)
    mode_of_sponsorship=models.CharField(max_length=50,choices=sorted({

    }))
    transaction_id=models.CharField(max_length=50)
    amount=models.IntegerField(null=True)

