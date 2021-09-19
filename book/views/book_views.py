from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from book.models import Book
from datetime import date
from book.views.model_enum import Math, Names


# Create your views here.

# def func(request):    #function based view
#     return render(request, "base.html")

    # print(request.method)
    # print("------------In function-----------")
    # return HttpResponse("Hi welcome to Home Page")
    # return JsonResponse({"Key": "Value"})

def homepage(request):
    if request.method == "POST":
        # print(request.POST)
        data = request.POST
        if not data.get("id"):
            if data["ispub"] == "Yes":
                Book.objects.create(name = data["nm"],
                    qty = data["qty"],
                    price = data["price"],
                    is_published = True,
                    published_date = date.today())
            elif data["ispub"] == "No":
                Book.objects.create(name = data["nm"],
                    qty = data["qty"],
                    price = data["price"],    # data.get("price")
                    is_published = False)

            return redirect("home")
        else:
            bid = data.get("id")
            book_obj = Book.objects.get(id=bid)
            book_obj.name = data["nm"]
            book_obj.qty = data["qty"]
            book_obj.price = data["price"]
            if data["ispub"] == "Yes":
                if book_obj.is_published:
                    pass
                else:
                    book_obj.is_published = True
                    book_obj.published_date = date.today()
            elif data["ispub"] == "No":
                if book_obj.is_published == True:
                    pass
            book_obj.save()
            return redirect("home")
 
    else:
        return render(request, template_name="home.html")
    # return HttpResponse("Hi welcome to Home Page")

def get_books(request):
    books = Book.objects.all()
    return render(request, template_name="books.html", context={"all_books": books})

def delete_book(request, id):
    # print(id, "delete book id")
    Book.objects.get(id=id).delete()
    return redirect("showbook")

def update_book(request, id):
    book_obj = Book.objects.get(id=id)
    return render(request, "home.html", context={"single_book": book_obj})

def soft_delete(request, id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_deleted = "Y"
    book_obj.save()
    return redirect("showbook")

def active_books(request):
    # all_active_books = Book.objects.filter(is_deleted="N")
    all_active_books = Book.active_books.all()
    return render(request, template_name="books.html", context={"all_books": all_active_books})

def inactive_books(request):
    # all_inactive_books = Book.objects.filter(is_deleted="Y")
    all_inactive_books = Book.inactive_books.all()
    return render(request, template_name="books.html", context={"all_books": all_inactive_books, "book_status": "InActive"})

def restore_books(request,id):
    restore_book_obj = Book.objects.get(id=id)
    restore_book_obj.is_deleted = "N"
    restore_book_obj.save()
    return redirect("showbook")




