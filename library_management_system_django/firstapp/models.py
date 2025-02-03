from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    registrationno = models.IntegerField(primary_key=True)
    bankaccount = models.IntegerField()
    cnic = models.IntegerField()
    phoneno = models.BigIntegerField()
    def __str__(self):
        return self.name

class Book(models.Model):
    bname = models.CharField(max_length=255)
    bisbn = models.IntegerField()
    bookid = models.IntegerField(primary_key=True)
    bookcategory = models.CharField(max_length=255)
    bookstatus = models.CharField(max_length=255)
    def __str__(self):
        return self.bname

class BookAuthor(models.Model):
    bookid = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length=255)
    def __str__(self):
        return self.author

class BookIssue(models.Model):
    bookid = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    registration = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateField()

class Fine(models.Model):
    fineID = models.IntegerField()
    Amount = models.IntegerField()
    registration = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class BookPlace(models.Model):
    bookid = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    slot = models.IntegerField()