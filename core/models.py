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


class picture(models.Model):
    title = models.CharField('标题', max_length=20)
    caption = models.CharField('内容', max_length=34, blank=True, null=True)
    filepath = models.CharField('文件地址', max_length=200, blank=True, null=True)  # 头像路径
    dimDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "图片"
        verbose_name_plural = "图片库"
        ordering = ['id']

    def __str__(self):
        return self.title



class carousel(models.Model):

    """
    轮播.
    """
    title = models.CharField('标题', max_length=50)
    imgs = models.ManyToManyField(picture)
    link = models.CharField('链接地址（可为空）', max_length=50, blank=True)
    caption = models.CharField('子标题', max_length=500, blank=True, null=True)
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '轮播管理'
        ordering = ['-dimDate'] # sorted news by dimdate


class article(models.Model):
    '''
    文章
    '''
    title = models.CharField('文章标题', max_length=50)
    imgs = models.ForeignKey(picture, to_field='id', null=True)
    content = models.TextField('文章详情')
    viewedTimes = models.IntegerField('浏览次数')
    type = models.CharField('文章类型',max_length=50,blank=True,null=True)
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '文章'
        ordering = ['-dimDate'] # sorted news by dimdate


class user(models.Model):
    username = models.CharField('登录名', max_length=20, blank=True, null=False,unique=True)  # 登录名、昵称，唯一校验
    pwd = models.CharField('密码', max_length=34, blank=True, null=True)
    avt = models.ForeignKey(picture,to_field='id',null=True)
    salt=models.CharField('密码盐值',max_length=32,blank=True,null=True)
    type = models.CharField('用户类型', max_length=32, blank=True, null=True)
    dimDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "用户资料表"
        verbose_name_plural = "users"
        ordering = ['id']

    def __str__(self):
        return self.username


class flowgroup(models.Model):
    name=models.CharField('名字',max_length=20)
    user = models.ManyToManyField(user)
    dimDate = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "流程组表"
        verbose_name_plural = "流程组们"
        ordering = ['id']

    def __str__(self):
        return self.name


class flow(models.Model):
    name=models.CharField('名字',max_length=20)
    groupName=models.ForeignKey(flowgroup)
    orderId=models.CharField('下一个流程id号',max_length=20)
    user = models.ManyToManyField(user)
    dimDate = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "流程表"
        verbose_name_plural = "流程们"
        ordering = ['id']

    def __str__(self):
        return self.name
