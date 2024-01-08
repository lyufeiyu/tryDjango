from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
	title = forms.CharField(label='。。',widget=forms.TextInput(
								attrs={
									"placeholder": "Your title",
								}
							)
						)
	email = forms.EmailField()
	description = forms.CharField(
						required=False,
						widget=forms.Textarea(
							attrs={
								"placeholder": "Your description",
								"class": "new-class-name two",
								"id": "my-id-for-textarea",
								"rows": 20,
								"cols": 120	
							}
						)
					)
	price = forms.DecimalField(initial=2024)
	class Meta:  # 你有可能也会注意到，将这个class注释掉，再将上面的ModelForm改成Form，效果也是一样的。
		model=Product
		fields=[
			'title',
			'description', 
			'price'
		]
	def clean_title(self,*args,**kwargs):   # 标题验证，本质是数据筛选。我们同样有一个名为form valid的方法，它接受self和form参数
		title = self.cleaned_data.get("title")
		if "CFE" in title:
			return title
		else:
			raise forms.ValidationError("This is not a valid title")

	def clean_email(self,*args,**kwargs):
		email  = self.cleaned_data.get("email")
		if not email.endswith("edu"):
			raise forms.ValidationError("This is not a valid email")
		return email

class RawProductForm(forms.Form):     # 注意了，django原生的表单是用forms.Form
	title = forms.CharField(label='。。',widget=forms.TextInput(
								attrs={
									"placeholder": "Your title",
								}
							)
						)
	description = forms.CharField(
						required=False,
						widget=forms.Textarea(
							attrs={
								"placeholder": "Your description",
								"class": "new-class-name two",
								"id": "my-id-for-textarea",
								"rows": 20,
								"cols": 120	
							}
						)
					)
	price = forms.DecimalField(initial=2024)

