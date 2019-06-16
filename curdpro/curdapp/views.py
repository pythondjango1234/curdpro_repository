from django.shortcuts import render
from .models import ProductData
from .forms import InsertingDataForm ,UpdatingDataForm, DeletingDataForm
from django.http.response import HttpResponse


def main_page_view(request):
    return render(request,'curd_main_page.html')


def create_page_view(request):
    if request.method=="POST":
        cform=InsertingDataForm(request.POST)
        if cform.is_valid():
            Product_Id=request.POST.get('Product_Id','')
            Product_Name = request.POST.get('Product_Name', '')
            Product_Cost = request.POST.get('Product_Cost', '')
            Product_Color= request.POST.get('Product_Color', '')
            Product_Class= request.POST.get('Product_Class', '')
            Customer_Name = request.POST.get('Customer_Name', '')
            Customer_Mobile= request.POST.get('Customer_Mobile', '')
            Customer_Email = request.POST.get('Customer_Email', '')
            data=ProductData(
                Product_Id=Product_Id,
                Product_Name=Product_Name,
                Product_Cost=Product_Cost,
                Product_Color=Product_Color,
                Product_Class=Product_Class,
                Customer_Name=Customer_Name,
                Customer_Mobile=Customer_Mobile,
                Customer_Email=Customer_Email,
            )
            data.save()
            cform=InsertingDataForm()
            return render(request,'curd_insert_page.html',{'cform':cform})
        else:
            return HttpResponse("Invalid Data")
    else:
        cform = InsertingDataForm()
        return render(request, 'curd_insert_page.html', {'cform':cform})

def retrieve_page_view(request):
    Product_Data=ProductData.objects.all()
    return render(request,'curd_retrieve_page.html',{'pdata':Product_Data})
def update_page_view(request):
    if request.method=="POST":
        uform=UpdatingDataForm(request.POST)
        if uform.is_valid():
            Product_Id=request.POST.get('Product_Id','')
            Product_Cost=request.POST.get('Product_Cost','')
            pid=ProductData.objects.filter(Product_Id=Product_Id)
            if not pid:
                return HttpResponse("Invalid Product Id")
            else:
                pid.update(Product_Cost=Product_Cost)
                uform=UpdatingDataForm()
                return render(request,'curd_update_page.html',{'uform':uform})
        else:
            return HttpResponse("invalid User Data")
    else:
        uform=UpdatingDataForm()
        return render(request, 'curd_update_page.html', {'uform': uform})
def delete_page_view(request):
    if request.method=="POST":
        dform=DeletingDataForm(request.POST)
        if dform.is_valid():
            Product_Id=request.POST.get('Product_Id')
            pid=ProductData.objects.filter(Product_Id=Product_Id)
            if not pid:
                return HttpResponse("Product Id is not available")
            else:
                pid.delete()
                dform=DeletingDataForm()
                return render(request,'curd_delete_page.html',{'dform':dform})
        else:
            return HttpResponse("Invalid Form")
    else:
        dform=DeletingDataForm()
        return render(request,'curd_delete_page.html',{'dform':dform})


