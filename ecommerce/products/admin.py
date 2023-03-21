from django.contrib import admin
from products.models import Category, Product, SubCategory

class SubCategoryAdmin(admin.TabularInline):
    model = SubCategory

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','live',)
    list_filter = ('live',)
    search_fields = ['title',]
    inlines = [SubCategoryAdmin,]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','category','in_stock_items', 'live',)
    list_filter = ('live', 'category', )
    search_fields = ['title',]
    readonly_fields = ('ordered_times',)

    fieldsets = (
        ("معلومات المنتج", {
            "classes": ("wide"),
            "fields": ("title", "category", "sub_category", "description", "live", "in_stock_items", "product_order", "ordered_times", "currency", "item_weight"),
        }),
        ("صور المنتج", {
            "classes": ("wide"),
            "fields": ("main_image", "image_1", "image_2", "image_3"),
        }),
        # ("بيانات الفئة الكبيرة", {
        #     "classes": ("wide"),
        #     "fields": ("big_unit", "big_unit_price", "big_unit_max_quantity", "big_unit_price_discount", "big_unit_discount_max_quantity", "in_big_items", "item_weight"),
        # }),
        # ("بيانات الفئة الصغيرة", {
        #     "classes": ("wide"),
        #     "fields": ("small_available", "small_unit", "small_unit_price", "small_unit_max_quantity", "small_unit_price_discount", "small_unit_discount_max_quantity"),
        # })
        ("بيانات الفئة", {
            "classes": ("wide"),
            "fields": ("small_unit", "small_unit_price", "small_unit_max_quantity", "small_unit_price_discount", "small_unit_discount_max_quantity"),
        })
        )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)