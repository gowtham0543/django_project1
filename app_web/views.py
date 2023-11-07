from django.shortcuts import render

# Create your views here.
app_name = "app_web"
def home_page(request):
    # take inputs
    # initiliaze
    # process
    # send outputs
    # send information
    # send template
    # return
    context = {'page': 'My Home Page'}
    template_file = f"{app_name}/home.html"
    return render(request, template_file, context)