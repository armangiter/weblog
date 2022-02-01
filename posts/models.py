from djongo import models


class Comment(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    content = models.TextField(max_length=255, null=True, blank=True)
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True, blank=True)
    reply = models.ForeignKey('Comment', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.content}"


class Source(models.Model):
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.link}"


class Author(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    title = models.CharField(max_length=40, null=True, blank=True)
    text = models.TextField(max_length=255, blank=True, null=True)
    source = models.ArrayReferenceField(to=Source, null=True, blank=True)
    author = models.ArrayField(model_container=Author, null=True, blank=True)

    def __str__(self):
        return f"title : {self.title} text : {self.text} source : {self.source} author : {self.author}"
