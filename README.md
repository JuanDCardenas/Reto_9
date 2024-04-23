# Reto_9
```python
import math
pi= math.pi
if __name__ == "__main__":
    #reto6 punto1
    radio_esfera=float(input("Escribe el radio de la esfera: "))
    radio_cono=float(input("Escribe el radio de el cono: "))
    altura_cono=float(input("Escribe la altura del cono: "))
    volumen= lambda radio_esfera, radio_cono, altura_cono: ((4/3)*pi*(radio_esfera)**3)+((1/3)*pi*(radio_cono)**2*(altura_cono))
    total_volumen= volumen(radio_esfera, radio_cono, altura_cono)
    area= lambda radio_esfera, radio_cono, altura_cono: (4*pi*(radio_esfera)**2)+(pi*(radio_cono)*((radio_cono**2+altura_cono**2)**0.5)+pi*(radio_cono)**2)
    total_area= area(radio_esfera, radio_cono, altura_cono)
    print(f"El volumen de la figura es igual a {total_volumen}" )
    print(f"El area de la figura es igual a {total_area}")

    #reto 6 punto 2
    radio_circulos=float(input("Escribe un radio para los circulos: "))
    lado_a=float(input("Escribe un lado a para el rectangulo: "))
    lado_b=float(input("Escribe un lado b para el rectangulo: "))
    area= lambda radio_circulos,lado_a,lado_b: (2*pi*(radio_circulos**2))+(lado_a*lado_b)
    area_total=area(radio_circulos,lado_a,lado_b)
    perimetro= lambda radio_circulos,lado_a,lado_b: (2*lado_a+2*lado_b)+(2*pi*radio_circulos)
    perimetro_total=perimetro(radio_circulos,lado_a,lado_b)
    print(f"El area de la figura es de {area_total}")
    print(f"El perimetro de la figura es igual a {perimetro_total}")

    #reto 6 punto 3
    gallinas=float(input("Escribe cuantas gallinas se pesaran: "))
    gallos=float(input("Escribe cuantos gallos se pesaran: "))
    pollitos=float(input("Escribe cuantos pollitos se pesaran: "))
    carnes= lambda gallinas,gallos,pollitos: gallinas*6+gallos*7+pollitos
    kilos=carnes(gallinas,gallos,pollitos)
    print(f"En total se tienen {kilos} de carne")
    
```
