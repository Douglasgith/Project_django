from django import forms


class LoginForms(forms.Form):
   nome_login=forms.CharField(
      label="Nome de Login ",
      required=True,
      max_length=100,
      widget=forms.TextInput(
         attrs={"class":"form-control",
                "placeholder": "Ex.: Joao Silva"}
      )
    
   )
   senha=forms.CharField(
      label="Senha",
      required=True,
      max_length=70,
      widget=forms.PasswordInput(
         attrs={"class":"form-control",
                "placeholder": "Ex.: Digite sua senha "}
      )
   )


class CadastroFroms(forms.Form):
   nome_cadastro=forms.CharField(
      label="Nome de Cadastro ",
      required=True,
      max_length=100,
      widget=forms.TextInput(
         attrs={"class":"form-control",
                "placeholder": "Ex.: Joao Silva"}
      )
    
   )
   email=forms.EmailField(
      label="Email",
      required=True,
      max_length=100,
      widget=forms.EmailInput(
          attrs={"class":"form-control",
                "placeholder": "Ex.: Joaisilva@gmail.com "}
      )
   )
   senha_1=forms.CharField(
      label="Senha",
      required=True,
      max_length=70,
      widget=forms.PasswordInput(
         attrs={"class":"form-control",
                "placeholder": "Ex.: Digite sua senha "}
      )
   )
   senha_2=forms.CharField(
      label="Confirme sua senha",
      required=True,
      max_length=70,
      widget=forms.PasswordInput(
         attrs={"class":"form-control",
                "placeholder": "Ex.: Digite sua senha novamente "}
      )
   )