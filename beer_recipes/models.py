from django.db import models
from datetime import date
from django import forms

# Create your models here.

# These models were taken from the Beer XML Version 1.0 standard


class Hop(models.Model):
    """ This is a hop ingredient a user creates """
    user = models.CharField(max_length=200)  # This is the user that created the object
    name = models.CharField(max_length=200, unique=True,
                            help_text="Name must be unique.")  # Name of the hops
    # Notes about the hop. May be multiline.
    description = models.TextField(
        blank=True, help_text="Enter a description for the hop here. Optional.")
    version = models.PositiveIntegerField(default=1)
    date_submitted = models.DateField(auto_now_add=True)
    # Percent alpha of hops - for example "5.5" represents 5.5% alpha
    alpha = models.DecimalField()
    # The time as measured in minutes.  Meaning is dependent on the “USE” field.
    # For “Boil” this is the boil time.  For “Mash” this is the mash time.  For “First Wort” this is the boil time.
    # For “Aroma” this is the steep time.  For “Dry Hop” this is the amount of time to dry hop.
    time = models.PositiveIntegerField(help_text="In minutes.")
    # Weight in Kilograms of the hops used in the recipe.
    amount = models.DecimalField(help_text="Weight in Kilograms")

    USE_CHOICES = [
        ('Boil', 'Boil'),
        ('Dry Hop', 'Dry Hop'),
        ('Mash', 'Mash'),
        ('First Wort', 'First Wort'),
        ('Aroma', 'Aroma'),

    ]
    use = models.CharField(choices=USE_CHOICES)


class Fermentable(models.Model):
    """ This is a Fermentable object a user creates """
    # The term "fermentable" encompasses all fermentable items that contribute substantially to the beer including extracts, grains, sugars, honey, fruits.
    user = models.CharField(max_length=200)  # This is the user that created the object
    name = models.CharField(max_length=200, unique=True,
                            help_text="Name must be unique.")  # Name of the fermentable.
    # Notes about the fermentable. May be multiline.
    description = models.TextField(
        blank=True, help_text="Enter a description for the fermentable here. Optional.")
    version = models.PositiveIntegerField(default=1)
    date_submitted = models.DateField(auto_now_add=True)
    # Weight of the fermentable, extract or sugar in Kilograms.
    amount = models.DecimalField(help_text="Weight in Kilograms")
    # Percent dry yield (fine grain) for the grain, or the raw yield by weight if this is an extract adjunct or sugar.
    ferm_yield = models.DecimalField()
    # The color of the item in Lovibond Units (SRM for liquid extracts).
    color = models.FloatField()

    TYPE_CHOICES = [
        ('Grain', 'Grain'),
        ('Sugar', 'Sugar'),
        ('Extract', 'Extract'),
        ('Dry Extract', 'Dry Extract'),
        ('Adjunct', 'Adjunct'),
    ]
    # May be "Grain", "Sugar", "Extract", "Dry Extract" or "Adjunct".  Extract refers to liquid extract.
    type = models.CharField(choices=TYPE_CHOICES)


class Yeast(models.Model):
    """ This is a yeast ingredient the user creates """
    # The term "yeast" encompasses all yeasts, including dry yeast, liquid yeast and yeast starters.
    user = models.CharField(max_length=200)  # This is the user that created the object
    name = models.CharField(max_length=200, unique=True,
                            help_text="Name must be unique.")  # Name of the yeast.
    version = models.PositiveIntegerField(default=1)
    date_submitted = models.DateField(auto_now_add=True)
    # Notes about the yeast. May be multiline.
    description = models.TextField(
        blank=True, help_text="Enter a description for the yeast here. Optional.")
    TYPE_CHOICES = [
        ('Ale', 'Ale'),
        ('Lager', 'Lager'),
        ('Wheat', 'Wheat'),
        ('Wine', 'Wine'),
        ('Champagne', 'Champagne'),
    ]
    # May be “Ale”, “Lager”, “Wheat”, “Wine” or “Champagne”.
    type = models.CharField(choices=TYPE_CHOICES)

    FORM_CHOICES = [
        ('Liquid', 'Liquid'),
        ('Dry', 'Dry'),
        ('Slant', 'Slant'),
        ('Culture', 'Culture'),
    ]
    # May be “Liquid”, “Dry”, “Slant” or “Culture”
    form = models.CharField(choices=FORM_CHOICES)


