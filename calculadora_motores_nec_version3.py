# calculadora_motores_nec_final.py
"""
Calculadora de parámetros de motores según NEC
Ing. Miguel Cárdenas - Proyecto de demostración
Versión final con correcciones de nomenclatura AWG/kcmil
"""

def flc_nec(hp, voltaje, fases=3):
    """
    Retorna corriente a plena carga (FLC) aproximada según NEC Table 430.250
    (Motores trifásicos, 60Hz)
    """
    # Datos para motores típicos a 230V y 460V (NEC Table 430.250)
    tablas_230v = {
        1: 3.4, 2: 6.8, 3: 9.6, 5: 15.2, 7.5: 22, 10: 28, 15: 42,
        20: 54, 25: 68, 30: 80, 40: 104, 50: 130, 60: 154, 75: 192,
        100: 248, 125: 312, 150: 360, 200: 480
    }
    tablas_460v = {
        1: 1.7, 2: 3.4, 3: 4.8, 5: 7.6, 7.5: 11, 10: 14, 15: 21,
        20: 27, 25: 34, 30: 40, 40: 52, 50: 65, 60: 77, 75: 96,
        100: 124, 125: 156, 150: 180, 200: 240
    }
    
    if voltaje == 230:
        tabla = tablas_230v
    elif voltaje == 460:
        tabla = tablas_460v
    else:
        return f"Voltaje {voltaje}V no soportado (usa 230 o 460)"
    
    if hp in tabla:
        return tabla[hp]
    else:
        # Interpolación lineal para valores intermedios
        hp_list = sorted(tabla.keys())
        for i in range(len(hp_list)-1):
            if hp_list[i] < hp < hp_list[i+1]:
                flc1 = tabla[hp_list[i]]
                flc2 = tabla[hp_list[i+1]]
                return flc1 + (flc2 - flc1) * (hp - hp_list[i]) / (hp_list[i+1] - hp_list[i])
        return "HP fuera de rango"

def proteccion_nec(flc, tipo="breaker"):
    """
    Calcula protección máxima según NEC 430.52
    tipo: "breaker" (250%), "fusible_dual" (175%), "fusible_normal" (300%)
    """
    factores = {
        "breaker": 2.5,
        "fusible_dual": 1.75,
        "fusible_normal": 3.0
    }
    if tipo not in factores:
        return "Tipo no válido"
    
    proteccion_max = flc * factores[tipo]
    # Tamaños estándar de protecciones según NEC 240.6
    tamanos_estandar = [15,20,25,30,35,40,45,50,60,70,80,90,100,110,125,150,175,200,225,250,300,350,400,450,500,600,700,800,1000,1200]
    for tam in tamanos_estandar:
        if tam >= proteccion_max:
            return tam
    return proteccion_max

def conductor_minimo(flc):
    """
    Calcula calibre mínimo de conductor según NEC 310.16 (cobre, 75°C)
    Retorna calibre AWG/kcmil como string correctamente identificado
    """
    # Tabla de ampacidad (cobre 75°C) con calibres mixtos (int para AWG, string para >4/0)
    tabla_conductores = [
        (14, 20), (12, 25), (10, 35), (8, 50), (6, 65), (4, 85), (3, 100),
        (2, 115), (1, 130), ("1/0", 150), ("2/0", 175), ("3/0", 200), ("4/0", 230),
        (250, 255), (300, 285), (350, 310), (400, 335), (500, 380)
    ]
    
    # NEC 430.22: conductor dimensionado al 125% de FLC
    corriente_requerida = flc * 1.25
    
    for calibre, amp in tabla_conductores:
        if amp >= corriente_requerida:
            # Determinar si es kcmil (calibre >= 250 y es entero) o AWG
            if isinstance(calibre, int) and calibre >= 250:
                return f"{calibre} kcmil"
            else:
                return f"{calibre} AWG"
    return "Calibre > 500 kcmil requerido"

def lra_estimada(flc, codigo_nema="G"):
    """
    Estima corriente de rotor bloqueado (LRA) según código NEMA
    Códigos: B (3-3.5x), C (3.5-4x), D (4-5x), E (4-5x), F (5-6x), G (6-7x)
    """
    factores = {
        "B": 3.5, "C": 4.0, "D": 4.5, "E": 4.5, "F": 5.5, "G": 6.5, "H": 7.5, "J": 8.0
    }
    factor = factores.get(codigo_nema.upper(), 6.0)
    return flc * factor

# --- INTERFAZ PRINCIPAL ---
if __name__ == "__main__":
    print("="*60)
    print("CALCULADORA DE MOTORES SEGÚN NEC - Ing. Miguel Cárdenas")
    print("="*60)
    
    try:
        hp = float(input("Potencia del motor (HP): "))
        voltaje = int(input("Voltaje (230 o 460): "))
        
        flc = flc_nec(hp, voltaje)
        if isinstance(flc, str):
            print(f"Error: {flc}")
        else:
            print(f"\n📊 RESULTADOS:")
            print(f"   Corriente a plena carga (FLC): {flc:.1f} A")
            
            conductor = conductor_minimo(flc)
            print(f"   Conductor mínimo (125% de FLC): {conductor}")
            
            tipo_prot = input("\nTipo de protección (breaker/fusible_dual/fusible_normal) [breaker]: ") or "breaker"
            prot = proteccion_nec(flc, tipo_prot)
            print(f"   Protección máxima recomendada: {prot} A")
            
            resp = input("\n¿Estimar corriente de arranque (LRA)? (s/n) [s]: ") or "s"
            if resp.lower() == "s":
                codigo = input("Código NEMA del motor (B,C,D,E,F,G,H,J) [G]: ") or "G"
                lra = lra_estimada(flc, codigo)
                print(f"   Corriente de arranque estimada (LRA): {lra:.0f} A")
    except ValueError:
        print("Error: Ingresa valores numéricos válidos (usa punto para decimales).")
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")
