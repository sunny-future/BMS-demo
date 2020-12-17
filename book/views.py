from django.shortcuts import render, redirect
from book.models import Book, Publish, Author, AuthorDetail
# Create your views here.


def index(request):
    books = Book.objects.all()
    print(books.query)
    return render(request, 'book/index.html', {"books": books})


def show_book(request):
    books = Book.objects.all()
    return render(request, 'book/index.html', {"books": books})


def add_book(request):
    if request.method == 'GET':
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        return render(request, 'book/add_book.html', {"publish_list": publish_list, "author_list": author_list})
    else:
        # 方式一：
        # title = request.POST.get('title')
        # price = request.POST.get('price')
        # pub_date = request.POST.get('pub_date')
        # publisher_id = request.POST.get('publisher_id')
        # author_id = request.POST.get('author_id')
        # print("publish_id", publisher_id, author_id)
        # book_obj = Book.objects.create(title=title, price=price, pub_date=pub_date, publisher_id=publisher_id)
        # author_obj = Author.objects.get(pk=author_id)
        # book_obj.authors.add(author_obj,)

        # 方式二:
        author_ids = request.POST.getlist('author_id')   # 通过getlist()方法获取完整的list数据
        params = request.POST.dict()   # dict()方法将querydict类型转为dict类型
        params.pop('author_id')
        book = Book.objects.create(**params)
        # **kwargs，注意：1）这里key务必等于字段名；2）这里key数量务必保持一致，不能多不能少

        book.authors.add(*author_ids)
        # add()方法可以传 *args，这里传值 *[]
        return redirect('/')


def delete_book(request, id_book):
    if request.method == 'GET':
        del_book = Book.objects.get(pk=id_book)
        return render(request, 'book/delete_book.html', {"del_book": del_book})
    else:
        Book.objects.filter(pk=id_book).delete()
        return redirect('/book/show_book/')


def update_book(request, id_book):
    if request.method == 'GET':
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        upd_book = Book.objects.get(pk=id_book)
        return render(request, 'book/update_book.html', {'upd_book': upd_book, 'publish_list': publish_list,
                                                         'author_list': author_list})
    else:
        author_ids = request.POST.getlist('author_ids')   # 通过getlist()方法获取完整的list数据
        params = request.POST.dict()   # dict()方法将querydict类型转为dict类型
        params.pop('author_ids')
        # 更新书籍，一对多关系, update返回 更新的条数，即返回一个整型
        Book.objects.filter(pk=id_book).update(**params)   # **kwargs，注意：1）这里key务必等于字段名；2）这里key数量务必保持一致，不能多不能少

        # 重置作者，多对多关系
        book = Book.objects.get(pk=id_book)
        book.authors.set(author_ids)          # set([1,2])，set()方法参数可以为列表，重置绑定关系(先清空，后绑定)
        return redirect('/')


def show_publish(request):
    publish_list = Publish.objects.all()
    return render(request, 'book/show_publish.html', {'publish_list': publish_list})


def add_publish(request):
    if request.method == 'GET':
        return render(request, 'book/add_publish.html')
    else:
        name = request.POST.get('name')
        city = request.POST.get('city')
        email = request.POST.get('email')
        Publish.objects.create(name=name, city=city, email=email)
        return redirect('/book/show_publish/')


def delete_publish(request, id_publish):
    Publish.objects.filter(pk=id_publish).delete()
    return redirect('/book/show_publish/')


def update_publish(request, id_publish):
    if request.method == 'GET':
        publish = Publish.objects.get(pk=id_publish)        # 这里需要拿到model对象，只能get取
        return render(request, 'book/update_publish.html', {'pub': publish})
    else:
        name = request.POST.get('name')
        city = request.POST.get('city')
        email = request.POST.get('email')
        Publish.objects.filter(pk=id_publish).update(name=name, city=city, email=email)
        return redirect('/book/show_publish/')


def show_author(request):
    author_list = Author.objects.all()
    return render(request, 'book/show_author.html', {'author_list': author_list})


def add_author(request):
    if request.method == 'GET':
        author_detail_list = AuthorDetail.objects.all()
        return render(request, 'book/add_author.html', {"author_detail_list": author_detail_list})
    else:
        name = request.POST.get('name')
        age = request.POST.get('age')
        author_detail_id = request.POST.get('author_detail_id')
        Author.objects.create(name=name, age=age, author_detail_id=author_detail_id)
        return redirect('/book/show_author/')


def delete_author(request, id_author):
    Author.objects.filter(pk=id_author).delete()
    return redirect('/book/show_author/')


def update_author(request, id_author):
    if request.method == 'GET':
        author = Author.objects.get(pk=id_author)        # 这里需要拿到model对象，只能get取
        print(author.name)
        author_detail_list = AuthorDetail.objects.all()
        return render(request, 'book/update_author.html', {'author': author, 'author_detail_list': author_detail_list})
    else:
        name = request.POST.get('name')
        age = request.POST.get('age')
        author_detail_id = request.POST.get('author_detail_id')
        Author.objects.filter(pk=id_author).update(name=name, age=age, author_detail_id=author_detail_id)
        return redirect('/book/show_author/')


def show_author_detail(request):
    show_author_detail_list = AuthorDetail.objects.all()
    return render(request, 'book/show_author_detail.html', {'author_detail_list': show_author_detail_list})


def add_author_detail(request):
    if request.method == 'GET':
        return render(request, 'book/add_author_detail.html')
    else:
        addr = request.POST.get('addr')
        birthday = request.POST.get('birthday')
        hobby = request.POST.get('hobby')
        telephone = request.POST.get('telephone')
        AuthorDetail.objects.create(addr=addr, birthday=birthday, hobby=hobby, telephone=telephone)
        return redirect('/book/show_author_detail/')


def delete_author_detail(request, id_author_detail):
    AuthorDetail.objects.filter(pk=id_author_detail).delete()
    return redirect('/book/show_author_detail/')


def update_author_detail(request, id_author_detail):
    if request.method == 'GET':
        author_detail = AuthorDetail.objects.get(pk=id_author_detail)        # 这里需要拿到model对象，只能get取
        print(author_detail.addr)
        return render(request, 'book/update_author_detail.html', {'id_author_detail': author_detail})
    else:
        # addr = request.POST.get('addr')
        # birthday = request.POST.get('birthday')
        # hobby = request.POST.get('hobby')
        # telephone = request.POST.get('telephone')
        # AuthorDetail.objects.filter(pk=id_author_detail).update(addr=addr, birthday=birthday,
        #                                                         hobby=hobby, telephone=telephone)
        data = request.POST.dict()
        AuthorDetail.objects.filter(pk=id_author_detail).update(**data)
        return redirect('/book/show_author_detail/')



