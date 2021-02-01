from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from seln.models import Leads
from seln.utils import AutomationWhatsApp
import threading
from django.http import HttpResponse

@login_required
def panel(request):

    return render(request, 'panel.html')

@login_required
def import_contact(request):
    pass
    return render(request)

@login_required
def save_content(request):
    pass
    return render(request)


@login_required
def start_now(request):
    #set the way of save number and content
    zp_instance = threading.Thread(target=AutomationWhatsApp(content='contet', numbers=['5577998714634'], uuid_user=request.user.id).send(), daemon=True).start()
    return HttpResponse('200')

@login_required
def read_qr_code(request):
    pass
    return render(request, 'panel.html')