class Misc(models.Model):
    """ This is a miscellaneous ingredient a user creates """
    # The term "misc" encompasses all non-fermentable miscellaneous ingredients
    # that are not hops or yeast and do not significantly change the gravity of the beer.
    # For example: spices, clarifying agents, water treatments, etc…
    user = models.CharField(max_length=200)  # This is the user that created the object
    name = models.CharField(max_length=200, unique=True,
                            help_text="Name must be unique.")  # Name of the miscellaneous ingredient.
    # Notes about the ingredient. May be multiline.
    description = models.TextField(
        blank=True, help_text="Enter a description for the miscellaneous ingredient here. Optional.")
    version = models.PositiveIntegerField(default=1)
    date_submitted = models.DateField(auto_now_add=True)
    # Amount of time the misc was boiled, steeped, mashed, etc in minutes.
    time = models.PositiveIntegerField(help_text="In minutes.")
    # Amount of item used.  The default measurements are by weight, but this may be the measurement in volume units.
    # If a liquid it is in liters, if a solid the weight is measured in kilograms.
    amount = models.DecimalField(help_text="Weight in Kilograms or Liters.")

    TYPE_CHOICES = [
        ('Spice', 'Spice'),
        ('Fining', 'Fining'),
        ('Water Agent', 'Water Agent'),
        ('Herb', 'Herb'),
        ('Flavor', 'Flavor'),
        ('Other', 'Other'),
    ]
    # May be “Spice”, “Fining”, “Water Agent”, “Herb”, “Flavor” or “Other”
    type = models.CharField(choices=TYPE_CHOICES)

    USE_CHOICES = [
        ('Spice', 'Spice'),
        ('Fining', 'Fining'),
        ('Water Agent', 'Water Agent'),
        ('Herb', 'Herb'),
        ('Flavor', 'Flavor'),
        ('Other', 'Other'),
    ]
    # May be “Boil”, “Mash”, “Primary”, “Secondary”, “Bottling”
    use = models.CharField(choices=USE_CHOICES)


class Waters(models.Model):
    """ This is a water profile a user creates """
    # The term "water" encompasses water profiles.  Though not strictly required for recipes,
    # the water record allows supporting programs to record the water profile used for brewing a particular batch.
    user = models.CharField(max_length=200)  # This is the user that created the object
    name = models.CharField(max_length=200, unique=True,
                            help_text="Name must be unique.")  # Name of the water profile.
    description = models.TextField(
        blank=True, help_text="Enter a description for the water profile here. Optional.")  # Notes about the water profile.  May be multiline.
    version = models.PositiveIntegerField(default=1)
    # Volume of water to use in a recipe in liters.
    amount = models.DecimalField(help_text="In Liters.")
    # The amount of calcium (Ca) in parts per million.
    calcium = models.FloatField()
    # The amount of bicarbonate (HCO3) in parts per million.
    bicarbonate = models.FloatField()
    # The amount of sulfate (SO4) in parts per million.
    sulfate = models.FloatField()
    # The amount of chloride (Cl) in parts per million.
    chloride = models.FloatField()
    # The amount of sodium (Na) in parts per million.
    sodium = models.FloatField()
    # The amount of magnesium (Mg) in parts per million.
    magnesium = models.FloatField()


class BeerRecipe(models.Model):
    """ This is a recipe that a user creates """
    # A recipe record denotes a single recipe.  A recipe record may use records from any of the previously described record formats to specify ingredients and other data.
    user = models.CharField(max_length=200)  # This is the user that created the object
    name = models.CharField(max_length=200, unique=True,
                            help_text="Name must be unique.")  # Name of the recipe.
    # Notes associated with this recipe – may be multiline.
    description = models.TextField(
        blank=True, help_text="Enter a description here. Optional")
    date_submitted = models.DateField(auto_now_add=True)
    version = models.PositiveIntegerField(default=1)
    brewer = models.CharField(max_length=64)  # Name of the brewer
    # Target size of the finished batch in liters.
    batch_size = models.DecimalField(help_text="In liters.")
    # Starting size for the main boil of the wort in liters.
    boil_size = models.DecimalField(help_text="In liters.")
    # The total time to boil the wort in minutes.
    boil_time = models.PositiveIntegerField(help_text="In minutes.")

    TYPE_CHOICES = [
        ('Extract', 'Extract'),
        ('Partial Mash', 'Partial Mash'),
        ('All Grain', 'All Grain'),
    ]  # May be one of “Extract”, “Partial Mash” or “All Grain”
    type = models.CharField(choices=TYPE_CHOICES)
    # TODO: Do I need blank=True here??
    hops = models.ManyToManyField(Hop)  # Zero or more HOP ingredient records
    # Zero or more FERMENTABLE ingredients
    fermentables = models.ManyToManyField(Fermentable)
    miscs = models.ManyToManyField(Misc)
    yeasts = models.ManyToManyField(Yeast)
    waters = models.ManyToManyField(Waters)
