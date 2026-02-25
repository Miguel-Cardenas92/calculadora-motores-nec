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
