
from django import forms
from apps.endpoints.models import Flight


class FlightForm(forms.ModelForm):
    # class Meta:
    class Meta:
        # write the name of models for which the form is made
        model = Flight        
        # Custom fields
        fields =["departure", "destination", "flight_date", "arrival_date"]
        widgets = {
            'flight_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'arrival_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }
    def clean(self):
 
        super(FlightForm, self).clean()
         
        # # extract the username and text field from the data
        return self.cleaned_data