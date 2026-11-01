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
```
---

## ⚙️ Puesta en Marcha

### 1. Preparar el entorno Python
Clona este repositorio o descarga los archivos y entra a la carpeta del servidor:

```bash
cd server
pip install -r requirements.txt
```

*(Si no usas `requirements.txt`, instala manualmente: `pip install pyserial openpyxl`)*.

---

### 2. Ejecución

#### Opción A: Modo Simulación (Wokwi en VS Code)
1. Abre la carpeta del proyecto en **Visual Studio Code**.
2. Abre la paleta de comandos (`F1`) y selecciona `Wokwi: Start Simulator`.
3. En la terminal integrada, ejecuta el servidor:
   ```bash
   python server/servidor.py
   ```
4. Haz clic en cualquiera de los sensores en Wokwi y reduce la distancia por debajo del umbral (80 cm). Verás el registro en consola y se generará el archivo `registro_personas.xlsx`.

#### Opción B: Modo Físico (Arduino conectado por USB)
1. Carga `contador.ino` a tu placa Arduino desde el **Arduino IDE**.
2. Modifica en `servidor.py` la variable de conexión para apuntar a tu puerto COM físico:
   ```python
   # Cambia 'rfc2217://localhost:4000' por tu puerto real, ej: 'COM3' o '/dev/ttyUSB0'
   PUERTO_SERIAL = 'COM3'
   ```
3. Ejecuta el script:
   ```bash
   python server/servidor.py
   ```

---

## 📊 Formato del Archivo Excel Generado

Cada detección genera una fila automática en `registro_personas.xlsx` con la siguiente estructura:

| ID Evento | Fecha | Hora | Sensor | Incremento |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 2026-11-01 | 15:30:12 | SENSOR_1 | 1 |
| 2 | 2026-11-01 | 15:30:18 | SENSOR_3 | 1 |

---

## 📄 Licencia

Este proyecto está bajo la Licencia **MIT**. Consulta el archivo `LICENSE` para más información.

---
