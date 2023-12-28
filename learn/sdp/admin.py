from django.contrib import admin

# Register your models here.
from .models import cat, movie, music, marriage, contactf, addmovies, dcontactf, event, moviepic, addmovies2,Item

admin.site.register(cat)
admin.site.register(movie)
admin.site.register(music)
admin.site.register(marriage)
admin.site.register(contactf)
admin.site.register(addmovies)
admin.site.register(dcontactf)
admin.site.register(event)
admin.site.register(moviepic)
admin.site.register(addmovies2)
admin.site.register(Item)


# admin.site.register(Musicalconcertm)
# admin.site.register(weddinghalls)