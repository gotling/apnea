# coding=utf-8
from django import forms


class UploadFileForm(forms.Form):
    session_start = forms.TimeField(label='Sessionens start')
    discipline = forms.CharField(label='Disciplin', help_text='DNF')
    file = forms.FileField(label='Fil', help_text=u'Endast Dive Master CSV filer stöds')