from django import forms
from landing.models import image_evidence


# Create your forms here.
class ImageForm(forms.ModelForm):

    class Meta:
        model = image_evidence
        fields = ('form_id','image_evidence',)
        widgets = {'form_id': forms.HiddenInput()}

    def save(self, form_id=None):
        image_evidence = super(ImageForm, self).save(commit=False)
        if form_id:
            image_evidence.form_id = form_id
        image_evidence.save()
        return image_evidence
