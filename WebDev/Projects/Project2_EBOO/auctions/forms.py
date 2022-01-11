from django import forms

class ListingForm(forms.Form):
    listing_name = forms.CharField(label='Title: ', max_length=50, required=True)
    listing_desc = forms.CharField(label='Description: ', max_length=500, widget=forms.Textarea, required=True)
    listing_start_bit = forms.DecimalField(label="Starting Bid: ", min_value=1, max_value=9999999, max_digits=9, decimal_places=2, required=True)
    listing_image = forms.URLField(label='Image URL: ')
    
    lines = []
    with open('auctions/static/auctions/catagories.txt') as f:
        for line in f:
            lines.append((line, line))
    

    listing_catagory = forms.ChoiceField(label="Catagory: ", choices=lines, required=True)
    
    