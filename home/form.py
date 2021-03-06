from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from . import models


class kdeform(forms.Form):
    myRadius = forms.DecimalField(widget=forms.NumberInput(attrs={'min': '0', 'step': '1', 'value': '15'}))
    myOpacity = forms.DecimalField(widget=forms.NumberInput(attrs={'min': '0', 'step': '0.1', 'value': '0.8'}))


class clusteringform(forms.Form):
    # silhouette = forms.DecimalField(label='Coefficient de Silhouette', disabled=True, widget=forms.NumberInput)
    # inxch = forms.DecimalField(label='Indice CH', disabled=True)
    myEpsilon = forms.DecimalField(label='Epsilon', min_value=0,
                                   widget=forms.NumberInput(attrs={'min': '0', 'step': '0.01', 'value': '0.02'}))
    myMinPts = forms.DecimalField(label='minPts ', min_value=0,
                                  widget=forms.NumberInput(attrs={'min': '0', 'step': '1', 'value': '4'}))


class wilaya(forms.Form):
    options = [
        ('--', '--'), ('adrar', 'adrar'), ('ain defla', 'ain defla'), ('ain temouchent', 'ain temouchent'),
        ('alger', 'alger'), ('annaba', 'annaba'),
        ('bachar', 'bachar'), ('batna', 'batna'), ('bejaia', 'bejaia'), ('biskra', 'biskra'), ('blida', 'blida'),
        ('bouira', 'bouira'), ('boumerdes', 'boumerdes'), ('chlef', 'chlef'),
        ('constantine', 'constantine'), ('djelfa', 'djelfa'), ('el bayadh', 'el bayadh'), ('el oued', 'el oued'),
        ('el tarf', 'el tarf'),
        ('ghardaia', 'ghardaia'), ('guelma', 'guelma'), ('illizi', 'illizi'), ('jijel', 'jijel'),
        ('khenchela', 'khenchela'), ('laghouat', 'laghouat'),
        ('mascara', 'mascara'), ('medea', 'medea'), ('mila', 'mila'), ('mostaganem', 'mostaganem'), ('msila', 'msila'),
        ('naama', 'naama'), ('oran', 'oran'),
        ('ouargla', 'ouargla'), ('oum el bouaghi', 'oum el bouaghi'), ('relizane', 'relizane'), ('saida', 'saida'),
        ('setif', 'setif'),
        ('sidi bel abbes', 'sidi bel abbes'), ('skikda', 'skikda'), ('souk ahras', 'souk ahras'),
        ('tamanrasset', 'tamanrasset'), ('tebessa', 'tebessa'),
        ('tiaret', 'tiaret'), ('.', 'tindouf'), ('tipaza', 'tipaza'), ('tissemsilt', 'tissemsilt'),
        ('tizi ouzou', 'tizi ouzou'),
        ('tlemcen', 'tlemcen'),
    ]
    wilaya = forms.CharField(widget=forms.Select(choices=options,
                                                 attrs={'empty_value': "Toutes les wilayas", 'width': '200',
                                                        'id': 'mywilaya'}), initial="--")


class makefilter(forms.Form):
    causes = [('--', '--'), ]
    routes = [('--', '--'), ]

    cause = forms.CharField(label='Cause', required=False, widget=forms.Select(choices=causes))
    route = forms.CharField(label='Type de route', required=False, widget=forms.Select(choices=routes))


class authentif(forms.Form):
    comptes = [
        ('--', '--'),
        ("décideur", "Compte décideur"),
        ("admin", "Compte admin")
    ]
    user = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': "Nome d'utilisateur"}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Mot de passe"}), required=True, label="")
    # pwd =forms.CharField(label="Mot de passe", required=True)
    # compte =forms.CharField(label='Type de compte', required=True, widget=forms.Select(choices=comptes))


class intervalledate(forms.Form):
    debut = forms.DateField(label='Du', widget=forms.DateInput(
        attrs={'type': 'date', 'min': '2014-01-01', 'max': '2014-03-30', 'value': '2014-01-01'}))
    fin = forms.DateField(label='Au', widget=forms.DateInput(
        attrs={'type': 'date', 'min': '2014-01-02', 'max': '2014-03-31', 'value': '2014-03-31'}))
class intervalledate2(forms.Form):
    debutPred = forms.DateField(label='Du', widget=forms.DateInput(
        attrs={'type': 'date', 'min': '2014-01-01', 'max': '2014-03-30', 'value': '2014-01-01'}))
    finPred = forms.DateField(label='Au', widget=forms.DateInput(
        attrs={'type': 'date', 'min': '2014-01-02', 'max': '2014-03-31', 'value': '2014-03-31'}))
class intervalledate3(forms.Form):
    debutPred = forms.DateField(label='Du', widget=forms.DateInput(
        attrs={'type': 'date', 'min': '2014-01-01', 'value': '2014-03-31'}))
    finPred = forms.DateField(label='Au', widget=forms.DateInput(
        attrs={'type': 'date', 'min': '2014-01-02', 'value': '2014-03-31'}))
class savePred(forms.Form):
    user = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': "Nome d'utilisateur"}))

class uploadFiles(forms.Form):
    file_field = forms.FileField(label='Sélectionner un fichier',
                                 widget=forms.ClearableFileInput(attrs={'multiple': True, 'lang': 'fr'}))
    # class Meta:
    # model= models.Sheet1
    # fields = '__all__'
    # title = forms.CharField(max_length=50)

    # 'class': 'custom-file-input',


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class EditUserForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
