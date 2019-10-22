from django.db import models

# Create your models here.

class NewType(models.Model):
    label = models.CharField(max_length = 32)
    decription = models.TextField()
    def __str__(self):
        return self.label

class Editor(models.Model):
    name = models.CharField(max_length = 32)
    email = models.EmailField()
    def __str__(self):
        return self.name

class New(models.Model):
    title = models.CharField(max_length = 32, verbose_name="新闻标题" )
    time = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to = "img/upload")
    content = models.TextField()
    type_id = models.ForeignKey(to=NewType, on_delete=models.CASCADE)
    # models.CASCADE 级联删除
    # models.SET_NULL 设置为空
    # models.SET_DEFAULT 设置默认值，比如：删除作者，书的作者为佚名
    editor_id = models.ManyToManyField(to=Editor)
    def __str__(self):
        return self.title

