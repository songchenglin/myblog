from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length = 20)
    create_time = models.DateTimeField(auto_now_add = True)
    def __unicode__(self):
        return self.name
class Classification(models.Model):
    name = models.CharField(max_length = 20)
    def __unicode__(self):
        return self.name
class Author(models.Model):
    GENDER_CHOICES = (
        ('M','male'),
        ('F','female'),
        ('S','shemale'),
    )
    name = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 8,
                              choices = GENDER_CHOICES,
                              default = 'S')
    email = models.EmailField(blank = True)
    website = models.URLField(blank = True)
    def __unicode__(self):
        return u'%s' % self.name
class Article(models.Model):
    caption = models.CharField(max_length = 50)
    subcaption = models.CharField(max_length = 50, blank = True)
    publish_time = models.DateTimeField(auto_now_add = True)
    update_tiem = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(Author)
    classification = models.ForeignKey(Classification)
    tags = models.ManyToManyField(Tag, blank = True)
    content = models.TextField()
