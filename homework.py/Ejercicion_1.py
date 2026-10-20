class AlmacenSemillas:
    def __init__(self, cantidad):
        self.__cantidad = cantidad          # atributo privado

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:             # solo si no es negativa
            self.__cantidad = nueva_cantidad
        else:
            print("Error: la cantidad no puede ser negativa.")

    def entregar_semillas(self, cantidad):
        if cantidad <= self.__cantidad:     # hay suficientes
            self.__cantidad -= cantidad
            print(f"Se entregaron {cantidad} semillas.")
        else:
            print(f"No hay suficientes semillas para entregar {cantidad}.")


# 7. Crear objeto con 10 semillas
almacen = AlmacenSemillas(10)

# 8. Entregas
print("Entrega a Goku:")
almacen.entregar_semillas(3)      # quedan 7

print("Entrega a Yajirobe:")
almacen.entregar_semillas(9)      # 9 > 7, se rechaza

# 9. Cantidad final
print(f"Cantidad final disponible: {almacen.get_cantidad()}")