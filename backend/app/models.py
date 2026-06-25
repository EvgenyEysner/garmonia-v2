from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField("Kategorie", max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"


class Treatment(models.Model):
    name = models.CharField("Name", max_length=255)
    category = models.ForeignKey(
        Category, verbose_name="Kategorie", on_delete=models.CASCADE
    )
    description = models.TextField("Beschreibung", null=True, blank=True)
    price = models.CharField(
        "Preise", max_length=20, null=True
    )  # charField for entries such as, for example, 60€ or more

    class Meta:
        ordering = ["category"]
        verbose_name = "Behandlung"
        verbose_name_plural = "Behandlungen"

    def __str__(self):
        return self.name


class MonthlyOffer(models.Model):
    treatment = models.ForeignKey(
        Treatment,
        on_delete=models.CASCADE,
        verbose_name="Monatliches Angebot",
    )
    title = models.CharField("Angebotsbezeichnung", max_length=128)
    description = models.TextField("Angebotsbeschreibung")
    image = models.ImageField(verbose_name="Angebotsbild", upload_to="offers")
    active = models.BooleanField("Angebot aktiv?", default=False)
    price = models.DecimalField("Preise", max_digits=10, decimal_places=2, null=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Angebot"
        verbose_name_plural = "Angebote"

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    first_name = models.CharField("Vorname", max_length=64)
    last_name = models.CharField("Nachname", max_length=64)
    text = models.TextField("Bewertung")
    rating = models.IntegerField(
        "Bewertung", default=5, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        ordering = ("last_name",)
        verbose_name = "Bewertung"
        verbose_name_plural = "Bewertungen"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class GalleryImage(models.Model):
    image = models.ImageField(verbose_name="Galeriebild", upload_to="gallery")
    description = models.CharField("Kurzbeschreibung", max_length=28)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Bild"
        verbose_name_plural = "Bilder"
