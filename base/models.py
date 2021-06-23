from django.db import models

# Create your models here.


class Class_list(models.Model):
    stu_class = models.IntegerField()

    def __str__(self):
        return str(self.stu_class)


class Subject(models.Model):
    stu_class = models.ForeignKey(Class_list, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=50)
    subject_code = models.CharField(max_length=4, default="AAA")

    def __str__(self):
        return str(self.stu_class)+"-"+self.subject_code


class Chapter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    chapter = models.CharField(max_length=50)

    def __str__(self):
        return str(self.subject) + " ::  "+self.chapter


class Material(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name
