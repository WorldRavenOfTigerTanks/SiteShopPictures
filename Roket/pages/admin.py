from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import *
from django.utils.safestring import mark_safe


class PagesAdminForm(forms.ModelForm):
    fotercontent = forms.CharField(widget=CKEditorWidget())
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Pages
        fields = '__all__'



class PostsAdminForm(forms.ModelForm):
    dopolnitelnie_xapakteristiki = forms.CharField(widget=CKEditorWidget())
    polnoe_opisanie = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Posts
        fields = '__all__'

# class GorizontalPostsAdminForm(forms.ModelForm):
#     dopolnitelnie_xapakteristiki = forms.CharField(widget=CKEditorWidget())
#     polnoe_opisanie = forms.CharField(widget=CKEditorWidget())

#     class Meta:
#         model = Posts
#         fields = '__all__'

class SliderAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorWidget())


    class Meta:
        model = Slider
        fields = '__all__'

class PhotosAdminForm(forms.ModelForm):

    class Meta:
        model = Photos
        fields = '__all__'

# class GorizontalPhotosAdminForm(forms.ModelForm):

#     class Meta:
#         model = Photos
#         fields = '__all__'

class SubscribersAdminForm(forms.ModelForm):
    mas = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Subscribers
        fields = '__all__'














class PagesAdmin(admin.ModelAdmin):

    form = PagesAdminForm


class SliderAdmin(admin.ModelAdmin):

    form = SliderAdminForm

class PostsAdmin(admin.ModelAdmin):

    form = PostsAdminForm

# class GorizontalPostsAdmin(admin.ModelAdmin):

#     form = GorizontalPostsAdminForm

class PhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo')
    list_display_links = ('id', 'title')
    form = PhotosAdminForm

    def get_photo(self, obj):# функция get_photo показывает фото в админке
        if obj.photo:
            return mark_safe(f'<img src="{{obj.photo.url}}" width="50">')
        return '-'

# class GorizontalPhotosAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'photo')
#     list_display_links = ('id', 'title')
#     form = GorizontalPhotosAdminForm

#     def get_photo(self, obj):# функция get_photo показывает фото в админке
#         if obj.photo:
#             return mark_safe(f'<img src="{{obj.photo.url}}" width="50">')
#         return '-'

class SubscribersAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

    form = SubscribersAdminForm




admin.site.register(Pages,PagesAdmin)
admin.site.register(Posts,PostsAdmin)
admin.site.register(Slider,SliderAdmin)
admin.site.register(Category)
admin.site.register(Photos,PhotosAdmin)
admin.site.register(Subscribers,SubscribersAdmin)
# admin.site.register(GorizontalPosts,GorizontalPostsAdmin)
# admin.site.register(GorizontalPhotos,GorizontalPhotosAdmin)
