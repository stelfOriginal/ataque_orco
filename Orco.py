# -*- coding: utf-8 -*-
from Unidad_de_juego import Unidad_de_juego
from Funciones import *


class Orco(Unidad_de_juego):
    def __init__(self, Nombre=''):
        Unidad_de_juego.__init__(self,Nombre)
        self.max_salud = 30
        self.Medidor_salud = self.max_salud
        self.tipo_unidad = 'enemigo'
        self.numero_choza = 0

    # este codigo aun no esta ejecutado para verse 
    def info(self):
        list1 = ["Grrrr..Soy un Orco montador de huargos. Creo que esta noche serás mi cena", 
        "Tu ser apetitoso?creo que muy huesudo",
        "Mira hermano,carne con armadura,comamos!"]
        print(random.choice(list1))
