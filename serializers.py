from.models import Cryptocurrency
from rest_framework import serializers

class CryptocurrencySerializers(serializers.Serializer):
    class Meta:
         model=Cryptocurrency
         fields=[cryptocurrency,price,market_cap,change]