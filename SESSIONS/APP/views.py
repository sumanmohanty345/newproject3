from django.shortcuts import render,redirect

# Create your views here.
# def showindex(request):
#     try:
#         request.session['status']
#         return render(request,"welcome.html")
#     except KeyError:
#         return render(request,"index.html")
#
#
# def checkdata(request):
#     uname=request.POST.get('u1')
#     upass=request.POST.get('u2')
#     if uname == 'suman' and upass =='mohanty':
#         request.session['status'] = True
#         request.session.set_expiry(30)
#         return render(request,"welcome.html")
#     else:
#         return redirect('main')

def showindex(request):
    # try:
    #     #request.session['status']
    #     return render(request,"welcome.html")
    # except KeyError:
        return render(request,"index.html")

def checkdata(request):
    uname=request.POST.get('u1')
    upass=request.POST.get('u2')
    if uname=='suman' and upass=='mohanty':
        request.session['status']=True
        request.session.set_expiry(30)
        return render(request,"welcome.html")
    else:
        return redirect('main')