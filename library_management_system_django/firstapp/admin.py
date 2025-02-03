from django.contrib import admin
from firstapp import models

admin.site.register(models.Book)
admin.site.register(models.BookAuthor)
admin.site.register(models.BookIssue)
admin.site.register(models.BookPlace)
admin.site.register(models.Fine)
admin.site.register(models.User)

# Register your models here.
