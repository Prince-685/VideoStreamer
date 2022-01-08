from django.shortcuts import render
from . import pool
import os
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import JsonResponse
@xframe_options_exempt
def CategoryInterface(request):
    return render(request,"CategoryInterface.html")
@xframe_options_exempt
def SubmitCategory(request):
    try:
       db,cmd=pool.Connectionpooling()
       categoryname=request.POST['categoryname']
       description=request.POST['description']
       icon=request.FILES['icon']

       cmd.execute("insert into category(categoryname,description,icon) values('{0}','{1}','{2}')".format(categoryname,description,icon.name))
       db.commit()
       F=open("D:/videostrem/assets/"+icon.name,"wb")
       for chunk in icon.chunks():
           F.write(chunk)
       F.close()
       db.close()
       return render(request, "CategoryInterface.html",{'status':True})
    except Exception as e:
        print("err",e)
        return render(request, "CategoryInterface.html", {'status': False})
@xframe_options_exempt
def DisplayAllCategories(request):
    try:
        db, cmd = pool.Connectionpooling()
        q = "select * from category"
        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()
        return render(request, "displayallcategories.html", {'rows': rows})
    except Exception as e:
        return render(request, "displayallcategories.html", {'rows': []})
@xframe_options_exempt
def CategoryById(request):
    try:
        cid=request.GET['cid']
        db, cmd = pool.Connectionpooling()
        q = "select * from category where categoryid={}".format(cid)
        cmd.execute(q)
        row = cmd.fetchone()
        db.close()
        return render(request, "categorybyid.html", {'row': row})
    except Exception as e:
        return render(request, "categorybyid.html", {'row': []})
@xframe_options_exempt
def EditDeleteCategoryData(request):
  try:
     db, cmd = pool.Connectionpooling()
     btn=request.GET['btn']
     if(btn=="Edit"):
        categoryid=request.GET['categoryid']
        categoryname = request.GET['categoryname']
        description = request.GET['description']

        q = "update category set categoryname='{}', description='{}' where categoryid='{}'".format(categoryname,description,categoryid)
        cmd.execute(q)
        db.commit()
        db.close()
     elif(btn=="Delete"):
         categoryid = request.GET['categoryid']
         q = "delete from category where categoryid={}".format(categoryid)
         cmd.execute(q)
         db.commit()
         db.close()
     return render(request, "categorybyid.html", {'status':True})
  except Exception as e:
        return render(request, "categorybyid.html", {'status': False})
@xframe_options_exempt
def EditIcon(request):
    try:
       db,cmd=pool.Connectionpooling()
       categoryid = request.POST['categoryid']
       filename = request.POST['filename']
       icon=request.FILES['icon']

       cmd.execute("update category set icon='{0}' where categoryid='{1}'".format(icon.name,categoryid))
       db.commit()
       F=open("D:/videostrem/assets/"+icon.name,"wb")
       for chunk in icon.chunks():
           F.write(chunk)
       F.close()
       os.remove("D:/videostrem/assets/"+filename)
       db.close()
       return render(request, "categorybyid.html", {'status':True})
    except Exception as e:
        print("err",e)
        return render(request, "categorybyid.html", {'status': True})
@xframe_options_exempt
def DisplayAllCategoriesJSON(request):
    try:
        db, cmd = pool.Connectionpooling()
        q = "select * from category"
        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print("errr...",e)
        return JsonResponse([],safe=False)