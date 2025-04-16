import pathlib
from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "Welcome to DataDude"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "total_visit_count": qs.count()
    }
    
    html_template = "home.html"
    
    PageVisit.objects.create(path = request.path)
    return render(request, html_template, my_context)

def old_home_page_view(request, *args, **kwargs):
    my_title = "My demo landing page"
    my_context = {
        "page_title": my_title,
        "content": "Welcome to my demo landing page",
        "content2": "This is a test",
        "content3": "This is another test",
    }
    html_ = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{page_title}</title>

            </head>
            <body>
            <header>
                    <h1>Welcome to My Website</h1>
            </header>

            <main>
                
                <p>This is where you can put your content.</p>
            </main>

            <footer>
                
                <p>&copy; 2025 Your Name or Company</p>
            </footer>

            </body>
            </html>
        """.format(**my_context)
    
    html_file_path = this_dir / "home.html"
    html_ = html_file_path.read_text()
    return HttpResponse(html_)

