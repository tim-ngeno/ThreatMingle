from django import forms


class AssessmentForm(forms.Form):
    """
    Form to get a personalized assessment scan
    """
    SCAN_OPTIONS = [
        ('file', 'File Hash'),
        ('ip', 'IP Address'),
        ('url', 'URL'),
    ]

    options = forms.ChoiceField(
        choices=SCAN_OPTIONS, widget=forms.RadioSelect
    )
    input_data = forms.CharField(
        max_length=256,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter a file hash, URL or IP address'}
        )
    )
