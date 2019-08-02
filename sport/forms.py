from django import forms
from .models import Users,Football,Basketball,Login,Bolleyball,Rugby,Running,Cyclisme

# Create your models here.
class RegisterFom(forms.Form):
    nom=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    pseudo=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'input'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))
    password_confirm=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))
    created_at=forms.DateField(widget=forms.DateInput(attrs={'class':'input'}))

class UsersForm(forms.ModelForm):

    class Meta:
        model=Users
        fields=('nom','pseudo','email','password','password_confirm')
        widgets={
          'nom':forms.TextInput(attrs={'class':'form-control'}),
          'pseudo':forms.TextInput(attrs={'class':'form-control'}),
          'email':forms.EmailInput(attrs={'class':'form-control'}),
          'password':forms.PasswordInput(attrs={'class':'form-control'}),
          'password_confirm':forms.PasswordInput(attrs={'class':'form-control'}),
          'created_atnom':forms.DateInput(attrs={'class':'form-control'}) ,  
        }

class FootballForm(forms.Form):
    club=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    la_mise=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    score=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))

class FootballFormClass(forms.ModelForm):

    class Meta:
        model=Football
        fields=('club','la_mise','score')
        widgets={
          'club':forms.TextInput(attrs={'class':'form-control'}),
          'la_mise':forms.TextInput(attrs={'class':'form-control'}),
          'score':forms.TextInput(attrs={'class':'form-control'})
        }

class BasketballForm(forms.Form):
    club=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    la_mise=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    score=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))

class BasketballFormClass(forms.ModelForm):

    class Meta:
        model=Football
        fields=('club','la_mise','score')
        widgets={
          'club':forms.TextInput(attrs={'class':'form-control'}),
          'la_mise':forms.TextInput(attrs={'class':'form-control'}),
          'score':forms.TextInput(attrs={'class':'form-control'})
        }

class VolleyballForm(forms.Form):
    club=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    la_mise=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    score=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))

class VolleyballFormClass(forms.ModelForm):

    class Meta:
        model=Bolleyball
        fields=('club','la_mise','score')
        widgets={
          'club':forms.TextInput(attrs={'class':'form-control'}),
          'la_mise':forms.TextInput(attrs={'class':'form-control'}),
          'score':forms.TextInput(attrs={'class':'form-control'})
        }

class BasketballFormClass(forms.ModelForm):

    class Meta:
        model=Football
        fields=('club','la_mise','score')
        widgets={
          'club':forms.TextInput(attrs={'class':'form-control'}),
          'la_mise':forms.TextInput(attrs={'class':'form-control'}),
          'score':forms.TextInput(attrs={'class':'form-control'})
        }

class RugbyForm(forms.Form):
    club=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    la_mise=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    score=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))

class RugbyFormClass(forms.ModelForm):

    class Meta:
        model=Rugby
        fields=('club','la_mise','score')
        widgets={
          'club':forms.TextInput(attrs={'class':'form-control'}),
          'la_mise':forms.TextInput(attrs={'class':'form-control'}),
          'score':forms.TextInput(attrs={'class':'form-control'})
        }

class CyclismeForm(forms.Form):
    club=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    la_mise=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    score=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))

class CyclismeFormClass(forms.ModelForm):

    class Meta:
        model=Cyclisme
        fields=('club','la_mise','score')
        widgets={
          'club':forms.TextInput(attrs={'class':'form-control'}),
          'la_mise':forms.TextInput(attrs={'class':'form-control'}),
          'score':forms.TextInput(attrs={'class':'form-control'})
        }


class RunningForm(forms.Form):
    club=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    la_mise=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    score=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))

class RunningFormClass(forms.ModelForm):

    class Meta:
        model=Running
        fields=('club','la_mise','score')
        widgets={
          'club':forms.TextInput(attrs={'class':'form-control'}),
          'la_mise':forms.TextInput(attrs={'class':'form-control'}),
          'score':forms.TextInput(attrs={'class':'form-control'})
        }


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))

class LoginFormClass(forms.ModelForm):

    class Meta:
        model=Login
        fields=('username','password')
        widgets={
          'username':forms.TextInput(attrs={'class':'form-control'}),
          'password':forms.PasswordInput(attrs={'class':'form-control'})
        }


