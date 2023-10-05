from courses.models import Course

def menu_links(request):
    links=Course.objects.all()
    return {'links':links}