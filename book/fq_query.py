from django.http import HttpResponse
from book.models import Book, Author, AuthorDetail, Publish


def fq_query(request):
    from django.db.models import F, Q
    print(request)

    # 查询 评论数 大于 收藏数 的书籍
    books = Book.objects.filter(comment_nums__gt=F('keep_nums'))
    print(books)  # <QuerySet [<Book: 赳赳老秦>]>

    # 查询 价格 大于 100 或  评论数 大于 3000
    books = Book.objects.filter(Q(price__gt=100)|Q(comment_nums__gt=3000))
    print(books.query)
    print(books)  # <QuerySet [<Book: 三国志>, <Book: 西游记>, <Book: 赳赳老秦>]>

    return HttpResponse('F&Q查询')
