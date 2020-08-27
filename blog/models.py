from django.db      import models
from django.conf    import settings
from django.utils   import timezone

class Post(models.Model):
    author  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title   = models.CharField(max_length = 200)
    text    = models.TextField()
    created_date    = models.DateTimeField(default = timezone.now)
    published_date  = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Etry(models.Model):
    positionTitle   = models.CharField(max_length = 200)
    text            = models.TextField()
    start_date      = models.DateTimeField(default = timezone.now)
    end_date        = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.positionTitle

class Section(models.Model):
    title   = models.CharField(max_length = 200)
    content = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
