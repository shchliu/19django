from django import forms


class MyForm(forms.Form):
    email = forms.EmailField(label="邮箱", error_messages={"typeerror":"请输入正确的邮箱"})
    price = forms.FloatField(label="价格", error_messages={"invalid":"请输入浮点类型"})
    personal_website = forms.URLField(label="个人主页", error_messages={"invalid":"请输入正确的网站","require":"请输入正确的"})