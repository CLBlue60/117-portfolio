from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    year = models.PositiveIntegerField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='projects')
    repository = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='static/img/', blank=True, null=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=100, help_text="Format: Month YYYY - Month YYYY or Month YYYY - Present")

    class Meta:
        ordering = ['-id']  

    def __str__(self):
        return f"{self.title} at {self.company}"
