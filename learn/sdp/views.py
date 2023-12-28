import csv
from django.contrib.auth import authenticate, login, logout
from imp import source_from_cache
from tokenize import Name
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from .form import moviepicForm
from .models import cat, movie, music, marriage, contactf, addmovies, dcontactf, event,Item
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import datetime
def uh(request):
    if request.user.is_authenticated:
        username = request.user.username
        alle =event.objects.filter(username=username)
        # ev=cat.objects.filter(username=username)
        cont5 = {'al': alle}
        # c={'v':ev}
        return render(request, 'userhis.html', cont5)
    return redirect('/')
def dh(request):
    if request.user.is_authenticated:
        username = request.user.username
        allevents = movie.objects.filter(username=username)
        # ev=cat.objects.filter(username=username)
        context = {'al': allevents}
        # c={'v':ev}
        return render(request, 'dhistory.html', context)
    return redirect('/')
def dh1(request):
    if request.user.is_authenticated:
        username = request.user.username
        # allevent = cat.objects.filter(username=username)
        ev=cat.objects.filter(username=username)
        # contex = {'a': all}
        c={'v':ev}
        return render(request, 'dhist1.html', c)
    return redirect('/')
def dh2(request):
    if request.user.is_authenticated:
        username = request.user.username
        alls = music.objects.filter(username=username)
        # ev=cat.objects.filter(username=username)
        con = {'a': alls}
        # c={'v':ev}
        return render(request, 'dhist2.html', con)
    return redirect('/')
def dh3(request):
    if request.user.is_authenticated:
        username = request.user.username
        ells = marriage.objects.filter(username=username)
        # ev=cat.objects.filter(username=username)
        con = {'e': ells}
        # c={'v':ev}
        return render(request, 'dhist3.html', con)
    return redirect('/')

def home(request):
    return render(request,"base.html")
def contact(request):
    if request.method == 'POST':
        mail=request.POST['email']
        prob=request.POST['subject']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        c=contactf(username=username,email=mail,problem=prob)
        c.save()
    return render(request,"contact.html")
def dcontactf(request):
    if request.method == 'POST':
        mail=request.POST['email']
        prob=request.POST['subject']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        j=dcontactf(username=username,email=mail,problem=prob)
        j.save()
    return render(request,"dcontact.html")
def faqs(request):
    return render(request,"Faqs.html")
def about(request):
    return render(request,"about.html")
def login(request):
    return render(request,"newuserlogin.html")
def dlogin(request):
    return render(request,"dealerlogin.html")
def log(request):
    return render(request,"logselect.html")
def register(request):
    return render(request,"newuserregister.html")
def registerD(request):
    return render(request,"dealeregistration.html")
def base2(request):
    return render(request,"base2.html")
def logselect(request):
    return render(request,"select.html")
def music1(request):
    if request.method == 'POST':
        conname=request.POST['name1']
        nameor=request.POST['name2']
        conadd=request.POST['name3']
        city=request.POST['name4']
        zip=request.POST['name5']
        price=request.POST['name6']
        yaddress=request.POST['name7']
        ycity=request.POST['name8']
        zip=request.POST['name9']
        phno=request.POST['name10']
        email=request.POST['name11']
        print=(conadd,phno)
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        mu=music(username=username,conname=conname,nameor=nameor,conadd=conadd,city=city,zip=zip,price=price,yaddress=yaddress,ycity=ycity,yzip=zip,phno=phno,email=email)
        mu.save()
    return render(request,"Music.html")
#def movies1(request):
#    return render(request,"movies.html")
def movies(request):
    if request.method == 'POST':
        busname=request.POST['name1']
        nameuser=request.POST['name2']
        thaddress=request.POST['name3']
        c=request.POST['name4']
        z=request.POST['name5']
        pri=request.POST['name6']
        yadd=request.POST['name7']
        yc=request.POST['name8']
        yz=request.POST['name9']
        phno=request.POST['name10']
        mail=request.POST['name11']
        print(busname,nameuser,thaddress)
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        m=movie(username=username,business=busname,name=nameuser,thadd=thaddress, city=c,zip=z,price=pri, yaddress=yadd,ycity=yc, yzip=yz,phnum=phno,email=mail)
        m.save()
    return render(request,"movies.html")
