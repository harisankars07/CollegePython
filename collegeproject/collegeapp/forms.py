from django import forms
from .models import Department, Course

class EnquiryForm(forms.Form):
    name = forms.CharField()
    dob = forms.DateField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    phone_number = forms.CharField()
    mail_id = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.none())
    purpose = forms.ChoiceField(choices=[('enquiry', 'Enquiry'), ('place_order', 'Place Order'), ('return', 'Return')])
    materials_provide = forms.MultipleChoiceField(choices=[('notebook', 'Notebook'), ('pen', 'Pen'), ('exam_papers', 'Exam Papers')], widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'department' in self.data:
            department_id = int(self.data.get('department'))
            self.fields['course'].queryset = Course.objects.filter(department_id=department_id)
        elif self.initial.get('department'):
            self.fields['course'].queryset = Course.objects.filter(department_id=self.initial['department'])

