#coding=utf-8
from django.db import models


class BookStore(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=30)

    def __str__(self):
        return '%s'%self.store_name


class BookType(models.Model):
    booktype_id = models.AutoField(primary_key=True)
    book_type = models.CharField(max_length=30)
    borrow_days = models.IntegerField(max_length=30)

    def __str__(self):
        return '%s'%self.book_type


class ReaderType(models.Model):
    readertype_id = models.AutoField(primary_key=True)
    reader_type = models.CharField(max_length=30)
    reader_borrow_num = models.IntegerField(max_length=30)


class Jurisdiction(models.Model):
    jurisdiction_id = models.AutoField(primary_key=True)
    system_settings = models.BooleanField()
    reader_manage = models.BooleanField()
    boook_manage = models.BooleanField()
    book_return_borrow = models.BooleanField()
    system_search = models.BooleanField()

class Reader(models.Model):
    reader_id = models.AutoField(primary_key=True)
    reader_name = models.CharField(max_length=30)
    reader_type = models.ForeignKey(ReaderType,on_delete=models.CASCADE)
    reader_card = models.IntegerField(max_length=30)
    reader_phone = models.IntegerField(max_length=30)
    reader_email = models.CharField(max_length=30)

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=30)
    admin_password = models.CharField(max_length=30)
    admin_jurisdiction = models.ForeignKey(Jurisdiction,on_delete=models.CASCADE)
    admin_phone = models.IntegerField(max_length=30)

class Book(models.Model):
    book_id = models.AutoField(primary_key=30)
    book_name = models.CharField(max_length=30)
    book_store = models.ForeignKey(BookStore,on_delete=models.CASCADE)
    book_type = models.ForeignKey(BookType,on_delete=models.CASCADE)
    book_publishing = models.CharField(max_length=30)
    book_author = models.CharField(max_length=30)
    book_price = models.IntegerField(max_length=30)
    book_num = models.IntegerField(max_length=30)

class BookBorrow(models.Model):
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    reader_id = models.ForeignKey(Reader,on_delete=models.CASCADE)
    borrow_date = models.DateField()
    private_date = models.DateField()
    if_return = models.BooleanField()
    borrow_num = models.IntegerField(max_length=30)

    class Meta:
        unique_together = (('reader_id','book_id'),)

class BookReturn(models.Model):
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    reader_id = models.ForeignKey(Reader,on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField()

    class Meta:
        unique_together = (('reader_id','book_id'),)

class BookRenewal(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader_id = models.ForeignKey(Reader, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    renewal_date = models.DateField()

    class Meta:
        unique_together = (('reader_id','book_id'),)

class LibraryInfo(models.Model):
    lib_id = models.AutoField(primary_key=True)
    lib_name = models.CharField(max_length=30)
    lib_manager = models.CharField(max_length=30)
    lib_phone = models.IntegerField(max_length=30)
    lib_location = models.CharField(max_length=30)
    lib_email = models.CharField(max_length=30)
    lib_url = models.CharField(max_length=30)
    lib_build = models.DateField()
    lib_info = models.TextField()

class TransactionCard(models.Model):
    transactioncard_id = models.AutoField(primary_key=True)
    price = models.IntegerField(max_length=30)
    indate = models.IntegerField(max_length=30)
