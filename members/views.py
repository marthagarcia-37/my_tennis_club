from django.views import View
from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import Member


class MembersView(View):
    def get(self, request):
        miembros = Member.objects.all()
        contexto = {"miembros": miembros, "titulo": "Miembros del Club"}
        return render(request, "myfirst.html", contexto)
    
    def post(self, request):
        fname = request.POST.get("fname", "")
        lname = request.POST.get("lname", "")
        print("fname:", fname, "lname:", lname)
        miembros = Member.objects.filter(firstname__icontains=fname, lastname__icontains=lname)
        for member in miembros:
            print(member.firstname, member.lastname)
        contexto = {"miembros": miembros, "titulo": "Miembros del Club"}
        return render(request, "myfirst.html", contexto)

class MemberCreate(View):
    def get(self, request):
        form = MemberForm()
        contexto = {"form": form, "titulo": "Crear Miembro"}
        return render(request, "member_crud.html", contexto)

    def post(self, request):
        form = MemberForm(request.POST)
        contexto = {"form": form, "titulo": "Crear Miembro"}
        if form.is_valid():
            form.save()
            return redirect("miembros")
        return render(request, "member_crud.html", contexto)

class MemberUpdate(View):
    def get(self, request, pk):
        member = Member.objects.get(pk=pk)
        form = MemberForm(instance=member)
        contexto = {"form": form, "titulo": "Actualizar Miembro"}
        return render(request, "member_crud.html", contexto)

    def post(self, request, pk):
        member = Member.objects.get(pk=pk)
        form = MemberForm(request.POST, instance=member)
        contexto = {"form": form, "titulo": "Actualizar Miembro"}
        if form.is_valid():
            form.save()
            return redirect("miembros")
        return render(request, "member_crud.html", contexto)
    
class MemberDelete(View):
    def get(self, request, pk):
        member = Member.objects.get(pk=pk)
        member.delete()
        return redirect("miembros")