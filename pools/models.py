from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Equipo(models.Model):
    equipo_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    logo = models.CharField(max_length=100, null=True)
    class Meta:
        db_table = u'equipo'
    def __unicode__(self):
        return self.nombre

class Torneo(models.Model):
    torneo_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    logo = models.CharField(max_length=100, null=True)
    class Meta:
        db_table = u'torneo'
    def __unicode__(self):
        return self.nombre

class Quiniela(models.Model):
    quiniela_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    usuario = models.ForeignKey(User, db_column='usuario')
    torneo = models.ForeignKey(Torneo, db_column='torneo')
    logo = models.CharField(max_length=100, null=True)
    class Meta:
        db_table = u'quiniela'
    def __unicode__(self):
        return self.nombre

#Clasificados a un torneo
class Clasificado(models.Model):
    clasificado_id = models.AutoField(primary_key=True)
    equipo = models.ForeignKey(Equipo, db_column='equipo')
    torneo = models.ForeignKey(Torneo, db_column='torneo')
    grupo = models.CharField(max_length=200)
    class Meta:
        db_table = u'clasificado'
    def __unicode__(self):
        return self.equipo.nombre

class Partido(models.Model):
    partido_id = models.AutoField(primary_key=True)
    equipoLocal = models.ForeignKey(Equipo, db_column='equipo_local')
    equipoVisitante = models.ForeignKey(Equipo, related_name='equipo_visitante')
    torneo = models.ForeignKey(Torneo, db_column='torneo')
    fase = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=300)
    fecha = models.DateField(null=True,default=None)
    golesLocal = models.IntegerField(null=True)
    golesVisitante = models.IntegerField(null=True)
    golesPenaltyLocal = models.IntegerField(null=True)
    golesPenaltyVisitante = models.IntegerField(null=True)
    realizado = models.IntegerField(default=0)
    class Meta:
        db_table = u'partido'
    def __unicode__(self):
        return self.descripcion

class Prediccion(models.Model):
    prediccion_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, db_column='usuario')
    partido = models.ForeignKey(Partido, db_column='partido')
    quiniela = models.ForeignKey(Quiniela, db_column='quiniela')
    golesLocal = models.IntegerField(null=True)
    golesVisitante = models.IntegerField(null=True)
    golesPenaltyLocal = models.IntegerField(null=True)
    golesPenaltyVisitante = models.IntegerField(null=True)
    puntos = models.IntegerField(default=0)
    class Meta:
        db_table = u'prediccion'
    def __unicode__(self):
        return self.partido.descripcion


