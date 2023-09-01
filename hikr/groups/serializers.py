from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Group, GroupMembership


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name', 'description', 'location', 'owner', 'image', 'created_at', 'updated_at']


class GroupMembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = GroupMembership
        fields = ['id', 'joined_at', 'user']