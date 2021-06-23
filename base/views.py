from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MaterialForm, ChapterForm

# importing models
from base.models import Class_list, Chapter

# Create your views here.


def index(request):
    return HttpResponse("not allowed")


def contents(request, stuclass, sub):
    print()
    context = {}

    searched_stu_class = Class_list.objects.filter(stu_class=stuclass)[0]
    searched_sub = searched_stu_class.subject_set.filter(subject_code=sub)[0]
    searched_chapters = searched_sub.chapter_set.all()

    # print(searched_sub)
    # print(searched_chapters)
    chapters = []
    for chapter in searched_chapters:
        chapter_ = {
            'chapter': chapter,
            'chapter_id': chapter.id,
            'materials': chapter.material_set.all(),
        }
        # print(chapter_)
        chapters.append(chapter_)
    #    context["materials"].append(chapter.material_set.all())
    context = {'chapters': chapters}
    context['class'] = searched_stu_class.stu_class
    context['subject_name'] = searched_sub.subject_name
    context['subject_code'] = searched_sub.subject_code
    context['form'] = MaterialForm()
    context['add_chapter_form'] = ChapterForm()
    # print(context)

    # print()
    return render(request, 'index.html', context=context)
    return HttpResponse(str(stuclass)+" "+sub)


def add_chapter(request, stuclass, sub):
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid:
            searched_stu_class = Class_list.objects.filter(
                stu_class=stuclass)[0]
            # searched_sub = searched_stu_class.subject_set.filter(
            # subject_code=sub)[0]
            new_chapter = form.save(commit=False)
            new_chapter.subject = searched_stu_class.subject_set.get(
                subject_code=sub)
            new_chapter.save()
            return redirect('sub_contents', stuclass, sub)
        else:
            return HttpResponse("invalid input")
    else:
        return HttpResponse("not allowed")


def chapter(request, stuclass, sub, chapter):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        # print(stuclass, sub, chapter)
        if form.is_valid():
            new_material = form.save(commit=False)
            new_material.chapter = Chapter.objects.get(id=chapter)
            new_material.save()
            # searched_chapters.material_set.add(new_material)

            return redirect('sub_contents', stuclass, sub)
        else:
            return HttpResponse('invalid input')

    return HttpResponse("no allowed")


def get_iframe_url(url):
    print("\n\n")
    url = url.rpartition('/')[0]+"/preview"
    return url


def material(request, material_link):

    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            # print(from)
            return HttpResponse('hei')
        else:
            return HttpResponse('invalid input')

    material_link = get_iframe_url(material_link)
    return render(request, 'material.html', {'url': material_link})