# def catering(request):
#     return render(request,"catering.html")
def addmovies1(request):
    if(request.method)=='POST':
        thname=request.POST['name1']
        mname=request.POST['name2']
        gen=request.POST['name4']
        thaddress=request.POST['name3']
        c=request.POST['name8']
        z=request.POST['name9']
        username=None
        if request.user.is_authenticated:
            username=request.user.username
        am=addmovies(username=username,theatrename=thname,moviename=mname,genre=gen,theatreaddress=thaddress,city=c,zip=z)
        messages.success(request, "Movie Added Successfully")
        am.save()
    return render(request,"addmovies.html")
def marriage1(request):
    if request.method == 'POST':
        hall=request.POST['name1']
        halladd=request.POST['name2']
        city=request.POST['name3']
        zip=request.POST['name4']
        pricepe=request.POST['name5']
        capacity=request.POST['name6']
        phno=request.POST['name7']
        email=request.POST['name8']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        mr=marriage(username=username,hall1=hall,halladd1=halladd,city1=city,zip1=zip,pricepe1=pricepe,capacity1=capacity,phno1=phno,email1=email)
        mr.save()
        print(phno)

    return render(request,"marriage.html")
def userregisteruser(request):
    if  request.method == 'POST':
        fname = request.POST['fn']
        lname = request.POST['ln']
        email = request.POST['email']
        username = request.POST['uname']
        passwd = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.success(request, "Username already exists")
            return redirect('/userregisteruser')
        messages.info(request, 'Passwords dont match')
        date = datetime.date.today()
        user3 = User.objects.create_user(first_name = fname, last_name = lname, username = username , password = passwd , email = email, date_joined = date)
        user3.save()
        print('user created')
        return redirect('/login')

    return render(request,'newuserlogin.html')

def LoginOut(request):
    logout(request)
    return redirect('/login')
def Logout(request):
    logout(request)
    return redirect('/dlogin')
def userloginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user1 = auth.authenticate(username=username, password=password)
        print(username, password)
        if user1 is not None:
            auth.login(request,user1)
            return redirect('/')
        else:
            messages.error(request, "Inavalid Crendtials,Please Try Again!")
            return redirect("/login")
    else:
        return render(request,'newuserlogin.html')
def Catering(request):
    if request.method == 'POST':
        Servicename = request.POST['name']
        Name = request.POST['name1']
        PPrice = request.POST['name2']
        Capacity = request.POST['name3']
        Mobile = request.POST['name4']
        Email = request.POST['name5']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        data = cat(username=username,sname=Servicename, name=Name, pph=PPrice,capacity=Capacity,mobile=Mobile,email=Email)#, namemanu=Name1, pricemanu=PPrice, mobile=Mobile, emailmanu=Email)
        data.save()
        print(Servicename)  # ,Name1,PPrice,Mobile,Email

    return render(request, 'catering.html')
def dr(request):
    if  request.method == 'POST':
        fname = request.POST['fn']
        lname = request.POST['ln']
        email = request.POST['email']
        username = request.POST['uname']
        passwd = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.success(request, "Username already exists")
            return redirect('/dr')
        messages.info(request, 'Passwords dont match')
        date = datetime.date.today()
        user3 = User.objects.create_user(username=username,first_name = fname, last_name = lname, password = passwd , email = email, date_joined = date,is_staff=True)
        user3.save()
        print('user created')
        return redirect('/dlogin')

    return render(request,'dealerlogin.html')
