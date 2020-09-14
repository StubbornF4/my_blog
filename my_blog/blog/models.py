from django.db import models


#文章分类
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='名称')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')

    class Meta:
        verbose_name = verbose_name_plural = '分类'

#文章标签
class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='标签')

    class Meta:
        verbose_name = verbose_name_plural = '标签'

#文章
class ArticlePost(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    desc = models.CharField(max_length=1024, blank=True, verbose_name='摘要')
    body = models.TextField(verbose_name='正文', help_text="正文为Markdown格式")
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='分类'
    )
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-created_time']




