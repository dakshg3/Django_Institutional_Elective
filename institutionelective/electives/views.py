from django.shortcuts import render

from .models import Options
from .models import Choices
from .models import AdminLogin
from .models import allocated
from .models import timer

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout

from .forms import ChoiceForm, AdminForm

from datetime import datetime, timezone
import xlwt
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def finalform_view(request):
    return render(request, "electives/finalform.html", {})


def adminlogin_view(request):
    form2 = AdminForm()
    
    context = {
        'form2': form2
    }
    return render(request, "electives/adminlogin.html", context)

def adexport_view(request):
    id_u = request.POST.get('id_user_id')
    pas_u = request.POST.get('id_user_pass')
    pas_ch = AdminLogin.objects.values('user_pass','user_id')
    context = {}
    for i in pas_ch:
        if pas_u == i['user_pass'] and id_u == i['user_id']:
            id_u = False
            return render(request, "electives/adexport.html", context)
        else:
            return render(request, "electives/adminlogin.html", context)


def options_view(request):
    usns_obj = Choices.objects.values('usn')
    my_usn = request.user.username
    x=my_usn.upper()
    for i in usns_obj:
         if my_usn == i['usn']:
             my_usn = False
             logout(request)
    options_obj = Options.objects.all()
    depts_obj = Options.objects.values('dept').distinct()
    arr = [1, 2, 3, 4, 5]
    cno=['c1','c2','c3','c4','c5']

    alloc=allocated.objects.filter(usn=x).values_list('sub',flat=True)
    try:
	    context = {
		"usn": my_usn,
		"depts": depts_obj,
		"options": options_obj,
		"arr": arr,
		"cno": cno,
		"alloc":alloc[0]
	    }
    except:
	    context = {
			"usn": my_usn,
			"depts": depts_obj,
			"options": options_obj,
			"arr": arr,
			"cno": cno
		    }

    return render(request, "electives/form.html", context)

def insertdata_view(request):
    my_usn = request.POST.get('usn')
    c1 = request.POST.get('c1')
    c2 = request.POST.get('c2')
    c3 = request.POST.get('c3')
    c4 = request.POST.get('c4')
    c5 = request.POST.get('c5')
    temp = datetime.now().strftime('%H:%M:%S:%f')
    temp=str(temp)
    
    record = Choices(usn=my_usn, 
        choice1=c1, 
        choice2=c2, 
        choice3=c3, 
        choice4=c4, 
        choice5=c5,
        cur_time=temp)
    record.save()
    logout(request)
    context = {
        'usn': my_usn,
        'choices': [c1, c2, c3, c4, c5]
    }

    return render(request, "electives/insertdata.html", context)


def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="electives.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Choices')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['USN', 'Time', 'Choice 1', 'Choice 2', 'Choice 3', 'Choice 4', 'Choice 5']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Choices.objects.all().values_list('usn', 'cur_time', 'choice1', 'choice2', 'choice3', 'choice4', 'choice5')
    huh = 0
    for row in rows:
        if huh > 0:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        huh += 1

    wb.save(response)
    return response

@csrf_exempt
def changetime(request):
    hrs = request.POST.get('hrs')
    mins = request.POST.get('min')
    timer.objects.filter().delete()
    ins=timer(hrs=hrs,mins=mins)
    ins.save()
    return render(request, "electives/adexport.html")



@csrf_exempt
def uploaddata(request):
    my_usn = request.POST.get('name')
    my_sub = request.POST.get('sub')
    ins = allocated(usn=my_usn, sub=my_sub)
    ins.save()
    context = {
        'usn': my_usn,
        'sub': my_sub,
    }
    return request
