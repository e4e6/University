from django.db import models

# Create your models here.




class University(models.Model):

    def upload_to_func(self,filename):
        return "images/{}/{}".format(self.id, filename)

    name = models.CharField(max_length=200)
    info = models.CharField(max_length=200, default="")

    country = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")

    numberOfLocalStudents = models.CharField(max_length=200, default="")
    numberOfForeignStudents = models.CharField(max_length=200, default="")
    universityType = models.CharField(max_length=200, default="")

    # profile_photo_path = models.CharField(max_length=200, default="")
    # cover_photo_path = models.CharField(max_length=200, default="" )

    profile_photo = models.ImageField(null=True, blank=True, upload_to=upload_to_func)
    cover_photo = models.ImageField(null=True, blank=True, upload_to=upload_to_func)
    images = models.CharField(max_length=200, default="", blank=True, null=True)



    website_link = models.CharField(max_length=200, default="")
    pinterest_link = models.CharField(max_length=200, default="" , blank=True, null=True)
    twitter_link = models.CharField(max_length=200, default="" , blank=True, null=True)
    instagram_link = models.CharField(max_length=200, default="" , blank=True, null=True)
    linkedin_link = models.CharField(max_length=200, default="" , blank=True, null=True)
    facebook_link = models.CharField(max_length=200, default="" , blank=True, null=True)


    numberOfAcademicians= models.CharField(max_length=200, default="")
    location = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name

    def getid(self):
        return str(self.id)

    def getwebsitelink(self):
        return 'http://' + self.website_link + '/'



    # def getprofilePhoto(self):
    #     return '/static/assets/img/universities/' + str(self.id) + '/' + self.profile_photo_path

    # def getcoverPhoto(self):
    #     return '/static/assets/img/universities/' + str(self.id) + '/' + self.cover_photo_path


class Faculty(models.Model):
    name = models.CharField(max_length=200)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    departmentType = models.CharField(max_length=200, default="")  ## Lisans mı yükske lisans mı önlisans
    puanType = models.CharField(max_length=200, default="")
    minimumPuan =  models.CharField(max_length=200, default="")
    minimumRanking =  models.CharField(max_length=200, default="")
    educaitonLanguage = models.CharField(max_length=200, default="")
    theTimeofEducation = models.CharField(max_length=200, default="") ## birinci öğretim ikinci öğretim
    presentageofScholarhip = models.CharField(max_length=200, default="") ## bursluluk oranı
    tution = models.CharField(max_length=200, default="") ## parası
    years = models.CharField(max_length=200, default="") ## parası

    def __str__(self):
        return self.name



class Privaligities(models.Model): ## yemekhane kulüpler
    name = models.CharField(max_length=200)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Campuses(models.Model): ## kampüsler
    name = models.CharField(max_length=200)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
