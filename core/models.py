from django.db import models


class Client(models.Model):
    clientid = models.AutoField(primary_key=True)
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    adresa = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'clienti'
        managed = False

    def __str__(self):
        return f"{self.nume} {self.prenume}"


class Producator(models.Model):
    producatorid = models.AutoField(primary_key=True)
    denumire = models.CharField(max_length=150)
    tara_origine = models.CharField(max_length=100, blank=True, null=True, db_column='taraorigine')
    adresa = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'producatori'
        managed = False

    def __str__(self):
        return self.denumire


class ProdusAlimentar(models.Model):
    produsid = models.AutoField(primary_key=True)
    denumire = models.CharField(max_length=150)
    data_producere = models.DateField(db_column='dataproducere')
    data_expirare = models.DateField(db_column='dataexpirare')

    class Meta:
        db_table = 'produsalimentar'
        managed = False

    def __str__(self):
        return self.denumire


class ClientProdus(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='clientid')
    produs = models.ForeignKey(ProdusAlimentar, on_delete=models.CASCADE, db_column='produsid')

    class Meta:
        db_table = 'client_produs'
        unique_together = ("client", "produs")
        managed = False

    def __str__(self):
        return f"{self.client} -> {self.produs}"


class ProdusProducator(models.Model):
    produs = models.ForeignKey(ProdusAlimentar, on_delete=models.CASCADE, db_column='produsid')
    producator = models.ForeignKey(Producator, on_delete=models.CASCADE, db_column='producatorid')

    class Meta:
        db_table = 'produs_producator'
        unique_together = ("produs", "producator")
        managed = False

    def __str__(self):
        return f"{self.produs} -> {self.producator}"
