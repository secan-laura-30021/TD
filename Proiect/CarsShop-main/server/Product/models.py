from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150)
    serie_sasiu = models.CharField(max_length=30, default="", unique=True)

    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)

    an_fabricatie = models.PositiveIntegerField(default=2001)
    motorizare = models.CharField(max_length=50, default="Diesel")
    caroserie = models.CharField(max_length=50, default="Sedan")
    kilometraj = models.PositiveIntegerField(default=100000)
    putere = models.PositiveIntegerField(default=101)
    capacitate_cilindrica = models.PositiveIntegerField(default=1900)
    norma_de_poluare = models.CharField(max_length=10, default="Euro 6")
    numar_portiere = models.PositiveIntegerField(default=4)
    culoare = models.CharField(max_length=25, default="Rosu")
    tara_de_origine = models.CharField(max_length=25, default="Germania")
    data_primei_inmatriculari = models.DateField(auto_now=True)
    oferit_de = models.CharField(max_length=25, default="Persoana fizica")
    stare = models.CharField(max_length=25, default="Second hand")

    image = models.ImageField(upload_to='products/%d/', default='empty.jpg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True, default="")

    def __str__(self):
        return self.name
