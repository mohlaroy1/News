from django.core.exceptions import ValidationError
from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(published=True)


class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title=models.CharField(max_length=255)
    intro=models.TextField(max_length=1000)
    cover=models.ImageField(upload_to='article/cover/')

    views=models.PositiveIntegerField(default=0)
    read_time=models.DurationField(blank=True, null=True)

    author=models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    tags=models.ManyToManyField(Tag)

    published=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    objects=models.Manager()
    pub_objects=PublishedManager()

    def __str__(self):
        return self.title


class Context(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    text=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='article/context/',blank=True,null=True)

    def clean(self):
        if not self.text and not self.image:
            raise ValidationError("Iltimos rasm yoki matn kiriting!")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)



class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(blank=True,null=True)
    text=models.TextField()

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(blank=True,null=True)
    phone_number=models.CharField(blank=True,null=True,max_length=15)
    subject=models.CharField(max_length=255)
    message=models.TextField(blank=True,null=True)
    seen=models.BooleanField(default=False)

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Newsletter(models.Model):
    email=models.EmailField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email}"







