# -*- coding: utf-8 -*-
from django.db import models
from django import forms
import datetime
from django.utils.safestring import mark_safe
from django.forms.extras.widgets import SelectDateWidget



# Create your models here.
class Leads(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    gender = models.CharField(verbose_name='Gender', max_length=2)
    languages = models.CharField(verbose_name='Languages', max_length=20, default='English')
    card_number = models.CharField(verbose_name='Card number', max_length=15)
    expiry_date = models.DateField(verbose_name='Expiry date')
    professional = models.CharField(verbose_name='Professional', max_length=5)

    def __unicode__(self):
        return self.name


# class Languages(models.Model):
#     leads = models.ForeignKey(Leads)
#     languages = models.CharField(verbose_name='Languages', max_length=20, default='English')


class HorizRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class LeadsForm(forms.ModelForm):
    name = forms.CharField(required=False, label='Name', max_length=50)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.CharField(required=False, label='Gender',
                             widget=forms.RadioSelect(
                                 renderer=HorizRadioRenderer,
                                 choices=GENDER_CHOICES))
    languages = forms.CharField(required=False, label='Languages', max_length=20, help_text='l')
    card_number = forms.CharField(required=False, label='Card number', max_length=15, help_text='c')
    expiry_date = forms.DateField(required=False, label='Expiry date', initial=datetime.date.today,
                                  widget=SelectDateWidget(years=range(2015, 2150)))

    PROFESSIONAL_CHOICES = (
        ('Y', 'YES'),
        ('N', 'NO')
    )
    professional = forms.CharField(required=False, label='Professional',
                                   widget=forms.RadioSelect(
                                       renderer=HorizRadioRenderer,
                                       choices=PROFESSIONAL_CHOICES))
    class Meta:
        model = Leads
        # fields = ['name', 'gender', 'card_number', 'expiry_date', 'professional', 'languages']
        fields = '__all__'