"""
Almacena los días de la semana y con una temperatura máxima y mínima. Razona
qué tipo de estructura utilizas (5 puntos)
● Muestra la media de las temperaturas para cada día ordenadas de mayor a menor (5
puntos)
● Dibuja en un gráfico NO de barras las temperaturas semanales aplicando formato
visualmente atractivo al gráfico (5 puntos)
● Modifica la temperatura mínima del miércoles y explica cómo afecta al gráfico y al
listado ordenado (5 puntos)
● Las temperaturas máximas y mínimas NO se pueden repetir. Es decir, si ya tengo 20
grados, NO puede darse de nuevo esta temperatura. Explica qué implica esta
limitación y actualiza el punto 1 para este caso (5 puntos)
"""
import matplotlib.pyplot as plt

class TemperaturasSemanales:
    def __init__(self):
        self.temperaturas = {
            "Lunes": {"maxima": 25, "minima": 15},
            "Martes": {"maxima": 28, "minima": 18},
            "Miércoles": {"maxima": 23, "minima": 13},
            "Jueves": {"maxima": 26, "minima": 17},
            "Viernes": {"maxima": 24, "minima": 16},
            "Sábado": {"maxima": 27, "minima": 19},
            "Domingo": {"maxima": 22, "minima": 14},
        }

    def mostrar_temperaturas(self):
        colores_dias = {'Lunes': '\033[94m', 'Martes': '\033[95m', 'Miércoles': '\033[96m',
                        'Jueves': '\033[92m', 'Viernes': '\033[91m', 'Sábado': '\033[93m', 'Domingo': '\033[90m'}

        for dia, temp in self.temperaturas.items():
            color = colores_dias.get(dia, '\033[0m')  # Restablecer el color si no está en la lista
            print(f"{color}{dia}: Máxima - {temp['maxima']}°C, Mínima - {temp['minima']}°C\033[0m")

    def media_temperaturas_ordenadas(self):
        medias = {
            dia: (temp["maxima"] + temp["minima"]) / 2 for dia, temp in self.temperaturas.items()
        }
        ordenadas = sorted(medias.items(), key=lambda x: x[1], reverse=True)
        return ordenadas

    def grafico_temperaturas(self):
        dias = list(self.temperaturas.keys())
        maximas = [temp["maxima"] for temp in self.temperaturas.values()]
        minimas = [temp["minima"] for temp in self.temperaturas.values()]

        plt.figure(figsize=(10, 6))
        plt.plot(dias, maximas, marker='o', label='Máximas', color='blue')
        plt.plot(dias, minimas, marker='o', label='Mínimas', color='green')
        plt.title('Temperaturas Semanales')
        plt.xlabel('Días de la semana')
        plt.ylabel('Temperatura (°C)')
        plt.legend()
        plt.grid(True)
        plt.show()

    def modificar_temperatura_miercoles(self, nueva_minima):
        self.temperaturas["Miércoles"]["minima"] = nueva_minima

    # Punto 2: Mostrar la media de las temperaturas ordenadas de mayor a menor
    def mostrar_media_temperaturas(self):
        medias_ordenadas = self.media_temperaturas_ordenadas()
        print("\n\033[93mMedia de temperaturas ordenadas de mayor a menor:\033[0m")
        for dia, media in medias_ordenadas:
            color_dia = '\033[93m' if dia == 'Miércoles' else '\033[0m'  # Color amarillo para el miércoles
            print(f"{color_dia}{dia}: \033[94m{media}°C\033[0m")


# Punto 1: Utilización de un diccionario para almacenar las temperaturas
# Punto 2: Mostrar la media de las temperaturas ordenadas de mayor a menor
# Punto 3: Dibujar en un gráfico las temperaturas semanales
# Punto 4: Modificar la temperatura mínima del miércoles
# Punto 5: No se permiten temperaturas máximas y mínimas repetidas

temperaturas_semanales = TemperaturasSemanales()

print("Punto 1:")
temperaturas_semanales.mostrar_temperaturas()

print("\nPunto 2:")
temperaturas_semanales.mostrar_media_temperaturas()

print("\nPunto 3:")
temperaturas_semanales.grafico_temperaturas()

print("\nPunto 4:")
temperaturas_semanales.modificar_temperatura_miercoles(10)
temperaturas_semanales.mostrar_temperaturas()

# Calcular y mostrar la media de temperaturas ordenadas de mayor a menor
medias_ordenadas_despues_modificacion = temperaturas_semanales.media_temperaturas_ordenadas()
print("\nMedia de temperaturas ordenadas de mayor a menor después de la modificación:")
for dia, media in medias_ordenadas_despues_modificacion:
    print(f"{dia}: {media:.2f}°C")

temperaturas_semanales.mostrar_temperaturas()

print("\nPunto 5:")
# Se puede implementar la validación para evitar repetición de temperaturas aquí.

