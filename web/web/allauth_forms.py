from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms


class CaptchedSignUpForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def signup(self, request, user):
        pass
