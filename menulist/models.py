from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        db_table    = "category"

    name        = models.CharField(verbose_name="カテゴリ名",max_length=10)

    def __str__(self):
        return self.name

class Menu(models.Model):
    class Meta:
        db_table    = "menu"

    category    = models.ForeignKey(Category,verbose_name="カテゴリ名",on_delete=models.PROTECT)
    name        = models.CharField(verbose_name="品名",max_length=20)
    breakfast   = models.BooleanField(verbose_name="朝メニュー",default=True)
    lunch       = models.BooleanField(verbose_name="昼メニュー",default=True)
    dinner      = models.BooleanField(verbose_name="夜メニュー",default=True)
    takeout     = models.BooleanField(verbose_name="テイクアウト",default=True)
    price       = models.IntegerField(verbose_name="価格")

    def __str__(self):
        return self.name
