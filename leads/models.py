from django.db import models
from django import forms
import datetime

# Create your models here.
class Leads(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    GENDER_CHOICES = (
        ('1', 'M'),
        ('2', 'S'),
    )
    gender = models.CharField(verbose_name='Gender', choices=GENDER_CHOICES, max_length=2)
    languages = models.CharField(verbose_name='Languages', max_length=20, default='English')
    card_number = models.CharField(verbose_name='Card number', max_length=15)
    expiry_date = models.DateField(verbose_name='Expiry date')
    professional = models.BooleanField(verbose_name='Professional')

    def __unicode__(self):
        return self.name


class LeadsForm(forms.ModelForm):
    name = forms.CharField(required=False, label='Name', max_length=50)
    GENDER_CHOICES = (
        ('1', 'M'),
        ('2', 'S'),
    )
    gender = forms.ChoiceField(required=False, label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect(), help_text='g')
    languages = forms.CharField(required=False, label='Languages', max_length=20, help_text='l')
    card_number = forms.CharField(required=False, label='Card number', max_length=15, help_text='c')
    expiry_date = forms.DateField(required=False, label='Expiry date', initial=datetime.date.today, help_text='e')
    professional = forms.BooleanField(required=False, label='Professional', help_text='p')
    class Meta:
        model = Leads
        fields = '__all__'