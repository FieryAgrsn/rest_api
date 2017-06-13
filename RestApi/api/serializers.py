from rest_framework import serializers
from api.models import Bet, Event, User




class BetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #event = serializers.ReadOnlyField(source='event.text')
    highlight = serializers.HyperlinkedIdentityField(view_name='bet-highlight', format='html')
    class Meta:
        model = Bet
        fields = ('url', 'id', 'highlight', 'owner',
                  'code', 'event', 'selected_team', 'size_of_bet', )


class EventSerializer(serializers.HyperlinkedModelSerializer):
    #bets = serializers.HyperlinkedRelatedField(many=True, view_name='bet-detail', read_only=True)

    class Meta:
        model = Event
        fields = ('url', 'id', 'text', 'Team_1', 'Team_2', 'coef', 'Team_1_bets', 'Team_2_bets')

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    money = serializers.FloatField(read_only=True)
    class Meta:
        model = User
        fields = ('url','id','username','first_name', 'last_name', 'email', 'password', 'money')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

