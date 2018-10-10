from django import forms
from .models import Politician, Quote

class PoliticianForm(forms.ModelForm):
    class Meta:
        model = Politician
        fields = ('title', 'first_name', 'last_name', 'date_of_birth', 'gender', 'party', 'twitter_account', 'url', 'total_votes', 'missed_votes', 'phone', 'state', 'state_rank', 'missed_votes_pct', 'votes_with_party_pct')

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('content', 'source', 'politician')