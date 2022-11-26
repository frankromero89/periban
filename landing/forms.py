from django import forms
from landing.models import image_evidence, ticket_image_evidence


# Create your forms here.
class ImageForm(forms.ModelForm):
    class Meta:
        model = image_evidence
        fields = (
            "form_id",
            "image_evidence",
        )
        widgets = {"form_id": forms.HiddenInput()}

    def save(self, form_id=None):
        image_evidence = super(ImageForm, self).save(commit=False)
        if form_id:
            image_evidence.form_id = form_id
        image_evidence.save()
        return image_evidence


class ImageTicketForm(forms.ModelForm):
    class Meta:
        model = ticket_image_evidence
        fields = (
            "client_name",
            "ticket_image",
        )

    def save(self, client_name=None):
        ticket_image = super(ImageTicketForm, self).save(commit=False)
        if client_name:
            ticket_image.client_name = client_name
        ticket_image.save()
        return ticket_image
