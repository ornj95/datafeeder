from rest_framework import serializers

from account.models import Articles


class ArticlesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Articles
        fields = ['heading', 'body', 'category', 'content_type', 'source_link',
                  'image_link', 'tags', 'published_date', 'published_time',
                  'author'
                  ]

