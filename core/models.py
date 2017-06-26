from django.db import models


class Message(models.Model):
    '''
    留言信息
    '''
    name = models.CharField('姓名', max_length=100, null=True, blank=True)
    email = models.CharField('电子邮箱', max_length=100, null=True, blank=True)
    tel = models.CharField('电话', max_length=50, null=True, blank=True)
    message = models.TextField('留言', max_length=1000, null=True, blank=True)
    date = models.DateTimeField('创建日期', auto_now_add=True, null=True)

    class Meta:
        verbose_name = "留言信息"
        verbose_name_plural = "留言信息库"
        ordering = ['id']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('姓名', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "新闻标签"
        verbose_name_plural = "新闻标签"
        ordering = ['id']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('姓名', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "新闻分类"
        verbose_name_plural = "新闻分类"
        ordering = ['id']

    def __str__(self):
        return self.name


class NewsImg(models.Model):
    Image = models.FileField('图片', upload_to='core/static/upload/')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.Image.name

    class Meta:
        verbose_name = '图片新闻'
        verbose_name_plural = "图片新闻"
        ordering = ['-dimDate']


class News(models.Model):
    '''
    新闻
    '''

    name = models.CharField('姓名', max_length=500, null=True, blank=True)
    tag = models.ManyToManyField(Tag)
    cat = models.ForeignKey(Category)
    arthur = models.CharField('作者', max_length=500, null=True, blank=True)
    img = models.FileField('主要图片（480*270）', upload_to='core/static/img/')
    summary = models.CharField('文章简介', max_length=5000, null=True, blank=True)
    content = models.TextField('文章内容', max_length=500000, null=True, blank=True)
    dimdate = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = "新闻"
        ordering = ['-dimdate']