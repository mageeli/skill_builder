from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=30)
    progress = models.CharField(max_length=30)
    learning_time = models.CharField(max_length=30)


class SubSkill(models.Model):
    title = models.CharField(max_length=30)
    progress = models.CharField(max_length=30)
    learning_time = models.CharField(max_length=30)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    text = models.TextField(default=' ')


class Post(models.Model):
    title = models.CharField(max_length=30)
    assessment = models.CharField(max_length=30)
    subSkill = models.ForeignKey(SubSkill, on_delete=models.CASCADE)
    text = models.TextField()