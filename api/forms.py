from django import forms
from datetime import date

class DateForm(forms.Form):
    # Restricciones de fecha
    min_date= date(1995,6,16) #primer día disponible en la API de la NASA
    max_date= date.today()

    # Formulario que crea un selector de fecha limitado entre el 16 de junio de 1995 y hoy
    date= forms.DateField(
        widget= forms.DateInput(
            attrs={
                "type": "date",
                "min": min_date.strftime("%Y-%m-%d"),
                "max": max_date.strftime("%Y-%m-%d")
            }
        ),
        label= "Seleccione una fecha"
    )

    # Este método se ejecuta al validar el formulario(form.is_valid())
    def clean_date(self):
        selected_date= self.cleaned_data["date"] #obtener la fecha ingresada como un objeto date
        if selected_date < self.min_date or selected_date > self.max_date:
            raise forms.ValidationError(f"La fecha debe estar entre {self.min_date} y {self.max_date}")
        return selected_date
