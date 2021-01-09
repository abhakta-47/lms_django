from django.shortcuts import render, redirect
from django.http import HttpResponse


# importing models
from base.models import *

# Create your views here.

def index(request):
    return HttpResponse("not allowed")


def contents(request,stuclass,sub):
    print()
    context = {}

    searched_stu_class = Class_list.objects.filter(stu_class=stuclass)[0]
    searched_sub = searched_stu_class.subject_set.filter(subject=sub)[0]
    searched_chapters = searched_sub.chapter_set.all()

    # print(searched_sub)
    # print(searched_chapters)
    chapters=[]
    for chapter in searched_chapters:
        chapter_={
            'chapter':chapter,
            'materails':chapter.material_set.all(),
        }
        # print(chapter_)
        chapters.append(chapter_)
    #    context["materials"].append(chapter.material_set.all())
    context={'chapters':chapters}
    print(context)

    print()
    return render(request,'index.html',context=context)
    return HttpResponse(str(stuclass)+" "+sub)


def get_iframe_url(url):
    print("\n\n")
    url=url.rpartition('/')[0]+"/preview"
    return url

def material(request, material_link):
    material_link=get_iframe_url(material_link)
    return render(request,'material.html',{'url':material_link})