from django.db import models


# Create your models here.


class Author(models.Model):
    # django 默认会帮我们生成自增主键id，故直接生成表之后使用pk即可
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    # 与AuthorDetail建立一对一的关系,OneToOneField会创建一个唯一约束字段author_detail_id字段实现一对一关系
    author_detail = models.OneToOneField(to="AuthorDetail", on_delete=models.CASCADE)  # 级联删除

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    # id = models.AutoField(primary_key=True)
    birthday = models.DateTimeField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)
    hobby = models.CharField(max_length=32, null=True)  # 新增字段，务必设置字段允许为空，不然migrations报错


class Publish(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Book(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    pub_date = models.DateTimeField()
    price = models.DecimalField(max_digits=9, decimal_places=2)  # 9999999.99

    # 与Publish建立一对多的关系,外键字段ForeignKey会生成publisher_id建立在多的一方
    # publish = models.ForeignKey(to="Publish", to_field="pk", on_delete=models.CASCADE)  # 级联删除
    publish = models.ForeignKey(to="Publish", on_delete=models.CASCADE)  # 级联删除

    # 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表book_authors实现多对多的关系
    authors = models.ManyToManyField(to='Author')

    def __str__(self):
        return self.title
