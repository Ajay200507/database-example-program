from django.shortcuts import render
from django.http import HttpResponse
from testApp.models import people_details

# Create your views here.

def index(request):
    return render(request,'form.html')

def index_html(request):
    data = [
        {
            'name':'bob',
            'age':31,
            'city':'new york',
            'show':'0'
        },
        {
            'name':'george',
            'age':41,
            'city':'new york',
            'show':'1'

        },
        {
            'name':'angel',
            'age':21,
            'city':'new jersey',
            'show':'1'

        },
    
    ]
    obj = people_details.objects.all().values()
    print('#########',data)
    print(list(obj))


    return render(request, 'index.html',{'data_list':list(obj)})




def insert_data(request):
    name1 = request.POST['name']
    age1 = request.POST['age']
    city1 = request.POST['city']
    show1 = request.POST['show']
    print('########', name1,age1,city1,show1)
    obj = people_details(
                        name = name1,
                        age = age1,
                        city = city1,
                        show = show1
                        )
    obj.save()

    return HttpResponse('inserted')



# insert into table_name (col1,col2,col3,)

