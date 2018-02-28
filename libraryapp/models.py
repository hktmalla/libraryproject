from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=30, blank=False)
    roll_number = models.IntegerField(blank=False)
    address = models.CharField(max_length=15, blank=False)
    phone_number = models.IntegerField(blank=False)
    batch = models.DateField()


    def __str__(self):
    	return self.student_name


class Book(models.Model):
    s_id = models.CharField(max_length=20, blank=False)
    book_name = models.CharField(max_length=30, blank=False)
    author = models.CharField(max_length=20, blank=False)


    def __str__(self):
    	return self.book_name


class Issue(models.Model):
    issue_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    issue_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(blank=False)
    expire_date = models.DateField(blank=False)

