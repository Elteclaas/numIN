# 🚶‍♂️ numIN - Contador de Personas Inteligente

**numIN** es un sistema de conteo de aforo y flujo de personas basado en hardware abierto. Utiliza un microcontrolador **Arduino UNO**, tres sensores ultrasónicos independientes para monitorear diferentes accesos/carriles, retroalimentación sonora inmediata (buzzer) y un servidor en **Python** que consolida el registro de accesos en tiempo real dentro de una hoja de cálculo de Microsoft Excel (`.xlsx`).

El proyecto incluye soporte completo para simulación local o en la nube mediante **Wokwi**.

---

## 🚀 Características

* **Monitoreo multizona:** Control simultáneo de hasta 3 carriles o accesos independientes con sensores HC-SR04.
* **Filtro antirebote (Debounce):** Algoritmo por software para evitar conteos duplicados si una persona se detiene frente al sensor.
* **Feedback sonoro:** Emisión de un tono corto (*bip*) cada vez que se detecta un cruce válido.
* **Registro automatizado:** Script de Python que captura los eventos y guarda marca temporal (Fecha, Hora, ID de Sensor) en Excel sin intervención manual.
* **Listo para simular:** Configurado para ejecutarse en Wokwi (Web o extensión de VS Code) sin necesidad de hardware físico.

---

## 🛠️ Tecnologías y Componentes

* **Hardware:**
  * Arduino UNO (o equivalente ATmega328P).
  * 3x Sensores ultrasónicos HC-SR04.
  * 1x Buzzer (piezoeléctrico activo o pasivo).
* **Software:**
  * Arduino IDE / C++
  * Python 3.x
  * Librerías Python: `pyserial`, `openpyxl`
  * Simulador Wokwi (con protocolo RFC2217)

---

## 🔌 Esquema de Conexiones

| Componente | Pin del Componente | Pin Arduino UNO |
| :--- | :--- | :--- |
| **Sensor 1** | VCC / GND | 5V / GND |
| | TRIG / ECHO | Pin 2 / Pin 3 |
| **Sensor 2** | VCC / GND | 5V / GND |
| | TRIG / ECHO | Pin 4 / Pin 5 |
| **Sensor 3** | VCC / GND | 5V / GND |
| | TRIG / ECHO | Pin 6 / Pin 7 |
| **Buzzer** | Positivo (+) / GND (-) | Pin 8 / GND |

---

## 📁 Estructura del Repositorio

```text
numIN/
├── firmware/
│   ├── contador.ino             # Código de Arduino
│   └── contador.ino.hex         # Binario compilado para Wokwi
├── simulation/
│   ├── diagram.json             # Circuito visual para Wokwi
│   └── wokwi.toml               # Configuración de puerto virtual (RFC2217)
├── server/
│   ├── servidor.py              # Receptor de eventos y guardado en Excel
│   └── requirements.txt         # Dependencias de Python
├── LICENSE                      # Licencia MIT
└── README.md                    # Documentación del proyecto
