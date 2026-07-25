from django.contrib import admin
import nested_admin
from .models import Product, BookTemplate, PageTemplate, BeforeAfterSlide, ProductPreviewItem, ProductPreviewImage

class PageTemplateInline(admin.TabularInline):
    model = PageTemplate
    extra = 1
    fields = ('page_number', 'story_text', 'image_name', 'mask_image_name', 'is_preview')
    ordering = ('page_number',)

class ProductPreviewImageInline(nested_admin.NestedTabularInline):
    model = ProductPreviewImage
    extra = 1
    fields = ('image', 'order')
    ordering = ('order',)

class ProductPreviewItemInline(nested_admin.NestedTabularInline):
    model = ProductPreviewItem
    extra = 1
    fields = ('item_type', 'order')
    inlines = [ProductPreviewImageInline]
    ordering = ('order',)

@admin.register(ProductPreviewItem)
class ProductPreviewItemAdmin(nested_admin.NestedModelAdmin):
    list_display = ('product', 'item_type', 'order', 'created_at')
    list_filter = ('item_type', 'product')
    inlines = [ProductPreviewImageInline]

@admin.register(Product)
class ProductAdmin(nested_admin.NestedModelAdmin):
    list_display = ('title', 'age_range', 'price_softcover', 'original_price_softcover', 'price_hardcover', 'original_price_hardcover', 'rating', 'is_active')
    list_filter = ('is_active', 'age_range')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductPreviewItemInline]


@admin.register(BookTemplate)
class BookTemplateAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'age_group', 'is_active', 'created_at')
    list_filter = ('is_active', 'age_group')
    search_fields = ('title', 'description')
    inlines = [PageTemplateInline]

@admin.register(PageTemplate)
class PageTemplateAdmin(admin.ModelAdmin):
    list_display = ('book_template', 'page_number', 'is_preview')
    list_filter = ('is_preview', 'book_template')
    ordering = ('book_template', 'page_number')

@admin.register(BeforeAfterSlide)
class BeforeAfterSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'slide_type', 'order', 'is_active', 'created_at')
    list_filter = ('slide_type', 'is_active')
    search_fields = ('title',)

