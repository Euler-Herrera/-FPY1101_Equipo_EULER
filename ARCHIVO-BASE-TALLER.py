
import os
os.system("cls")



# Función de EULER HERRERA
def calcular_rectangulo():
    print("\n--- CALCULAR RECTÁNGULO ---")
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    area = largo * ancho
    perimetro = 2 * (largo + ancho)
    print(f"Área: {area:.2f}")
    print(f"Perímetro: {perimetro:.2f}")


# Funciones persoales (presentación del grupo)
def hola_soy_Euler():
    print("Hola ¿que tal? Mi nombre es Euler HERRERA, soy el lider de este equipo y soy" \
    "un joven de 50 años. soy profesor de artes marciales, mi especialidad es Ninjutsu," \
    "tambien soy tatuador profesional aunque yo no tengo tatuajes, pero me gusta el arte de dibujar" \
    "y lo practico bien. Tambien creo contenido sobre auto superación masculina y escribo sobre el tema")


def nota_para_profesor():
    print("Hola profe, he creado este programa que es muy sencillo porque" \
    "es hasta donde aún llega mi comprensión de aprendizaje, esperando cumpla con" \
    "lo solicitado. Se que me faltaron mas comprobaciones pero ya se me hacia mas largo y complejo" \
    "y preferí que fuese al menos funcional")

# Menú base del programa
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Calcular rectángulo")
    print("2. Convertir temperatura")
    print("3. Convertir kilómetros a millas")
    print("4. Ver Perfil EULER HERRERA")
    print("5. Ver Perfil PANCHO PISTOLAS")
    print("6. Ver Perfil SEÑOR BOLAINAS")
    print("7. NOTA PARA EL PROFESOR")
    print("0. Salir")

    
    op = input("Seleccione opción: ")
    if op == "0":
        print("   ")
        print("     😎💖😎💖😎💖😎💖😎💖    ")
        print("GRACIAS POR USAR MI SENSUAL PROGRAMA.")
        print("====================================")
    
        print("     😁 VUELVE PRONTO. 😁")
        print("====================================")
        print("   😎 HASTA LA VISTA BABY. 😎")
        print("   ")
        
        break
    elif op == "1":
        calcular_rectangulo()
    elif op == "2":
        convertir_temperatura()
    elif op == "3":
        convertir_kilometros_a_millas()
    elif op == "4":
        hola_soy_Euler()
    elif op == "5":
        hola_soy_pancho_pistolas()
    elif op == "6":
        hola_soy_el_señor_bolainas()
    elif op == "7":
        nota_para_profesor()
    else:
        print("Opción inválida.")

















