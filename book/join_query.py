from django.http import HttpResponse
from book.models import Book, Author, AuthorDetail, Publish


def join_query(request):
    print(request)
    # 基于双划线的查询(join)

    # 一对多
    """
       正向跨表(由关联字段所在表查询其关联的表)：按关联字段__查询字段
       反向跨表：按表名称小写__查询字段
    """
    # 1、一对多

    # 正跨查询：查询西游记出版社的名字和邮箱

    # 正跨：关联字段所在表 查询 其所关联的表记录
    # ret = Book.objects.filter(title='西游记').values('publish__name', 'publish__email')
    # print(ret)   # <QuerySet [{'publish__name': '小橘子出版社', 'publish__email': '222@666.com'}]>
    #
    # ret = Book.objects.filter(publish__name='小橘子出版社').values('title')
    # print(ret)   # <QuerySet [{'title': '西游记'}, {'title': '赳赳老秦'}]>
    #
    # # 反跨查询：查询小橘子出版社的所有书籍
    # ret = Publish.objects.filter(book__title='西游记').values('name', 'email')
    # print(ret)   # <QuerySet [{'name': '小橘子出版社', 'email': '222@666.com'}]>
    #
    # ret = Publish.objects.filter(name='小橘子出版社').values('book__title')
    # print(ret)   # <QuerySet [{'book__title': '西游记'}, {'book__title': '赳赳老秦'}]>

    # 2、多对多
    # 正向查询
    # # 查询西游记所有作者的名字
    #
    # ret = Book.objects.filter(title='西游记').values('authors__name')
    # print(ret)     # <QuerySet [{'authors__name': '强子'}, {'authors__name': '乖乖快回家'}]>
    #
    # ret = Author.objects.filter(book__title='西游记').values('name')
    # print(ret)     # <QuerySet [{'name': '强子'}, {'name': '乖乖快回家'}]>
    #
    # # 反向查询
    # # 查询 强子 所有出版过的书籍名称
    # ret = Author.objects.filter(name='强子').values('book__title')
    # print(ret)     # <QuerySet [{'book__title': '西游记'}, {'book__title': '三国志'}]>
    #
    # ret = Book.objects.filter(authors__name='强子').values('title')
    # print(ret)  # <QuerySet [{'title': '西游记'}, {'title': '三国志'}]>

    # 3、一对一
    """
    正向查询：按字段
    反向查询：按表名称小写，一对一对象查询，返回一个对象
    """
    # 正向查询
    # 查询强子的手机号
    # ret = Author.objects.filter(name='强子').values('author_detail__telephone')
    # print(ret)   # <QuerySet [{'author_detail__telephone': 111}]>
    #
    # ret = AuthorDetail.objects.filter(telephone='111').values('author__name')
    # print(ret)  # <QuerySet [{'author__name': '强子'}]>
    #
    # # 反向查询
    # # 查询手机号为111的作者名字
    # ret = AuthorDetail.objects.filter(author__name='强子').values('telephone')
    # print(ret)   # <QuerySet [{'telephone': 111}]>
    #
    # ret = Author.objects.filter(author_detail__telephone='111').values('name')
    # print(ret)  # <QuerySet [{'name': '强子'}]>

    # 进阶跨表
    # 跨表查询小橘子出版社出版过的所有书籍名字以及作者的姓名
    # 正向跨表
    # ret = Book.objects.filter(publish__name='小橘子出版社').values('title', 'authors__name')
    # print(ret)
    # <QuerySet [{'title': '西游记', 'authors__name': '强子'}, {'title': '西游记', 'authors__name': '乖乖快回家'}, {'title': '赳赳老秦', 'authors__name': '大猩猩'}, {'title': '赳赳老秦', 'authors__name': '马大哈'}]>

    # 反向查询
    # ret = Publish.objects.filter(name='小橘子出版社').values('book__title', 'book__authors__name')
    # print(ret)
    # <QuerySet [{'book__title': '西游记', 'book__authors__name': '强子'}, {'book__title': '西游记', 'book__authors__name': '乖乖快回家'}, {'book__title': '赳赳老秦', 'book__authors__name': '大猩猩'}, {'book__title': '赳赳老秦', 'book__authors__name': '马大哈'}]>

    # 查询手机号以111开头的作者出版过的所有书籍名称以及出版社名称

    # 方式1：
    query_ret = Book.objects.filter(authors__author_detail__telephone__regex=r'^111').\
        values_list('title',  'publish__name')
    print(query_ret)  # <QuerySet [('西游记', '小橘子出版社'), ('三国志', '小苹果出版社')]>

    # 方式2：
    ret = Author.objects\
        .filter(author_detail__telephone__regex=r'^111')\
        .values('book__title', 'book__publish__name')
    print(ret)
    # <QuerySet [{'book__title': '西游记', 'book__publish__name': '小橘子出版社'}, {'book__title': '三国志', 'book__publish__name': '小苹果出版社'}]>





    return  HttpResponse('join查询成功！')