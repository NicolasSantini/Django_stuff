from django.shortcuts import render
from first_app.models import AccessRecord, User


# Create your views here.
def index(request):
    index_dict = {'insert_index': "this is the index page and there's an index"}
    return render(request, 'first_app/index.html', context=index_dict)


def help(request):
    help_dict = {'insert_help': "this is the help page and there's an help"}
    return render(request, 'first_app/help.html', context=help_dict)


def webpages(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/webpages.html', context=date_dict)


def users(request):
    users_list = User.objects.order_by('first_name')
    user_dict = {'users_records': users_list}
    return render(request, 'first_app/users.html', context=user_dict)
