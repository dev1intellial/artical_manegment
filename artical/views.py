from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Artical,Artical_Tag,Tag
from .forms import ArticalTageForm,ArticalForm


def articals(request):
    artical=Artical_Tag.objects.filter(artical__draf=False)
    # print(artical)
    master_tag=list(Tag.objects.values_list('tags',flat=True))
    # print(master_tag)
    tags=list(Artical_Tag.objects.filter(artical__draf=False).values_list('tag',flat=True))
    a=' '.join(tags)
    b=a.split(' ')
    count_tag=[]
    for i in master_tag:
        # print(i)
        x=b.count(i)
        z=count_tag.append(x)
    count_all_tag=dict(zip(master_tag,count_tag))
    return render(request,'artical.html',{'artical':artical,'count_tag':count_tag,'master_tag':master_tag,'count_all_tag':count_all_tag})


@login_required(login_url='login')
def artical_save(request):
    artical=Artical_Tag.objects.filter(artical__draf=True).filter(artical__user_name=request.user)
    return render(request,'articalsavedraf.html',{'artical':artical})


@login_required(login_url='login')
def artical_tag(request,id=None):
    if id == 0:
        form=ArticalForm()
        form2=ArticalTageForm()
        text=request.POST.get('tag')
        if request.method=='POST':

            if 'savedraf' in request.POST :
                d=True
            elif 'publish' in request.POST:
                d=False
                if text:
                    mastertag = text.split(",")
                    mastertag_tags= list(Tag.objects.filter(tags__in=mastertag).values_list('tags',flat=True))
                    for j in mastertag:
                        if j in mastertag_tags:
                            # print(j)
                            mastertag.remove(j)
                    # print(mastertag)
                    if len(mastertag)>1:
                        for s in mastertag:
                            mastertag=Tag.objects.create(tags=s)
                            mastertag.save()
            
            if text:
                tag=text.split(",")
                a=' '.join(tag)
                
            form=ArticalForm(request.POST,request.FILES,)
            form2=ArticalTageForm(request.POST,)
            if form.is_valid or form2.is_valid():
                form=form.save(commit=False)
                form2=form2.save(commit=False)
                form.user_name=request.user
                

                form.draf=d
                # print(form)

                form2.artical=form
                form2.tag=a
                form.save()
                form2.save()
            
                return redirect('artical')
    else:
        artical=Artical.objects.get(pk=id)
        artical_tag=Artical_Tag.objects.get(pk=id)
        text=request.POST.get('tag')
        # print(text,'****************************')
        form=ArticalForm(instance=artical)
        form2=ArticalTageForm(instance=artical_tag)
        if request.method =='POST':
            if 'savedraf' in request.POST:
                d=True
            elif 'publish' in request.POST:
                d=False
                if text:
                    mastertag = text.split(",")
                    mastertag_tags= list(Tag.objects.filter(tags__in=mastertag).values_list('tags',flat=True))
                    for j in mastertag:
                        if j in mastertag_tags:
                            # print(j)
                            mastertag.remove(j)
                    if len(mastertag)>1:
                        for s in mastertag:
                            mastertag=Tag.objects.create(tags=s)
                            mastertag.save()

                if text:
                    tag=text.split(",")
                    a=' '.join(tag)
            form=ArticalForm(request.POST,request.FILES,instance=artical)
            form2=ArticalTageForm(request.POST,instance=artical_tag)
            if form.is_valid or form2.is_valid():
                form=form.save(commit=False)
                form2=form2.save(commit=False)
                form.draf=d
                # print(form)
                form2.artical=form
                form2.tag=a
            
                form.save()
                form2.save()
            
                return redirect('artical')
    return render(request,'articaltag.html',{'form':form,'form2':form2})
    
@login_required(login_url='login')
def artical_delete(request,id):
    # print(id)
    artical=Artical.objects.get(pk=id)
    if request.method=='POST':
        artical.delete()
        return redirect('artical')
    return render(request,'articaldelete.html')
    

def artical_find(request,cont_tag):
    artical=Artical_Tag.objects.filter(tag__icontains=cont_tag).filter(artical__draf=False)
    return render(request,'articalfind.html',{'artical':artical})
