from django import forms

class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=300)
    subtitle = forms.CharField(max_length=900)
    content = forms.CharField(max_length=10000)
    category = forms.CharField(max_length=45)

class ContactMessageForm(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    message = forms.CharField(max_length=700)

class TeamMemberForm(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    email = forms.EmailField()
    githubaccount = forms.CharField(max_length=30)
