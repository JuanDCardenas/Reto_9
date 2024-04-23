import math
pi= math.pi
if __name__ == "__main__":
    radio_esfera=float(input("Escribe el radio de la esfera: "))
    radio_cono=float(input("Escribe el radio de el cono: "))
    altura_cono=float(input("Escribe la altura del cono: "))
    volumen= lambda radio_esfera, radio_cono, altura_cono: ((4/3)*pi*(radio_esfera)**3)+((1/3)*pi*(radio_cono)**2*(altura_cono))
    total_volumen= volumen(radio_esfera, radio_cono, altura_cono)
    area= lambda radio_esfera, radio_cono, altura_cono: (4*pi*(radio_esfera)**2)+(pi*(radio_cono)*((radio_cono**2+altura_cono**2)**0.5)+pi*(radio_cono)**2)
    total_area= area(radio_esfera, radio_cono, altura_cono)
    print(f"El volumen de la figura es igual a {total_volumen}" )
    print(f"El area de la figura es igual a {total_area}")