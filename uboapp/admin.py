from django.contrib import admin
from .models import Building, ImgBuilding
from django.utils.safestring import mark_safe


#class ImageInLine(admin.TabularInline):
#    model = ImgBuilding

#class BuildingAdmin(ImageInLine):
#    inlines = [ImageInLine, ]


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


class BuildingAdmin(admin.ModelAdmin):
    list_display = ("streetname", "streetnumber", "zipcode")
    search_fields = ("streetname", "zipcode")
    inlines = [ImgBuildingInline]


admin.site.register(Building, BuildingAdmin)