@cache_control(no_cache=True,must_revalidate=True)
def dlogin(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user1 = auth.authenticate(username=username, password=password)
            print(username, password)
            if user1 is not None:
                if user1.is_staff == True:
                    auth.login(request, user1)
                    return redirect('/base2')
                # messages.info(request, 'invalid username or password')
                return redirect("/dlogin")
            else:
                messages.error(request, 'invalid credentials')
                return redirect("/dlogin")
        else:
            return render(request,'dealerlogin.html')
def cateringbook(request):
    allevent1 = cat.objects.all()
    cont1 = {'kl': allevent1}
    return render(request,'cateringbook.html',cont1)
def marriagebook(request):
    allevent2=marriage.objects.all()
    cont2={'kl1':allevent2}
    return render(request,'marriagebook.html',cont2)
def musicalbook(request):
    allevent3=music.objects.all()
    cont3={'kl2':allevent3}
    return render(request,'musicbook.html',cont3)
def moviebook1(request):
    allevent4=addmovies.objects.all()
    cont={'kl':allevent4}
    return render(request,'moviesbook.html',cont)



def fp1(request):
    c = None
    return render(request, 'fp.html')


@csrf_exempt
def fp(request):
    mail = request.POST['email']
    send_mail('Changing Password',  # subject
              'http://127.0.0.1:8000/cp/',
              'koushikpavani6@gmail.com',  # from
              [mail],  # to
              fail_silently=False,
              )

    return render(request, 'sp.html')


def cp(request):
    return render(request, 'cp.html')


@csrf_exempt
def cp1(request):
    username = request.POST['username']
    password = request.POST['Password']
    password1 = request.POST['re-enter Password']
    if password == password1:
        u = User.objects.get(username=username)
        u.set_password(password1)
        u.save()
        return redirect('/login')
    else:
        return redirect('/cp1')
def event1(request):
    if request.method=='POST':
        Typeofevent1=request.POST['tp']
        name1=request.POST['name']
        date1=request.POST['date']
        starttime1=request.POST['stime']
        endtime1=request.POST['etime']
        venue1=request.POST['venue']
        isfood1=request.POST['food']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        user19=event(username=username,Typeofevent=Typeofevent1,name=name1,date=date1,starttime=starttime1,endtime=endtime1,venue=venue1,isfood=isfood1)
        user19.save()
        messages.success(request, 'Event is Booked Successfully Please Check Mail For Details')
        msg = "Your Event has been successfully booked" + "\n\n" + "Event Name :" + Typeofevent1 + "\n" + "Name :" + name1 + "\n" + "Date :" + date1 + "\n"
        send_mail('Event Confirmation',  # subject
                   msg,
                  'outlining25@gmail.com',  # from
                  [request.user.email],  # to
                  fail_silently=False,
                  )

    return render(request,'BookingAnEvent.html',)
def deleteevent(request):
    if request.method == 'POST':
        cname = request.POST['name']
        type = request.POST['event']
        date=request.POST['date']
        if request.user.is_authenticated:
            username = request.user.username
            userdata = event.objects.filter(username=username,name=cname,Typeofevent=type,date=date)
            userdata.delete()
            messages.success(request,'Event deleted Sucessfully')
            return render(request,'cancel.html')
    if request.user.is_authenticated:
        return render(request, 'cancel.html')
    else:
        messages.error(request, "PLEASE LOGIN!")
    return redirect('/')
def movdelete(request):
    if request.method == 'POST':
        # type1 = request.POST['event']
        business1 = request.POST['Business']
        name1=request.POST['name']
        if request.user.is_authenticated:
            username = request.user.username
            userdata = movie.objects.filter(username=username,business=business1,name=name1)
            userdata.delete()
            messages.success(request,'Event deleted Sucessfully')
            return render(request,'moviedelete.html')
    if request.user.is_authenticated:
        return render(request, 'moviedelete.html')
    else:
        messages.error(request, "PLEASE LOGIN!")
    return redirect('/')
def terms(request):
    return render(request, "termsconditions.html")
def movbook(request):
    if request.method=='POST':
        Typeofevent1=request.POST['tp']
        name1=request.POST['name']
        date1=request.POST['date']
        starttime1=request.POST['stime']
        # endtime1=request.POST['etime']
        # venue1=request.POST['venue']
        isfood1=request.POST['food']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        print(Typeofevent1, name1, date1, starttime1, isfood1)
        user19=event(username=username,Typeofevent=Typeofevent1,name=name1,date=date1,starttime=starttime1,isfood=isfood1)
        user19.save()
        messages.success(request, 'Event is Booked Successfully Please Check Mail For Details')
        msg = "Your Event has been successfully booked" + "\n\n" + "Event Name :" + Typeofevent1 + "\n" + "Name :" + name1 + "\n" + "Date :" + date1 + "\n"
        send_mail('Event Confirmation',  # subject
                   msg,
                  'outlining25@gmail.com',  # from
                  [request.user.email],  # to
                  fail_silently=False,
                  )
        return render(request,'movbooking.html',)
    if request.user.is_authenticated:
        allevent4 = Item.objects.all()
        cont4 = {'il': allevent4}
        return render(request, 'movbooking.html', cont4)
    else:
        messages.success(request, "PLEASE LOGIN!")
    return redirect('/')


def musbook(request):
    if request.method=='POST':
        Typeofevent1=request.POST['tp']
        name1=request.POST['name']
        date1=request.POST['date']
        starttime1=request.POST['stime']
        # endtime1=request.POST['etime']
        # venue1=request.POST['venue']
        isfood1=request.POST['food']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        print(Typeofevent1, name1, date1, starttime1, isfood1)
        user19=event(username=username,Typeofevent=Typeofevent1,name=name1,date=date1,starttime=starttime1,isfood=isfood1)
        user19.save()
        messages.success(request, 'Event is Booked Successfully Please Check Mail For Details')
        msg = "Your Event has been successfully booked" + "\n\n" + "Event Name :" + Typeofevent1 + "\n" + "Name :" + name1 + "\n" + "Date :" + date1 + "\n"
        send_mail('Event Confirmation',  # subject
                   msg,
                  'outlining25@gmail.com',  # from
                  [request.user.email],  # to
                  fail_silently=False,
                  )
        return render(request,'musbooking.html',)
    if request.user.is_authenticated:
        allevent4 = music.objects.all()
        cont4 = {'il': allevent4}
        return render(request, 'musbooking.html', cont4)
    else:
        messages.success(request, "PLEASE LOGIN!")
    return redirect('/')
def marbook(request):
    if request.method=='POST':
        Typeofevent1=request.POST['tp']
        name1=request.POST['name']
        date1=request.POST['date']
        starttime1=request.POST['stime']
        # endtime1=request.POST['etime']
        #venue1=request.POST['venue']
        isfood1=request.POST['food']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        print(Typeofevent1,name1,date1, starttime1,isfood1)
        user19=event(username=username,Typeofevent=Typeofevent1,name=name1,date=date1,starttime=starttime1,isfood=isfood1)
        user19.save()
        messages.success(request, 'Event is Booked Successfully Please Check Mail For Details')
        msg = "Your Event has been successfully booked" + "\n\n" + "Event Name :" + Typeofevent1 + "\n" + "Name :" + name1 + "\n" + "Date :" + date1 + "\n"
        send_mail('Event Confirmation',  # subject
                   msg,
                  'outlining25@gmail.com',  # from
                  [request.user.email],  # to
                  fail_silently=False,
                  )
        messages.success(request, "Event is successfuly Booked !verify your mail")
        return render(request,'marbooking.html')
    if request.user.is_authenticated:
        allevent4 = marriage.objects.all()
        cont4 = {'il': allevent4}
        return render(request, 'marbooking.html', cont4)
    else:
        messages.success(request, "PLEASE LOGIN!")
    return redirect('/')
def catbook(request):
    if request.method=='POST':
        Typeofevent1=request.POST['tp']
        name1=request.POST['name']
        date1=request.POST['date']
        starttime1=request.POST['stime']
        # endtime1=request.POST['etime']
        # venue1=request.POST['venue']
        isfood1=request.POST['food']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        print(Typeofevent1, name1, date1, starttime1, isfood1)
        user19=event(username=username,Typeofevent=Typeofevent1,name=name1,date=date1,starttime=starttime1,isfood=isfood1)
        user19.save()
        messages.success(request, 'Event is Booked Successfully Please Check Mail For Details')
        msg = "Your Event has been successfully booked" + "\n\n" + "Event Name :" + Typeofevent1 + "\n" + "Name :" + name1 + "\n" + "Date :" + date1 + "\n"
        send_mail('Event Confirmation',  # subject
                   msg,
                  'outlining25@gmail.com',  # from
                  [request.user.email],  # to
                  fail_silently=False,
                  )
        return render(request,'catbooking.html',)
    if request.user.is_authenticated:
        allevent4 = cat.objects.all()
        cont4 = {'il': allevent4}
        return render(request, 'catbooking.html', cont4)
    else:
        messages.success(request, "PLEASE LOGIN!")
    return redirect('/')
def musdelete(request):
    if request.method == 'POST':
        # type1 = request.POST['event']
        conname1 = request.POST['conname']
        name1=request.POST['nameor']
        if request.user.is_authenticated:
            username = request.user.username
            userdata = music.objects.filter(username=username,conname=conname1,nameor=name1)
            userdata.delete()
            messages.success(request,'Event deleted Sucessfully')
            return render(request,'musicdelete.html')
    if request.user.is_authenticated:
        return render(request, 'musicdelete.html')
    else:
        messages.error(request, "PLEASE LOGIN!")
    return redirect('/')
def mardelete(request):
    if request.method == 'POST':
        # type1 = request.POST['event']
        hall = request.POST['hall1']
        halladd=request.POST['halladd1']
        if request.user.is_authenticated:
            username = request.user.username
            userdata = music.objects.filter(username=username,hall1=hall,halladd1=halladd)
            userdata.delete()
            messages.success(request,'Event deleted Sucessfully')
            return render(request,'marriagedelete.html')
    if request.user.is_authenticated:
        return render(request, 'marriagedelete.html')
    else:
        messages.error(request, "PLEASE LOGIN!")
    return redirect('/')
def catdelete(request):
    if request.method == 'POST':
        # type1 = request.POST['event']
        sname1 = request.POST['name']
        oname1=request.POST['name1']
        if request.user.is_authenticated:
            username = request.user.username
            userdata = cat.objects.filter(username=username,sname=sname1,name=oname1)
            userdata.delete()
            messages.success(request,'Event deleted Sucessfully')
            return render(request,'catdelete.html')
    if request.user.is_authenticated:
        return render(request, 'catdelete.html')
    else:
        messages.error(request, "PLEASE LOGIN!")
    return redirect('/')
def avatarView(request):
    if request.method == 'POST':
        form = moviepicForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = moviepicForm()
    return render(request, 'moviepicForm.html', {'form': form})


def uploadok(request):
    return HttpResponse(' upload successful')

def image(request):
        all = Item.objects.all()
        c = {'a': all}
        return render(request, 'moviesbook.html', c)
def addimgmovie(request):
    if request.method == "POST":
        prod = Item()
        prod.name = request.POST.get('name')
        prod.mname=request.POST.get('name1')
        prod.genre = request.POST.get('genre')
        prod.thaddress = request.POST.get('address')
        prod.capacity = request.POST.get('capacity')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']
        if len(request.FILES) != 0:
            prod.video = request.FILES['video']
        prod.save()

        messages.success(request, "Movie Added Successfully")
    return render(request, 'addimgmovie.html')


