from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title

def banner_img(instance, filename):
    return f"{instance.title}/banner-{filename}"

def title_img(instance, filename):
    return f"{instance.title}/title-{filename}"

def trailer_video(instance, filename):
    return f"{instance.title}/trailer-{filename}"

class Anime(models.Model):
    title = models.CharField(max_length=20)
    sinopse = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    min_faixaE = models.IntegerField()
    year = models.DateField()
    data_public = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(upload_to=banner_img)
    titleimg = models.ImageField(upload_to=title_img)
    trailer = models.FileField(upload_to=trailer_video)

    def __str__(self):
        return self.title

class SeasonGroup(models.Model):
    number = models.IntegerField(unique=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)

class EpsGroup(models.Model):
    title = models.CharField(max_length=10)
    seasonGroup = models.ForeignKey(SeasonGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

def episode_file(instance, filename):
    return f"{instance.group}/{filename}"

class Episode(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    file = models.FileField(upload_to=episode_file, blank=True)
    group = models.ForeignKey(EpsGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name