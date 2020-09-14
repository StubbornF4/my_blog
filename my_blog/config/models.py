from django.db import models


class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_HIDE, '隐藏'),
        (STATUS_SHOW, '展示'),
    )
    SIDE_TYPE = (
        (1, 'HTML'),
        (2, '最新文章'),
        (3, '最热文章'),
    )
    title = models.CharField(max_length=50, verbose_name='标题')
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE, verbose_name='展示类型')
    contents = models.CharField(max_length=500, blank=True, help_text="如果不是html类型，可为空", verbose_name='内容')

    class Meta:
        verbose_name = verbose_name_plural = '侧边栏'