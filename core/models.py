from django.db import models


class Message(models.Model):
    '''
    留言信息
    '''
    name = models.CharField('姓名', max_length=100, null=True, blank=True)
    email = models.CharField('电子邮箱', max_length=100, null=True, blank=True)
    tel = models.CharField('电话', max_length=50, null=True, blank=True)
    message = models.TextField('留言', max_length=1000, null=True, blank=True)
    date = models.DateTimeField('创建日期',auto_now_add=True)

    class Meta:
        verbose_name = "留言信息"
        verbose_name_plural = "留言信息库"
        ordering = ['id']

    def __str__(self):
        return self.name
