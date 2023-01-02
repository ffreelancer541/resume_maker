from django.db import models
from .manager import UserManager
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser , PermissionsMixin
)
# Create your models here.

class User(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    tc = models.BooleanField(default=False)
    phone=models.IntegerField(default=True ,null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','phone' , 'tc']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin




class Resume(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_resume')
    page=models.TextField()

    def __str__(self) :
        return self.user.email
        
class Cover_letter(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_coverLetter')
    page=models.TextField()

    def __str__(self) :
        return self.user.email
        
class CV(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_CV')
    page=models.TextField()

    def __str__(self) :
        return self.user.email


status_choices=(
    ('basic' , 'basic'),
    ('premium' , 'premium')
    )

class ResumeTemplates(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    page=models.TextField(null=True , default=True)
    image=models.ImageField(upload_to='images/')
    status=models.CharField(choices=status_choices , max_length=255)

    def __str__(self):
        return self.name


    


# class Skills(models.Model):
#     user=models.ManyToManyField(User )
#     skill=models.CharField(max_length=255)

#     def __str__(self):
#         return self.skill


# class Achievments(models.Model):
#     user=models.ManyToManyField(User)
#     achievment=models.CharField(max_length=1000)
#     from_date=models.DateField()
#     to_date=models.DateField()
#     description=models.TextField()

#     def __str__(self):
#         return self.achievment


# class Certificates(models.Model):
#     user=models.ManyToManyField(User)
#     certificate=models.CharField(max_length=1000)
#     from_date=models.DateField()
#     to_date=models.DateField()
#     description=models.TextField(null=True)

#     def __str__(self):
#         return self.certificate


# class Work_Experience(models.Model):
#     user=models.ManyToManyField(User )
#     title=models.CharField(max_length=255)
#     company=models.CharField(max_length=255)
#     from_date=models.DateField()
#     to_date=models.DateField()
#     address=models.CharField(max_length=600)
#     description=models.TextField(null=True)
#     task=models.CharField(max_length=255)
#     contact_person=models.CharField(max_length=255)
#     contact_info=models.CharField(max_length=255)

#     def __str__(self):
#         return self.title

    
# class Technical_Skills(models.Model):
#     user=models.ManyToManyField(User )
#     group_name=models.CharField(max_length=255)
#     technical_skills=models.CharField(max_length=250)

#     def __str__(self):
#         return self.technical_skills


# class Teaching_experince(models.Model):
#     user=models.ManyToManyField(User )
#     title=models.CharField(max_length=255)
#     company=models.CharField(max_length=255)
#     from_date=models.DateField()
#     to_date=models.DateField()
#     address=models.CharField(max_length=600)
#     description=models.TextField(null=True)
#     task=models.CharField(max_length=255)
#     contact_person=models.CharField(max_length=255)
#     contact_info=models.CharField(max_length=255)

#     def __str__(self):
#         return self.title



# class Soft_Skills(models.Model):
#     user=models.ManyToManyField(User )
#     skill=models.CharField(max_length=255)

#     def __str__(self):
#         return self.skill


# class Reference(models.Model):
#     user=models.ManyToManyField(User )
#     name=models.CharField(max_length=255)
#     reference=models.CharField(max_length=255)
#     contact_person=models.CharField(max_length=255)
#     contact_info=models.CharField(max_length=255)

#     def __str__(self):
#         return self.name



# class Publications(models.Model):
#     user=models.ManyToManyField(User )
#     type=models.CharField(max_length=255)
#     title=models.CharField(max_length=255)
#     author=models.CharField(max_length=255)
#     skill=models.CharField(max_length=255)

#     def __str__(self):
#         return self.skill
# class Skills(models.Model):
#     user=models.ManyToManyField(User )
#     skill=models.CharField(max_length=255)

#     def __str__(self):
#         return self.skill
# class Skills(models.Model):
#     user=models.ManyToManyField(User )
#     skill=models.CharField(max_length=255)

#     def __str__(self):
#         return self.skill
# class Skills(models.Model):
#     user=models.ManyToManyField(User )
#     skill=models.CharField(max_length=255)

#     def __str__(self):
#         return self.skill
# class Skills(models.Model):
#     user=models.ManyToManyField(User )
#     skill=models.CharField(max_length=255)

#     def __str__(self):
#         return self.skill
# class Skills(models.Model):
#     user=models.ManyToManyField(User )
#     skill=models.CharField(max_length=255)

#     def __str__(self):
#         return self.skill
# class Skills(models.Model):
#     user=models.ManyToManyField(User )
#     skill=models.CharField(max_length=255)

#     def __str__(self):
#         return self.skill
# class Skills(models.Model):
#     user=models.ManyToManyField(User )
#     skill=models.CharField(max_length=255)

#     def __str__(self):
#         return self.skill
# class Skills(models.Model):
#     user=models.ManyToManyField(User )
#     skill=models.CharField(max_length=255)

#     def __str__(self):
#         return self.skill
# class Skills(models.Model):
#     user=models.ManyToManyField(User )
#     skill=models.CharField(max_length=255)

#     def __str__(self):
#         return self.skill
