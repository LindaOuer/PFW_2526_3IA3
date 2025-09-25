from django.contrib import admin
from .models import Category, Tag, Product

# Personnalisation globale de l'AdminSite
admin.site.site_header = 'Administration de Mon Application' # Titre en haut de la page
admin.site.site_title = 'Admin Django' # Titre de l'onglet du navigateur
admin.site.index_title = 'Bienvenue dans le Dashboard' # Titre de la page d'accueil de l'admin

# InlineModelAdmin pour la relation ManyToMany entre Product et Tag
class TagInline(admin.TabularInline):
    model = Product.tags.through
    extra = 1
    
# Enregistrement simple pour Tag
admin.site.register(Tag)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 10
    
admin.site.register(Category, CategoryAdmin)


# Méthodes personnalisées pour ProductAdmin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'stock', 'created', 'updated')
    list_filter = ('category', 'price')
    search_fields = ('title', 'description')
    list_editable = ('price', 'stock')
    list_display_links = ('title', 'category')
    list_per_page = 2
    date_hierarchy = 'created'
    readonly_fields = ('created', 'updated')
    # exclude = ('description',)
    # fields = ('title', 'category', 'price', 'stock', 'slug')
    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'price', 'stock', 'description')
        }),
        ('Slug Information', {
            'fields': ('slug',),
        }),
        ('Timestamps', {
            'fields': ('created', 'updated'),
        }),
    )
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ('category',)
    ordering = ('title', '-price')  # Ordonnancement : titre ascendant, prix descendant
    list_select_related = ('category',)  # Optimisation des queries
    preserve_filters = True  # Conserver les filtres après actions
    show_full_result_count = False  # Désactiver le compteur total pour performance
    actions = ['set_price_to_zero']
    inlines = [TagInline]
    

    # def get_discounted_price(self, obj):
    #     return obj.price * 0.9  # Réduction de 10%
    # get_discounted_price.short_description = 'Prix réduit'

    def set_price_to_zero(self, request, queryset):
        queryset.update(price=0)
        self.message_user(request, "Le prix a été mis à 0 pour les produits sélectionnés.")
    set_price_to_zero.short_description = "Mettre le prix à 0 pour les produits sélectionnés"

    # Ajout de CSS/JS personnalisés
    class Media:
        css = {
            'all': ('css/custom_admin.css',)
        }
        js = ('js/custom_admin.js',)


