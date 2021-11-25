"""Landing views"""
from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings

def home(request):
    return render(request, 'landing/home.html')

def login_view(request):
    return render(request, 'landing/login.html')

def shipment(request):
    return render(request, 'landing/shipment.html')

def branches(request):
    return render(request, 'landing/branches.html')

def coverage(request):
    branch = request.GET.get('sucursal')
    if branch == 'ajusco':
        name = 'AJUSCO'
        address = 'Halacho esq. KinchilH. de Padierna,Tlalpan, CDMX'
        tel = '55 8791 3477'
        tel_link = '525587913477'
    if branch == 'aztecas':
        name = 'AZTECAS'
        address = 'Av. Aztecas 762, Ajusco Coyoacán, cdmx'
        tel = '55 1517 0679'
        tel_link = '525536523218'
    if branch == 'marina':
        name = 'MARINA'
        address = 'Marina Nac. 240, Anáhuac, Miguel Hidalgo, cdmx'
        tel = '55 6394 2221'
        tel_link = '525536523714'
    if branch == 'roma':
        name = 'ROMA'
        address = 'Campeche 171, Col. Roma Sur cdmx'
        tel = '55 5207 6146'
        tel_link = '525535573741'
    if branch == 'coapa':
        name = 'COAPA'
        address = 'Av. Prolongación División del Norte 4496 Prado Coapa, Tlalpan, CDMX'
        tel = '55 7259 0035'
        tel_link = '525535569825'
    return render(
        request,
        'landing/coverage.html',
        {
            "name": name,
            "address": address,
            "phone": tel,
            "phone_link": tel_link
        }
    )

def events(request):
    if request.method == 'POST':
        client_name = request.POST.get('clientname')
        phone = request.POST.get('phone')
        date_event = request.POST.get('dateevent')
        num_persons = request.POST.get('numberpersons')
        email = request.POST.get('email')
        address = request.POST.get('address')
        subject = 'Cotización evento'
        message = f"""
            Cotización de evento para:
            nombre: {client_name}
            teléfono: {phone}
            correo: {email}
            fecha de evento: {date_event}
            numero de personas: {num_persons}
            dirección: {address}
        """
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, ['eventos@elperiban.com'], fail_silently=False)
        # except BadHeaderError:
        #     print('Invalid header found.')
    return render(request, 'landing/events.html')

def employees(request):
    if request.method == 'POST':
        name = request.POST.get('nameEmployee')
        last_name = request.POST.get('lastNameEmployee')
        phone = request.POST.get('phoneEmployee')
        email = request.POST.get('emailEmployee')
        interests = request.POST.get('employeeText')
        subject = 'Formulario de empleo'
        message = f"""
            Una persona lleno el formulario de bolsa de trabajo:
            nombre: {name} {last_name}
            teléfono: {phone}
            correo: {email}
            intereses: {interests}
        """
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, ['rh@elperiban.com'], fail_silently=False)
    return render(request, 'landing/employee.html')

def medios(request):
    return render(request, 'landing/medios.html')

def invoices(request):
    if request.method == 'POST':
        name = request.POST.get('nameInvoice')
        rfc = request.POST.get('rfcInvoice')
        phone = request.POST.get('phoneInvoice')
        email = request.POST.get('emailInvoice')
        interests = request.POST.get('textInvoice')
        subject = 'Problema facturación'
        message = f"""
            Una persona indicó que tiene problemas con su facturación sus datos són:
            nombre: {name}
            rfc: {rfc}
            teléfono: {phone}
            correo: {email}
            intereses: {interests}
        """
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, ['mesadecontrol@elperiban.com'], fail_silently=False)
    return render(request, 'landing/invoices.html')

def privacy_notice(request):
    return render(request, 'landing/terms_conditions.html')