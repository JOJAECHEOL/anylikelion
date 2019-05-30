from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def result(request):
    chitext=request.GET['firsttext']
    sp_spen=chitext.split(' ')
    mydict={}
    for i in sp_spen:
        if i in mydict:
            mydict[i]+=1
        else:
            mydict[i]=1    
    context={'textchi':chitext,'mydict':mydict,'myitem':mydict.items}
    return render(request,'result.html',context)    