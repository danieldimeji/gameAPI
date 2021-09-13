from django.db import models


class PlayStoreGamesCategory(models.Model):

    category_name = models.CharField('Category Name', max_length = 500)

    category_link = models.URLField('Category Link', max_length = 1000)

    created_on = models.DateTimeField(auto_now_add = True)

    updated_on = models.DateTimeField(auto_now = True)


    class Meta:
        ordering = ['category_name']


    def __str__(self) -> str:
        return self.category_name



class Games(models.Model):

    title = models.CharField('Title', max_length = 500)  #check

    category = models.ForeignKey(PlayStoreGamesCategory, on_delete = models.SET_NULL, null = True) #check

    details_link = models.URLField('Details Link', max_length = 1000)  #check

    app_id = models.CharField('App ID', max_length = 500, null = True)  #check

    image_link =  models.URLField('Image Link', max_length = 1000, null = True)

    description = models.TextField('Description', null = True)  #check

    ratings = models.CharField('Ratings', max_length = 500, null = True) #check

    score = models.CharField('Score', max_length = 225, null = True) #check

    created_on = models.DateTimeField(auto_now_add = True)

    updated_on = models.DateTimeField(auto_now = True)


    class Meta:
        ordering = ['title']


    def __str__(self) -> str:
            return self.title
