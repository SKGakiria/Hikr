from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Group, GroupMembership


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class GroupMembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = GroupMembership
        fields = ['id', 'joined_at', 'user']