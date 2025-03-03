from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.constants import COUNTRIES, CATEGORY_TYPE


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=75, verbose_name='Nom', unique=True)
    category_type = models.CharField(_("Type"), max_length=15, choices=CATEGORY_TYPE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'
    
    def __str__(self):
        return self.name


class Options(models.Model):
    name = models.CharField(_("Nom"), max_length=50)
    description = models.TextField(_("Description"), max_length=300)
    created_at = models.DateTimeField(_("Créé le"), auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'
    
    def __str__(self):
        return self.name


class Buildings(models.Model):
    name = models.CharField(_("Nom de l'immeuble"), max_length=100)
    cooling = models.CharField(_("Refroidissement"), max_length=50)
    heater = models.CharField(_("Rechauffement"), max_length=50)
    new = models.BooleanField(_("Nouvelle construction"), )
    nb_garage = models.PositiveIntegerField(_("Espace du garage"), )
    materials = models.CharField(_("Matériel de construction(brièvement)"), max_length=255)
    
    class Meta:
        verbose_name = 'Bâtiment'
        verbose_name_plural = 'Bâtiments'
    
    def __str__(self):
        return self.name


class Properties(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nom', )
    slug = models.SlugField(max_length=175, )
    image = models.ImageField(_("Image"), upload_to="properties", height_field=None, width_field=None, max_length=None)
    description = models.TextField(verbose_name=_('Description'))
    category = models.ForeignKey("Categories", verbose_name=_("Catégorie"), on_delete=models.SET_NULL, null=True)
    options = models.ManyToManyField("Options", )
    building = models.ForeignKey("Buildings", verbose_name=_("Bâtiment"), on_delete=models.CASCADE)
    bedrooms = models.PositiveIntegerField(_("Chambres"))
    bathrooms = models.PositiveIntegerField(_("Douches"))
    rooms = models.PositiveIntegerField(_("Pièces"))
    surface = models.PositiveIntegerField(_("Surface"), default=35)
    price = models.DecimalField(_("Prix"), decimal_places=0, max_digits=12)
    country = models.CharField(max_length=75, choices=COUNTRIES, verbose_name=_('Pays'))
    city = models.CharField(_("Ville"), max_length=75)
    address = models.CharField(_("Adresse"), max_length=100)
    is_available = models.BooleanField(_("Disponibe ?"), default=True)
    created_at = models.DateTimeField(_("Créé le"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("Modifié le"), auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = 'Propriété'
        verbose_name_plural = 'Propriétés'
    
    def __str__(self):
        return self.name
