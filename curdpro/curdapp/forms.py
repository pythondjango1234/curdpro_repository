from django import forms
class InsertingDataForm(forms.Form):
    Product_Id=forms.IntegerField(
        label="Enter your product Id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Product Id'
            }
        )
    )
    Product_Name=forms.CharField(
        label='Enter Your Product Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Product Name'
            }
        )
    )
    Product_Cost=forms.IntegerField(
        label='Enter Your Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Product Cost'
            }
        )
    )
    Product_Color = forms.CharField(
        label='Enter Product Color',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Color'
            }
        )
    )
    Product_Class = forms.CharField(
        label='Enter Product Class',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Class'
            }
        )
    )
    Customer_Name = forms.CharField(
        label='Enter Customer Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Customer Name'
            }
        )
    )
    Customer_Mobile = forms.IntegerField(
        label='Enter Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Product Cost'
            }
        )
    )
    Customer_Email=forms.EmailField(
        label='Enter Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email'
            }
        )
    )
class UpdatingDataForm(forms.Form):
    Product_Id = forms.IntegerField(
        label='Enter Your Product Id',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Product Id'
            }
        )
    )
    Product_Cost = forms.IntegerField(
        label='Enter Your Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Product Cost'
            }
        )
    )
class DeletingDataForm(forms.Form):
    Product_Id=forms.IntegerField(
        label='Enter Your Product Id',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Product Id'
            }
        )

    )