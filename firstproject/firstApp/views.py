from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee

# Create your views here.

def employeeView(request):
    # emp={
    #     "id":121,
    #     "name":"Avinash",
    #     "salary":"1200000"
    # }  

    data=Employee.objects.all()
    #data is a query set we cant return query set
    response={'employees':list(data.values('name','salary'))}
    return JsonResponse(response)
