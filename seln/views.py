from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from seln.models import Leads

@login_required
def panel(request):
    pass
    return render(request, 'panel.html')

@login_required
def import_contact(request):
    pass
    return render(request)


@login_required
def read_qr_code(request):
    pass
    return render(request, 'panel.html')