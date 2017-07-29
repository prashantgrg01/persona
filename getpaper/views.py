from django.shortcuts import render
from .paperman import PaperManager

# Create your views here.
def index(request):
    if request.method == "POST":
        # get the values from the form fields
        code = request.POST.get("code", "")
        year = request.POST.get("year", "")
        session = request.POST.get("session", "")
        paper_type = request.POST.get("paper_type", "")
        paper_num = request.POST.get("paper_num", "")

        # save them in a list of fields
        fields = [code, year, session, paper_type, paper_num]

        # create new PaperManager
        pm = PaperManager(code, year, session, paper_type, paper_num)
        # get the list of subject_links
        subject_links = pm.get_subject_links()
        # use subject_links to get the list of paper_links
        paper_links = pm.get_paper_links(subject_links)

        # render view with paper_links and fields
        return render(request, "getpaper/index.html", {"links": paper_links, "fields": fields})
    else:
        # Handle GET request
        # render home view with empty form
        return render(request, "getpaper/index.html", {})