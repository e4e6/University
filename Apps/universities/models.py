from django.db import models

# Create your models here.

class Privilige(models.Model): ## yemekhane kulüpler
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "priviligies"


class Campus(models.Model): ## kampüsler
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "campuses"


class Department(models.Model):
    name = models.CharField(max_length=200)
    departmentType = models.CharField(max_length=200, default="", blank=True, null=True)  ## Lisans mı yükske lisans mı önlisans
    puanType = models.CharField(max_length=200, default="", blank=True, null=True)
    minimumPuan =  models.CharField(max_length=200, default="", blank=True, null=True)
    minimumRanking =  models.CharField(max_length=200, default="", blank=True, null=True)
    educaitonLanguage = models.CharField(max_length=200, default="", blank=True, null=True)
    theTimeofEducation = models.CharField(max_length=200, default="", blank=True, null=True) ## birinci öğretim ikinci öğretim
    presentageofScholarhip = models.CharField(max_length=200, default="", blank=True, null=True) ## bursluluk oranı
    tution = models.CharField(max_length=200, default="", blank=True, null=True) ## parası
    years = models.CharField(max_length=200, default="", blank=True, null=True)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=200)
    departmentList = models.ManyToManyField(Department, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "faculties"


class University(models.Model):

    def upload_to_func(self,filename):
        return "images/{}/{}".format(self.name, filename)

    name = models.CharField(max_length=200)
    info = models.CharField(max_length=200, default="")
    detailedInfo = models.TextField(max_length=3200, default="")

    country = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")

    numberOfLocalStudents = models.CharField(max_length=200, default="")
    numberOfForeignStudents = models.CharField(max_length=200, default="")
    universityType = models.CharField(max_length=200, default="")

    # profile_photo_path = models.CharField(max_length=200, default="")
    # cover_photo_path = models.CharField(max_length=200, default="" )

    profile_photo = models.ImageField(null=True, blank=True, upload_to=upload_to_func, default='images/default/logo.png')
    cover_photo = models.ImageField(null=True, blank=True, upload_to=upload_to_func, default='images/default/cover.jpg')
    images = models.CharField(max_length=200, default="", blank=True, null=True)

    website_link = models.CharField(max_length=200, default="#")
    pinterest_link = models.CharField(max_length=200, default="https://tr.pinterest.com/" , blank=True, null=True)
    twitter_link = models.CharField(max_length=200, default="https://twitter.com/" , blank=True, null=True)
    instagram_link = models.CharField(max_length=200, default="https://www.instagram.com/" , blank=True, null=True)
    linkedin_link = models.CharField(max_length=200, default="https://www.linkedin.com/" , blank=True, null=True)
    facebook_link = models.CharField(max_length=200, default="https://www.facebook.com/" , blank=True, null=True)

    numberOfAcademicians= models.CharField(max_length=200, default="")
    location = models.CharField(max_length=200, default="")

    facultyList = models.ManyToManyField(Faculty, blank=True)
    priviligeList = models.ManyToManyField(Privilige, blank=True)
    campusList = models.ManyToManyField(Campus, blank=True)


    # Gets events for that university (primary key used)
    def GetEvents(self):
        return "\n".join([e.name for e in self.eventList.all()])

    GetEvents.short_description = 'events'

    # This is used to seriliaze events
    def natural_key(self):
        return (self.id, self.name)


    def __str__(self):
        return self.name

    def getid(self):
        return str(self.id)

    def getwebsitelink(self):
        return 'http://' + self.website_link + '/'

    class Meta:
        verbose_name_plural = "universities"



    # def getprofilePhoto(self):
    #     return '/static/assets/img/universities/' + str(self.id) + '/' + self.profile_photo_path

    # def getcoverPhoto(self):
    #     return '/static/assets/img/universities/' + str(self.id) + '/' + self.cover_photo_path



