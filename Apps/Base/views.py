from django.shortcuts import render, redirect, reverse, get_object_or_404
from Apps.Cni.models import *
from Apps.Cni.forms import *
from Apps.Cni.urls import *
from Apps.Cni.views import *
from Apps.Locations.models import *
from Apps.CompleteIdentity.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.urls import reverse
from Apps.Base.forms import *
from django.contrib import messages
from Apps.Admins.models import *

# Create your views here.

@login_required
def EditProfil(request,id):
	get_current_user = get_object_or_404(Profil,pk=id)
	my_profil = Profil.objects.filter(Q(user=request.user)).count()
	if my_profil < 1:
		return redirect(AddProfil)
	else:
		updateCniForm = UpdateCniForm(request.POST or None, request.FILES, instance=get_current_user)
		if request.method == "POST":
			if updateCniForm.is_valid():
				get_current_user.save()
				messages.info(request, "Votre profile est complet")
				return redirect(index)
		updateCniForm = UpdateCniForm(instance=get_current_user)
		
	return render(request, 'edit_profil.html', locals())
	
@login_required
def index(request):
	h3 = "Acceuil"
	connected_user = Profil.objects.filter(user=request.user)
	is_adm = AdminiUsers.objects.filter(user=request.user, is_area_admin=True)
	return render(request,'base.html',locals())

@login_required
def CompleteIdentityList(request):
	h3 = "Attestations"
	connected_user = request.user
	get_identity = CompleteIdentity.objects.filter(Q(beneficiary=connected_user))
	get_identity1 = CompleteIdentity.objects.filter(Q(beneficiary=connected_user)).count()
	return render(request, 'home.html', locals())

@login_required
def AllCompleteIdentityList(request):
	h3 = "Attestations"
	connected_user = request.user
	is_sta = AdminiUsers.objects.filter(Q(user=connected_user) & Q(is_area_admin=True))
	if is_sta:
		typ_admin = get_object_or_404(AdminiUsers,Q(user=connected_user) & Q(is_area_admin=True))
		get_identity_untreated = CompleteIdentity.objects.filter(Q(treated=False) & Q(area=typ_admin.area))
		get_identity_untreated_c = CompleteIdentity.objects.filter(Q(treated=False) & Q(area=typ_admin.area)).count()
		get_identity_treated = CompleteIdentity.objects.filter(Q(treated=True) & Q(area=typ_admin.area))
		get_identity_treated_c = CompleteIdentity.objects.filter(Q(treated=True) & Q(area=typ_admin.area)).count()
	else:
		return redirect(index)
	return render(request,'un-treated.html',locals())

@login_required
def ViewCompleteIdentity(request, id):
	connected_user = request.user
	get_prof1 = Profil.objects.filter(Q(user=connected_user)).count()
	get_identity = CompleteIdentity.objects.filter(Q(beneficiary=connected_user) & Q(pk=id))
	get_identity1 = CompleteIdentity.objects.filter(Q(beneficiary=connected_user) & Q(pk=id)).count()
	if get_identity1 < 1 or get_prof1 < 1:
		return redirect(AddProfil)
	else:
		get_lin = get_object_or_404(CompleteIdentity, pk = id)
		get_prof = Profil.objects.filter(Q(user=connected_user))
		treated_identity = TreatedCompleteIdentityForm(request.POST or None, request.FILES, instance=get_lin)
		
		if request.method == "POST":
			if treated_identity.is_valid():
				get_lin.save()
				messages.success(request,"Document traité!")
				return redirect(AllCompleteIdentityList)
		treated_identity = TreatedCompleteIdentityForm(instance = get_lin)
	
	return render(request,'view.html',locals()) 

def Disconnect(request):
	logout(request)
	return redirect(index)

def Connect(request):
	login_error = "hidden"
	formulaire = ConnexionForm(request.POST)
	try:
		next_p = request.GET["next"]
	except:
		next_p = ""
	if request.method == "POST" and formulaire.is_valid():
		username = formulaire.cleaned_data['username']
		password = formulaire.cleaned_data['password']
		user = authenticate(username=username, password=password)
		print(username, password)
		if user:
			login(request, user)
			messages.success(request, "You're now connected!")
			if next_p:
				return redirect(next_p)
			else:
				return redirect(index)
		else:
			messages.error(request, "Wrong password!")
	formulaire = ConnexionForm()
	return render(request, 'sign-in.html', locals())

def Inscription(request):
	if request.method == "POST" :
		form = InscriptionForm(request.POST, request.FILES)
		if form.is_valid():
			username = form.cleaned_data['username']
			firstname = form.cleaned_data['firstname']
			lastname = form.cleaned_data['lastname']
			password = form.cleaned_data['password']
			password2 = form.cleaned_data['password2']
			email = form.cleaned_data['email']
			# avatar = form.cleaned_data['avatar']
			if password==password2:
				user = User.objects.create_user(
					username=username,
					email=email,
					password=password)
				user.first_name, user.last_name = firstname, lastname
				user.save()
				# Profil(user=user, avatar=avatar).save()
				# Profil(user=user).save()
				messages.success(request, "Bienvenue chèr "+username+" !!!")
				if user:
					login(request, user)
					# return redirect(index)
					# return redirect(AddProfil)
					return redirect(Step_two)
			else:
				messages.error(request,"Envoi échoué, Vérifier le formulaire!")
	form = InscriptionForm()
	return render(request, 'inscription.html', locals())

@login_required
def Step_two(request):
    h3 = "Compléter votre profile"
    cniForm = CniForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if cniForm.is_valid():
            user = request.user
            genre = cniForm.cleaned_data['genre']
            no_identity = cniForm.cleaned_data['no_identity']
            given_place = cniForm.cleaned_data['given_place']
            birth_province = cniForm.cleaned_data['birth_province']
            birth_city = cniForm.cleaned_data['birth_city']
            birth_area = cniForm.cleaned_data['birth_area']
            birth_district = cniForm.cleaned_data['birth_district']
            birth_date = cniForm.cleaned_data['birth_date']
            father_fullname = cniForm.cleaned_data['father_fullname']
            mother_fullname = cniForm.cleaned_data['mother_fullname']
            profession = cniForm.cleaned_data['profession']
            phone_number = cniForm.cleaned_data['phone_number']
            matri_no = cniForm.cleaned_data['matri_no']
            residence_province = cniForm.cleaned_data['residence_province']
            residence_city = cniForm.cleaned_data['residence_city']
            residence_area = cniForm.cleaned_data['residence_area']
            residence_district = cniForm.cleaned_data['residence_district']
            civil_state = cniForm.cleaned_data['civil_state']
            
            Profil(user=user, genre=genre, no_identity=no_identity, given_place=given_place, \
            birth_province=birth_province, birth_city=birth_city, birth_area=birth_area,\
            birth_district=birth_district, birth_date=birth_date, father_fullname=father_fullname,\
            mother_fullname=mother_fullname, profession=profession, phone_number=phone_number,\
            matri_no=matri_no, residence_province=residence_province, residence_city=residence_city,\
            residence_area = residence_area, residence_district = residence_district, civil_state = civil_state).save()
            # messages.success(request, "Enregistrer avec success !!!")
            return redirect(index)
        else:
            messages.error(request, "Formulaire invalide !!!")
    return render(request, 'step_two.html', locals())

@login_required
def Change_password(request):
	h3 = "Paramètres"
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, 'Your password was successfully updated!')
			return redirect('home')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'change_pass.html', {
        'form': form
    })

