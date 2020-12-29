import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.abspath(__file__))             # 定位到django根目录
sys.path.append(os.path.abspath(os.path.join(BASE_DIR, os.pardir)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BMS.settings")   # django的settings文件
django.setup()


def test():
    from book.models import Book
    book = Book.objects.all()
    print(book)


if __name__ == '__main__':
    test()
