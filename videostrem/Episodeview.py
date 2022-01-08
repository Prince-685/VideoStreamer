from django.shortcuts import render
from . import pool
from django.views.decorators.clickjacking import xframe_options_exempt
import os
@xframe_options_exempt
def Episode(request):
    return render(request,"Episode.html")
@xframe_options_exempt
def Submitepisode(request):
    try:
        db, cmd = pool.Connectionpooling()
        categoryid = request.POST['categoryid']
        showid = request.POST['showid']
        episodenumber=request.POST['episodenumber']
        description =request.POST['description']
        poster = request.FILES['poster']
        trailer = request.FILES['trailer']
        video = request.FILES['video']

        cmd.execute("insert into episodes(categoryid,showid,episodenumber,description,poster,trailer,video) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(categoryid,showid,episodenumber,description,poster.name,trailer.name,video.name))
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
        return render(request, "Episode.html", {'status': True})
    except Exception as e:
        print("err", e)
        return render(request, "Episode.html", {'status': False})
@xframe_options_exempt
def DisplayAllEpisodes(request):
    try:
        db, cmd = pool.Connectionpooling()
        q = "select E.*,(select C.categoryname from category C where C.categoryid=E.categoryid),(select S.showname from display S where S.showid=E.showid) from episodes E"
        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()
        return render(request, "displayepisodes.html", {'rows': rows})
    except Exception as e:
        print('errrrrrr', e)
        return render(request, "displayepisodes.html", {'rows': []})
@xframe_options_exempt
def EpisodeById(request):
    try:
        db, cmd = pool.Connectionpooling()
        eid = request.GET['eid']
        q = "select * from episodes where episodeid='{}'".format(eid)
        cmd.execute(q)
        row = cmd.fetchone()
        db.close()
        return render(request, "episodebyid.html", {'row': row})
    except Exception as e:
        print(e)
        return render(request, "episodebyid.html", {'row': []})
@xframe_options_exempt
def EditDeleteEpisodeData(request):

  try:
     db, cmd = pool.Connectionpooling()
     btn=request.GET['btn']
     episodeid = request.GET['episodeid']
     if(btn=="Edit"):

         categoryid = request.GET['categoryid']
         showid=request.GET['showid']

         episodenumber = request.GET['episodenumber']
         description = request.GET['description']

         q = "update episodes set categoryid='{}',showid='{}',episodenumber='{}',description='{}' where episodeid='{}'".format(categoryid,showid,episodenumber,description,episodeid)
         cmd.execute(q)
         db.commit()
         db.close()
     elif(btn=="Delete"):

         db, cmd = pool.Connectionpooling()
         q = "delete from episodes where episodeid='{}'".format(episodeid)
         cmd.execute(q)
         db.commit()
         db.close()
     return render(request, "episodebyid.html", {'status':True})
  except Exception as e:
        print('erreeee',e)
        return render(request, "episodebyid.html", {'status': False})
@xframe_options_exempt
def Editposter(request):
    try:
       db,cmd=pool.Connectionpooling()
       episodeid = request.POST['episodeid']
       postername = request.POST['postername']
       poster=request.FILES['poster']

       cmd.execute("update episodes set poster='{0}' where episodeid='{1}'".format(poster.name,episodeid))
       db.commit()
       F=open("D:/videostrem/assets/"+poster.name,"wb")
       for chunk in poster.chunks():
           F.write(chunk)
       F.close()
       os.remove("D:/videostrem/assets/"+postername)
       db.close()
       return render(request, "episodebyid.html", {'status':True})
    except Exception as e:
        print("err",e)
        return render(request, "episodebyid.html", {'status': True})
@xframe_options_exempt
def Edittrailer(request):
    try:
       db,cmd=pool.Connectionpooling()
       episodeid = request.POST['episodeid']
       trailername = request.POST['trailername']
       trailer=request.FILES['trailer']

       cmd.execute("update episodes set trailer='{0}' where showid='{1}'".format(trailer.name,episodeid))
       db.commit()
       F=open("D:/videostrem/assets/"+trailer.name,"wb")
       for chunk in trailer.chunks():
           F.write(chunk)
       F.close()
       os.remove("D:/videostrem/assets/"+trailername)
       db.close()
       return render(request, "episodebyid.html", {'status':True})
    except Exception as e:
        print("err",e)
        return render(request, "episodebyid.html", {'status': True})
@xframe_options_exempt
def Editvideo(request):
    try:
       db,cmd=pool.Connectionpooling()
       episodeid = request.POST['episodeid']
       videoname = request.POST['videoname']
       video=request.FILES['video']

       cmd.execute("update episodes set video='{0}' where episodeid='{1}'".format(video.name,episodeid))
       db.commit()
       F=open("D:/videostrem/assets/"+video.name,"wb")
       for chunk in video.chunks():
           F.write(chunk)
       F.close()
       os.remove("D:/videostrem/assets/"+videoname)
       db.close()
       return render(request, "episodebyid.html", {'status':True})
    except Exception as e:
        print("err",e)
        return render(request, "episodebyid.html", {'status': True})