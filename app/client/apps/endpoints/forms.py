
from django import forms
from apps.endpoints.models import Flight


class FlightForm(forms.ModelForm):

    class Meta:
        model = Flight        

        fields =["departure", "destination", "flight_date", "arrival_date"]
        widgets = {
            'flight_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'arrival_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }
    def clean(self):
 
        super(FlightForm, self).clean()
 
        return self.cleaned_data