# -*- coding: utf-8 -*-
from Unidad_de_juego import Unidad_de_juego
from Funciones import *

class Arquero(Unidad_de_juego):
    def __init__(self,Nombre='Sir Legolas'):
        Unidad_de_juego.__init__(self, Nombre)
        self.max_salud = 30
        self.Medidor_salud = self.max_salud
        self.tipo_unidad = 'amigo'

    def info(self):
        print("Soy el heroe del bosque,el arquero de la reina de la noche y mis enemigos solo muescas a mia arco")


        