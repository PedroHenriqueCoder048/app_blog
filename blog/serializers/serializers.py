from rest_framework import serializers

from ..models import Blog , Reaction

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class ReactionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = "__all__"