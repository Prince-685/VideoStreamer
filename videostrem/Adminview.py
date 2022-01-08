from django.shortcuts import render
from . import pool
def AdminLogin(request):
    return render(request,"AdminLogin.html",{'msg':""})
def Checklogin(request):
    try:
        db, cmd = pool.Connectionpooling()
        emailid = request.POST['emailid']
        password = request.POST['password']
        q="select * from adminlogin where emailid='{}' and password='{}'".format(emailid,password)
        cmd.execute(q)
        row=cmd.fetchone()
        if(row):
          return render(request, "Dashboard.html", {'row': row})
        else:
          return render(request,"AdminLogin.html",{'msg':'Please Enter a valid Emailid/Password'})
    except Exception as e:
        print("errrr",e)
        return render(request,'AdminLogin.html',{'msg':'Server Error'})