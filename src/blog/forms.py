from django import forms
from .models import Article

class ArticleModelForm(forms.ModelForm):
	class Meta:  # 你有可能也会注意到，将这个class注释掉，再将上面的ModelForm改成Form，效果也是一样的。
		model=Article
		fields=[
			'title',
			'content', 
			'active',
		]