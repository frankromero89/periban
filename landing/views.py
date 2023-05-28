"""Landing views"""
import pwd
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from typing import List, cast
from django.db.models import Count

from landing.forms import ImageForm, ImageTicketForm
from landing.models import Form_type, Question_form, answer_form, image_evidence, promedy_form

def home(request):
    return render(request, 'landing/home.html')

def login_view(request):
    if request.method == 'POST':
        user_name = request.POST.get('userName')
        pswd = request.POST.get('userPassword')
        user = authenticate(request, username=user_name,password=pswd)
        if user:
            login(request, user)
            return redirect('form_list')
        else:
           return render(request, 'landing/login.html', {'error': True}) 
    return render(request, 'landing/login.html')

def logout_view(request):
    """Logout user"""
    logout(request)
    return redirect('home')

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
        email = 'ajusco@elperiban.com'
        tel_link = '525587913477'
    if branch == 'aztecas':
        name = 'AZTECAS'
        address = 'Av. Aztecas 762, Ajusco Coyoacán, cdmx'
        tel = '55 1517 0679'
        email = 'aztecas@elperiban.com'
        tel_link = '525536523218'
    if branch == 'marina':
        name = 'MARINA'
        address = 'Marina Nac. 240, Anáhuac, Miguel Hidalgo, cdmx'
        tel = '55 6394 2221'
        email = 'marina@elperiban.com'
        tel_link = '525536523714'
    if branch == 'roma':
        name = 'ROMA'
        address = 'Campeche 171, Col. Roma Sur cdmx'
        tel = '56 3332 1629'
        email = 'roma@elperiban.com'
        tel_link = '525633321629'
    if branch == 'coapa':
        name = 'COAPA'
        address = 'Av. Prolongación División del Norte 4496 Prado Coapa, Tlalpan, CDMX'
        tel = '55 7259 0035'
        email = 'coapa@elperiban.com'
        tel_link = '525535569825'
    if branch == 'cafetales':
        name = 'CAFETALES'
        address = 'V. de la Armada 1405 Col. Residencial Cafetales del Coyoacán, CDMX'
        tel = '55 3559 4524'
        email = 'cafetales@elperiban.com'
        tel_link = '525535594524'
    if branch == 'ayuntamiento':
        name = 'AYUNTAMIENTO'
        address = 'Ayuntamiento 87 Local D, Barrio la Lonja, Tlalpan, CDMX'
        tel = '55 3652 3050'
        email = 'ayuntamiento@elperiban.com'
        tel_link = '525536523050'
    return render(
        request,
        'landing/coverage.html',
        {
            "name": name,
            "address": address,
            "phone": tel,
            "email": email,
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
        interests = request.POST.get('vacancy')
        subject = 'Formulario de empleo'
        message = f"""
            Una persona lleno el formulario de bolsa de trabajo:
            nombre: {name} {last_name}
            teléfono: {phone}
            intereses: {interests}
        """
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, ['rh@elperiban.com'], fail_silently=False)
    return render(request, 'landing/employee.html')

def medios(request):
    return render(request, 'landing/medios.html')

@login_required
def forms_list(request):
    forms = Form_type.objects.all()
    forms_answer = answer_form.objects.values('form_id', 'form_type__form_id', 'form_type__form_name', 'created').annotate(dcount=Count('form_id'))
    # import pdb; pdb.set_trace()
    return render(request, 'landing/forms_list.html', {
        'forms': forms,
        'forms_answers': forms_answer
    })

@login_required
def form_view(request, form):
    if request.method == 'POST':
        answer_row = answer_form.objects.all().last()
        form_type = Form_type.objects.get(form_id=form)
        last_form = answer_row.form_id + 1 if answer_row else 1
        form_image = ImageForm(request.POST, request.FILES)
        checks = {}
        total_promedy = 0
        ####variables for email###
        body_email = ''
        email_destination = ''
        for i, qst_answer in request.POST.items():
            if i != 'csrfmiddlewaretoken' and i != 'imageEvidence' and i != 'form_id': 
                if len(i) > 1:
                    name_option=i.split("-")
                    checks[name_option[0]] = f'{checks[name_option[0]]};{qst_answer}' if checks.get(name_option[0]) else qst_answer
                else:
                    question = Question_form.objects.get(question_id=i)
                    if question.value_points > 0 and cast(str, qst_answer.lower()) == 'si':
                        total_promedy += question.value_points
                    answer = answer_form(
                        form_id=last_form,
                        form_type=form_type,
                        question_id=question,
                        answer=qst_answer,
                        answer_by=request.user
                    )
                    answer.save()
                    
                    #Data for email
                    if question.question_description == 'Sucursales':
                        email_destination = f"{answer.answer}@elperiban.com"
                    body_email = body_email + f"""
                        - {question.question_description}: {answer.answer}
                    """
        print(f'****total promedy: {total_promedy}')
        if len(checks) > 0:
            for i, check in checks.items():
                question = Question_form.objects.get(question_id=i)
                answer = answer_form(
                    form_id=last_form,
                    form_type=form_type,
                    question_id=question,
                    answer=check,
                    answer_by=request.user
                )
                answer.save()
                body_email = body_email + f"""
                    - {question.question_description}: {answer.answer}
                """
        if total_promedy > 0:
            promedy = promedy_form(
                form_id=last_form,
                promedy_form= total_promedy
            )
            promedy.save()
        form_image.save(last_form)
        """Send email with answers to branch"""
        subject = 'Respuestas formulario'
        email_from = settings.EMAIL_HOST_USER
        # send_mail(subject, body_email, email_from, [email_destination], fail_silently=False)
        return redirect('form_list')

    form_questions = Question_form.objects.filter(form_type__form_id=form)
    questions = []
    form_image = ImageForm()
    for qst in form_questions:
        options_list = qst.options.split(';') if qst.options else []
        questions.append({
            'id': qst.question_id,
            'label': qst.question_description,
            'is_options': qst.is_options,
            'is_check': qst.is_check,
            'options': {
                i : options_list[i] for i in range(len(options_list))
            }
        })
    return render(request, 'landing/forms_list.html', {
        'questions': questions,
        'form': form_questions[0].form_type,
        'image_form': form_image
    })

def form_answers(request, form):
    answers = answer_form.objects.filter(form_id=form)
    evidence = image_evidence.objects.get(form_id=form)
    promedy = promedy_form.objects.get(form_id=form)
    return render(request, 'landing/forms_list.html', {
        'answers': answers,
        'evidence': evidence,
        'date': answers[0].created,
        'form_type': answers[0].form_type.form_name,
        'applied': answers[0].answer_by,
        'promedy': promedy
    })    

def invoices(request):
    if request.method == 'POST':
        ticket_image = ImageTicketForm(request.POST, request.FILES)
        if not ticket_image.is_valid():
            print(f"***errors: {ticket_image.errors}")
        name = request.POST.get('nameInvoice')
        branch = request.POST.get('branchInvoice')
        rfc = request.POST.get('rfcInvoice')
        ticket_num = request.POST.get('ticketNum')
        payment_method = request.POST.get('paymentMethod')
        ticket_amount = request.POST.get('ticketAmount')
        phone = request.POST.get('phoneInvoice')
        email = request.POST.get('emailInvoice')
        interests = request.POST.get('textInvoice')
        subject = 'Problema facturación'
        message = f"""
            Una persona indicó que tiene problemas con su facturación sus datos són:
            nombre: {name}
            sucursal: {branch}
            rfc: {rfc}
            numero de ticket: {ticket_num}
            metodo de pago: {payment_method}
            monto del ticket: {ticket_amount}
            teléfono: {phone}
            correo: {email}
            intereses: {interests}
        """
        email_from = settings.EMAIL_HOST_USER
        branch_email = f'{branch}@elperiban.com'
        admin_email = f'{branch}.periban@gmail.com' if branch != 'marina' else f'{branch}240.periban@gmail.com' 
        send_mail(subject, message, email_from, [branch_email, admin_email], fail_silently=False)
        ticket_image.save(request.POST.get('nameInvoice'))
    return render(request, 'landing/invoices.html')

def privacy_notice(request):
    return render(request, 'landing/terms_conditions.html')

def presentation_card_01(request, user_id):
    users = {
        "1": {
            "name": "Miriam",
            "last_name": "Baldovinos",
            "position": "Dirección Administrativa",
            "email": "miriam@elperiban.com",
            "phone": "55 4343 3165",
            "waphone": "5543433165"
        },
        "2": {
            "name": "Norma Rosales",
            "last_name": "Rosales",
            "position": "Gerente de Marketing",
            "email": "mkt@elperiban.com",
            "phone": "56 1205 44 08",
            "waphone": "525612054408"
        }
    }
    user_data = users.get(user_id, None)
    return render(request, 'landing/pres_card.html', {'user_data': user_data})