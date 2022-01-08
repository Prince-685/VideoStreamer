from django.shortcuts import render
from . import pool
def Userview(request):
    try:
        db, cmd = pool.Connectionpooling()

        q = "select * from category"
        cmd.execute(q)
        rows = cmd.fetchall()

        q="select * from display where status='Trending'"
        cmd.execute(q)
        trows=cmd.fetchall()

        q="select * from display where categoryid in(select categoryid from category where categoryname='TV Shows')"
        cmd.execute(q)
        tvrows=cmd.fetchall()
        db.close()
        return render(request, "userinterface.html", {'rows': rows, 'trows':trows, 'tvrows':tvrows})
    except Exception as e:
        print(e)
        return render(request, "userinterface.html", {'rows': []})
def Preview(request):
    row=request.GET['row']
    row=eval(row)
    db, cmd = pool.Connectionpooling()
    #Main Menu
    q = "select * from category"
    cmd.execute(q)
    rows = cmd.fetchall()
    #Movies
    q = "select * from display where categoryid=5"
    cmd.execute(q)
    movies = cmd.fetchall()

    db.close()
    return  render(request,"Preview.html",{'row': row,'rows':rows,'movies':movies})
def Tvshows(request):
    row=request.GET['row']
    row=eval(row)
    db, cmd = pool.Connectionpooling()
    #Main Menu
    q = "select * from category"
    cmd.execute(q)
    rows = cmd.fetchall()
    #Tvshows
    q = "select * from display where categoryid=7"
    cmd.execute(q)
    tvshows = cmd.fetchall()
   #Episodes
    q="select * from episodes where categoryid=7 and showid={}".format(row[1])
    cmd.execute(q)
    episodes=cmd.fetchall()
    db.close()
    return  render(request,"TvPreview.html",{'row': row,'tvshows':tvshows,'episodes':episodes})