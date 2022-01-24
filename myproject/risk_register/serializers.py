from django.contrib.auth.models import User, Group
from rest_framework import serializers
from risk_register.models import Risks

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class RisksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Risks
        fields = ['risk_description', 'risk_impact','risk_mitigation','risk_owner', 'risk_assignee', 'risk_due_date','risk_assignee']