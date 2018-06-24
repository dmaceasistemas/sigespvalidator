from django import forms 



class ValidarConstancia(forms.Form):
	codigo = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control input-sm','style':'width:300px'}))
	#codigo = forms. FloatField(widget=forms.TextInput(attrs={'class':'form-control input-sm','style':'width:300px'}))


	def clean_codigo(self):
		codigo = self.cleaned_data.get('codigo')
		try:
			s = float(codigo)
		except ValueError:
			raise forms.ValidationError("Error, el Codigo no es Tipo float ")
		return codigo 
