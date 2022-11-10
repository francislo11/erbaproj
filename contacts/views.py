from email.message import EmailMessage
from unicodedata import name
from urllib import response
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from . models import Contact


def inquiry(request):
    return render(request, "contacts/inquiry.html")


def contacts(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            message = request.POST['message']

            member = Contact(name=name, email=email, phone=phone,
                             address=address, message=message)
            member.save()
            context = {
                'id': member.pk,
                'name': name,
                'message': message,
                'phone': phone,
                'address': address,
            }
            return render(request, "accounts/dashboard.html", context)
    else:
        return render(request, "pages/index.html")


class TaskDetail():
    def get(self, request, pk):
        if request.user.is_authenticated:
            if request.method == 'GET':
                task = Contact.objects.get(id=pk)
                context = {
                    'id': task.id,
                    'name': task.name,
                    'email': task.email,
                    'phone': task.phone,
                    'address': task.address,
                    'message': task.message,
                }
                return render(request, 'accounts/dashboard.html', context)

        return render(request, "pages/index.html")


def update(request, id):
    if request.user.is_authenticated:
        mymember = Contact.objects.get(id=id)
        context = {
            'mymember': mymember,
        }
        return render(request, "contacts/update.html", context)
    else:
        return render(request, "pages/index.html")


def delete(request, id):
    if request.user.is_authenticated:
        mymember = Contact.objects.get(id=id)
        mymember.delete()
        response = redirect("/")
        return response
    else:
        return render(request, "pages/index.html")


def updaterecord(request, id):
    if request.user.is_authenticated:
        mymember = Contact.objects.get(id=id)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        message = request.POST['message']

        mymember = Contact(pk=id, name=name, email=email, phone=phone,
                           address=address, message=message)

        mymember.save()
        return render(request, "accounts/logout.html")
    else:
        return render(request, "pages/index.html")
