# ⚙️ Calculadora de Motores Eléctricos según NEC

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green)

## 📌 Descripción

Herramienta de línea de comandos desarrollada en Python que automatiza el cálculo de parámetros fundamentales para motores eléctricos trifásicos, basándose en el **Código Eléctrico Nacional (NEC)** de los Estados Unidos. Ideal para ingenieros, técnicos y estudiantes que necesitan dimensionar rápidamente:

- Corriente a plena carga (FLC)
- Conductor mínimo según ampacidad
- Protección contra sobrecorriente (breaker/fusibles)
- Corriente de arranque (LRA) estimada por código NEMA

## 🚀 Funcionalidades

- ✅ Cálculo de FLC para tensiones **230V y 460V** según NEC Table 430.250.
- ✅ **Interpolación lineal** para valores de HP no incluidos en la tabla.
- ✅ Selección automática del **conductor mínimo** (NEC 310.16) con distinción correcta entre **AWG y kcmil**.
- ✅ Protección máxima recomendada para **breaker de tiempo inverso**, **fusible dual** y **fusible normal** (NEC 430.52).
- ✅ Estimación de **corriente de arranque (LRA)** según el código NEMA del motor.
- ✅ Interfaz interactiva por terminal, fácil de usar.

## 🛠️ Tecnologías utilizadas

- **Python 3** (lenguaje principal)
- Módulos estándar (sin dependencias externas)

## 📦 Instalación y uso

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Miguel-Cardenas92/calculadora-motores-nec.git

2. Accede a la carpeta del proyecto:

cd calculadora-motores-nec

3. Ejecuta el programa:

python3 calculadora_motores_nec_version3.py

4. Sigue las instrucciones en pantalla: ingresa la potencia en HP, el voltaje (230 o 460) y, si lo deseas, el código NEMA para estimar la corriente de arranque.


CALCULADORA DE MOTORES SEGÚN NEC - Ing. Miguel Cárdenas

Potencia del motor (HP): 20

Voltaje (230 o 460): 460

   Corriente a plena carga (FLC): 27.0 A
   Conductor mínimo (125% de FLC): 10 AWG

Tipo de protección (breaker/fusible_dual/fusible_normal) [breaker]: breaker
   
   Protección máxima recomendada: 70 A

¿Estimar corriente de arranque (LRA)? (s/n) [s]: s

Código NEMA del motor (B,C,D,E,F,G,H,J) [G]: B

   Corriente de arranque estimada (LRA): 94 A

  
 ## 📚 Aprendizajes y contexto
   
Este proyecto surgió durante mi preparación para procesos de selección en el área de ingeniería electromecánica. Me enfrenté a la necesidad de realizar cálculos repetitivos según normativa, y decidí automatizarlos con Python. Este desafío me permitió:

Profundizar en la normativa NEC aplicada a motores.

Mejorar mis habilidades en Python (manejo de datos, funciones, lógica condicional).

Aprender a usar Git y GitHub para compartir y versionar código.

Desarrollar una herramienta práctica que puede ser útil para otros profesionales.

## 🤝 Contribuciones

Las sugerencias y mejoras son bienvenidas. Si encuentras algún error o tienes una idea para ampliar la funcionalidad, no dudes en abrir un issue o enviar un pull request.

## 📬 Contacto

Ing. Miguel Cárdenas

LinkedIn: https://www.linkedin.com/in/miguel-angel-cardenas-alonso-5b9b59248/

Correo: miguelcardenasalonso@gmail.com
