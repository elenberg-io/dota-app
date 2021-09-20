from django import forms
from .models import Heroes


class HeroForm(forms.Form):
    hero = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Heroes.objects.values_list('localized_name', flat=True),
        label=''
    )


# class HeroForm(forms.ModelForm):
#     # hero = forms.ModelMultipleChoiceField(
#     #     widget=forms.CheckboxSelectMultiple,
#     #     queryset=Heroes.objects.all()
#     # )
#     class Meta:
#         model = Heroes
#         fields = ['localized_name']
#
#     def __init__(self, *args, **kwargs):
#         super(HeroForm, self).__init__(*args, **kwargs)
#         self.fields['localized_name'] = forms.ModelMultipleChoiceField(queryset=Heroes.objects.all(),
#                                                                        widget=forms.CheckboxSelectMultiple,
#                                                                        label='')

# class HeroForm(forms.ModelForm):
#     class Meta:
#         model = Heroes
#         fields = ['localized_name']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['localized_name'] = forms.ModelMultipleChoiceField(queryset=Heroes.objects.all(),
#                                                                        widget=forms.CheckboxSelectMultiple,
#                                                                        to_field_name="localized_name")


# class HeroModelChoiceField(forms.ModelMultipleChoiceField):
#     def label_from_instance(self, obj):
#          return obj.objects.localized_name
#
# class HeroForm(forms.Form):
#     hero = HeroModelChoiceField(
#         widget=forms.CheckboxSelectMultiple,
#         queryset=Heroes.objects.all(),
#         label=''
#     )
#
# class HeroForm(forms.ModelForm):
#
#     class Meta:
#         model = Heroes
#         fields = ('localized_name',)
#
#     name = forms.ModelMultipleChoiceField(
#         # queryset=Heroes.objects.values_list('localized_name', flat=True),
#         queryset=Heroes.objects.all(),
#                                           label='Select ',
#                                           widget=forms.CheckboxSelectMultiple,
#                                           )

    # def __init__(self, *args, **kwargs):
    #     super(HeroForm, self).__init__(*args, **kwargs)
    #     self.fields['localized_name'] = forms.ModelMultipleChoiceField(queryset=Heroes.objects.all(),
    #                                                                    widget=forms.CheckboxSelectMultiple,
    #                                                                    label='')
