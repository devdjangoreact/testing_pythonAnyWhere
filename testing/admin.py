from django.contrib import admin

from .models import Category, Test, HashTag, SetTest, TestList, SetTestList


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
#    fields = ("title",)
#    list_display = ("title", )
    readonly_fields = (    )

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
#    fields = ("title",)
#    list_display = ("title", )
    readonly_fields = (    )
    
@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
#    fields = ("title",)
#    list_display = ("title", )
    readonly_fields = (    )

@admin.register(SetTest)
class SetTestAdmin(admin.ModelAdmin):
#    fields = ("title",)
#    list_display = ("title", )
    readonly_fields = (    )
    
@admin.register(TestList)
class TestListAdmin(admin.ModelAdmin):
#    fields = ("title",)
#    list_display = ("title", )
    readonly_fields = (    )

@admin.register(SetTestList)
class SetTestListAdmin(admin.ModelAdmin):
#    fields = ("__all__",)
    # list_display = ("test", )
    readonly_fields = (  "updated_date",  )
