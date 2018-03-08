from django import forms


class RainForm(forms.Form):
    roofArea = forms.DecimalField(max_digits=4, decimal_places=2)
    roofSlope = forms.DecimalField(max_digits=4, decimal_places=2)
    tankSize = forms.DecimalField(max_digits=4, decimal_places=2)
    roofType = forms.ChoiceField(choices=(('1', 'Tin',), ('2', 'Tiled',)))   
    numPeople = forms.ChoiceField(choices=(('1', '1-5',), ('2', '6-10',), ('3', '11+',)))
    typeOfUser = forms.ChoiceField(choices=(('1', 'HouseHold',), ('2', 'Business',), ('3', 'School',), ('4', 'PolicyMaker',)))
    latitude = forms.DecimalField(max_digits=4, decimal_places=2)
    longitude = forms.DecimalField(max_digits=4, decimal_places=2)