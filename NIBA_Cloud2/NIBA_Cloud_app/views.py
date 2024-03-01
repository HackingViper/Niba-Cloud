from django.shortcuts import render
from NIBA_Cloud_app.models import section, dossier


def login(request):
    return render(request, "login.html")

def acceuil(request):
    
    return render(request, "acceuil.html")


def archives(request,slug):

    '''search_doc =""
    requete = request.GET.get('requete')
    if not requete:
        pass
    else:	
    	search_doc = dossier.objects.filter(section_name__slug=slug, name__icontains=requete)
    '''

    section_list = section.objects.all()
    
    section_doc = dossier.objects.filter(section_name__slug=slug)
    context = {
		'section': section_list,
        'section_doc': section_doc,
		}

    return render(request, 'archives.html', context)