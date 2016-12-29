from django.contrib import admin
from .models import Building, ImgBuilding, Comment, Rating
from django.utils.safestring import mark_safe


class ImgInline(admin.TabularInline):
    extra = 0
    max_num = 10
    fields = ('image', 'show_img', 'tri')
    verbose_name = ("Building gallery")
    verbose_name_plural = ("Building gallery")
    readonly_fields = ('show_img',)
    def show_img(self, obj):
        return mark_safe("""<img width="164px" height="90px" src="/media/%s" />""" % obj.image)

    show_img.short_description = "Image"


class ImgBuildingInline(ImgInline):
    model = ImgBuilding

######################################


class ComsInline(admin.TabularInline):
    extra = 0
    max_num = 10
    fields = ('text',)
    verbose_name = ("text")
    verbose_name_plural = ("texts")
    readonly_fields = ('show_img',)
    def show_img(self, obj):
        return mark_safe(obj.comment)

    show_img.short_description = "Comment"


class CommentInline(ComsInline):
    model = Comment


######################################


class BuildingAdmin(admin.ModelAdmin):
    list_display = ("streetname", "streetnumber", "zipcode")
    search_fields = ("streetname", "zipcode")
    inlines = [ImgBuildingInline,CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ("building", "text", "created")
    search_fields = ("building", )

class RatingAdmin(admin.ModelAdmin):
    list_display = ("building", "rate", "created")
    search_fields = ("building", )


admin.site.register(Building, BuildingAdmin)
#admin.site.register(Comment, CommentAdmin)
admin.site.register(Rating, RatingAdmin)
