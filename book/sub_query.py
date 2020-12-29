from django.http import HttpResponse
from book.models import Book, Author, AuthorDetail, Publish


def sub_query(request):
    print(request)
    # 基于对象查询
    """
    正向查询：多找一，按字段
    反向查询：一找多，按表名称小写_set，其中set表示集合的意思
    """
    # 1、一对多

    # 正向查询：查询西游记出版社的名字和邮箱
    # book = Book.objects.get(title='西游记')
    # print(book.publish.name)
    # print(book.publish.email)

    # 反向查询：查询小橘子出版社的所有书籍
    pub = Publish.objects.get(name='小橘子出版社')
    # print(pub.book_set.all())  # 与这个出版社关联的所有书籍
    # print(pub.book_set.values('title', 'price'))

    # 2、多对多
    # 正向查询
    # 查询西游记所有作者的名字
    # book = Book.objects.get(title='西游记')
    # ret = book.authors.all().values('name')
    # print(ret)   # <QuerySet [{'name': '强子'}, {'name': '乖乖快回家'}]>

    # 反向查询
    # 查询 强子 所有出版过的书籍名称
    # author_obj = Author.objects.get(name='强子')
    # ret = author_obj.book_set.all()
    # print(ret)   # <QuerySet [<Book: 西游记>, <Book: 三国志>]>

    # 3、一对一
    """
    正向查询：按字段
    反向查询：按表名称小写，一对一对象查询，返回一个对象
    """
    # 正向查询
    # 查询强子的手机号
    author_obj = Author.objects.get(name='强子')
    ret = author_obj.author_detail.telephone
    print(ret)   # 111

    # 反向查询
    # 查询手机号为111的作者名字
    tel_obj = AuthorDetail.objects.get(telephone='111')
    ret = tel_obj.author.name
    print(ret)   # 强子

    return HttpResponse("子查询成功")
