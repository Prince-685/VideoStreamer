from django.shortcuts import render
from . import pool
from django.views.decorators.clickjacking import xframe_options_exempt
import os
from django.http import JsonResponse
@xframe_options_exempt
def ShowCategory(request):
    return render(request,"Show.html")
@xframe_options_exempt
def Submit(request):
    try:
        db, cmd = pool.Connectionpooling()
        categoryid = request.POST['categoryid']
        showname = request.POST['showname']
        type=request.POST['type']
        description =request.POST['description']
        year =request.POST['year']
        rating =request.POST['rating']
        artists =request.POST['artists']
        status =request.POST['status']
        showstatus =request.POST['showstatus']
        episodes =request.POST['episodes']
        poster = request.FILES['poster']
        trailer = request.FILES['trailer']
        video = request.FILES['video']

        cmd.execute("insert into display(categoryid,showname,type,description,year,rating,artists,status,showstatus,episodes,poster,trailer,video) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')".format(categoryid,showname,type,description,year,rating,artists,status,showstatus,episodes,poster.name,trailer.name,video.name))
        db.commit()
        F = open("D:/videostrem/assets/" + poster.name, "wb")
        for chunk in poster.chunks():
            F.write(chunk)
        F.close()
        F = open("D:/videostrem/assets/" + trailer.name, "wb")
        for chunk in trailer.chunks():
            F.write(chunk)
        F.close()
        F = open("D:/videostrem/assets/" + video.name, "wb")
        for chunk in video.chunks():
            F.write(chunk)
        F.close()
        db.close()
        return render(request, "Show.html", {'status': True})
    except Exception as e:
        print("err", e)
        return render(request, "Show.html", {'status': False})
@xframe_options_exempt
def DisplayAllShows(request):
    try:
        db, cmd = pool.Connectionpooling()
        q = "select S.*,(select C.categoryname from category C where C.categoryid=S.categoryid) from display S"
        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()
        return render(request, "display.html", {'rows': rows})
    except Exception as e:
        print('errrrrrr',e)
        return render(request, "display.html", {'rows': []})
@xframe_options_exempt
def ShowById(request):
    try:
        sid=request.GET['sid']
        db, cmd = pool.Connectionpooling()
        q = "select S.*,(select C.categoryname from category C where C.categoryid=S.categoryid) from display S where S.showid='{}'".format(sid)
        cmd.execute(q)
        row = cmd.fetchone()
        db.close()
        return render(request, "showbyid.html", {'row': row})
    except Exception as e:
        return render(request, "showbyid.html", {'row': []})
@xframe_options_exempt
def EditDeleteShowData(request):

  try:
     db, cmd = pool.Connectionpooling()
     btn=request.GET['btn']
     if(btn=="Edit"):
         categoryid = request.GET['categoryid']
         showid=request.GET['showid']
         showname = request.GET['showname']
         type = request.GET['type']
         description = request.GET['description']
         year = request.GET['year']
         rating = request.GET['rating']
         artists = request.GET['artists']
         status = request.GET['status']
         showstatus = request.GET['showstatus']
         episodes = request.GET['episodes']

         q = "update display set categoryid='{}',showname='{}',type='{}',description='{}',year='{}',rating='{}',artists='{}',status='{}',showstatus='{}',episodes='{}' where showid='{}'".format(categoryid,showname,type,description,year,rating,artists,status,showstatus,episodes,showid)
         cmd.execute(q)
         db.commit()
         db.close()
     elif(btn=="Delete"):
         showid = request.GET['showid']
         db, cmd = pool.Connectionpooling()
         q = "delete from display where showid='{}'".format(showid)
         cmd.execute(q)
         db.commit()
         db.close()
     return render(request, "showbyid.html", {'status':True})
  except Exception as e:
        print('erreeee',e)
        return render(request, "showbyid.html", {'status': False})
@xframe_options_exempt
def Editposter(request):
    try:
       db,cmd=pool.Connectionpooling()
       showid = request.POST['showid']
       postername = request.POST['postername']
       poster=request.FILES['poster']

       cmd.execute("update display set poster='{0}' where showid='{1}'".format(poster.name,showid))
       db.commit()
       F=open("D:/videostrem/assets/"+poster.name,"wb")
       for chunk in poster.chunks():
           F.write(chunk)
       F.close()
       os.remove("D:/videostrem/assets/"+postername)
       db.close()
       return render(request, "showbyid.html", {'status':True})
    except Exception as e:
        print("err",e)
        return render(request, "showbyid.html", {'status': True})
@xframe_options_exempt
def Edittrailer(request):
    try:
       db,cmd=pool.Connectionpooling()
       showid = request.POST['showid']
       trailername = request.POST['trailername']
       trailer=request.FILES['trailer']

       cmd.execute("update display set trailer='{0}' where showid='{1}'".format(trailer.name,showid))
       db.commit()
       F=open("D:/videostrem/assets/"+trailer.name,"wb")
       for chunk in trailer.chunks():
           F.write(chunk)
       F.close()
       os.remove("D:/videostrem/assets/"+trailername)
       db.close()
       return render(request, "showbyid.html", {'status':True})
    except Exception as e:
        print("err",e)
        return render(request, "showbyid.html", {'status': True})
@xframe_options_exempt
def Editvideo(request):
    try:
       db,cmd=pool.Connectionpooling()
       showid = request.POST['showid']
       videoname = request.POST['videoname']
       video=request.FILES['video']

       cmd.execute("update display set video='{0}' where showid='{1}'".format(video.name,showid))
       db.commit()
       F=open("D:/videostrem/assets/"+video.name,"wb")
       for chunk in video.chunks():
           F.write(chunk)
       F.close()
       os.remove("D:/videostrem/assets/"+videoname)
       db.close()
       return render(request, "showbyid.html", {'status':True})
    except Exception as e:
        print("err",e)
        return render(request, "showbyid.html", {'status': True})
@xframe_options_exempt
def DisplayAllShowJSON(request):
    try:
        cid=request.GET["cid"]
        db, cmd = pool.Connectionpooling()
        q = "select * from display where categoryid={}".format(cid)
        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        return JsonResponse([],safe=False)