from django.contrib import admin

from .models.author import Author
from .models.post import Post, Comment
from .models.tag import Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)

# klase Post author tag i comment su glavne klase-modeli koje koristimo u projektu,
# njih editujemo preko admina ili preko shella, a klase commentadmin i postadmin su klase koje
# sluze samo da bi bolje videli glavne klase, one ne uticu na sadrzaj u ove 4 glavne klase
