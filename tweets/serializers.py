from abc import ABC

from rest_framework import serializers
from django.conf import settings
from .models import Tweet

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH
TWEET_ACTION_OPTIONS = settings.TWEET_ACTION_OPTIONS


class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    comment = serializers.CharField(allow_blank=True, required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate_action(self, value):
        value = value.lower().strip()
        if value not in TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action for Tweets")
        return value


class TweetCreateSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'content', 'likes']

    @staticmethod
    def get_likes(self):
        return self.likes.count()

    def validate_content(self, value):
        if len(value) > MAX_TWEET_LENGTH:
            raise serializers.ValidationError("This Tweet is too long")
        return value


class TweetSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    content = serializers.SerializerMethodField(read_only=True)
    parent = TweetCreateSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'content', 'likes', 'is_retweet', 'parent']

    @staticmethod
    def get_likes(self):
        return self.likes.count()

    @staticmethod
    def get_content(obj):
        content = obj.content
        if obj.is_retweet:
            content = obj.parent.content
        return content
