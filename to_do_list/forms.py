from django import forms

class LoginForms(forms.Form):
    user_name = forms.CharField(
        label = 'User Name',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type':"text",
                'class':"form-control mb-3", 
                'id':"floatingInput",
                'placeholder':"mokeyDLuffy",
            }
        )
    )
    password=forms.CharField(
        label='Password', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'type':"password", 
                'class':"form-control",
                'id':"floatingPassword", 
                'placeholder':"Password",
            }
        ),
    )
class RegisterForms(forms.Form):
    user_name = forms.CharField(
        label = 'User Name',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type':"text",
                'class':"form-control mb-3", 
                'id':"floatingInput",
                'placeholder':"mokeyDLuffy",
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'type':"email", 
                'class':"form-control", 
                'id':"floatingInput" ,'placeholder':"name@example.com",
            }
        )
    )
    password=forms.CharField(
        label='Password', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'type':"password", 
                'class':"form-control",
                'id':"floatingPassword", 
                'placeholder':"Password",
            }
        ),
    )
    password2=forms.CharField(
        label='Confirm your password', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'type':"password", 
                'class':"form-control",
                'id':"floatingPassword", 
                'placeholder':"Password",
            }
        ),
    )
class TaskForms(forms.Form):
    task=forms.CharField(
        label='Descreva sua tarefa',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type':"text" ,
                'class':"form-control ",                
                'id':"floatingInput", 
                'placeholder':"descreva sua tarefa",
            }
        )
    )
    deadline=forms.DateField(
        label='Prazo',
        required=True,          
        widget=forms.DateInput(
            attrs={
                'type':"date" ,
                'class':"form-control" ,
                'id':"floatingInput" ,
                'placeholder':"monkeydluffy",
            }
        )
    )