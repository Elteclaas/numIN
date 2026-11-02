import serial
import serial.tools.list_ports
import time
import os
from datetime import datetime
from openpyxl import Workbook, load_workbook

# ==============================================================================
# CONFIGURACIÓN
# ==============================================================================
# Cambia 'COM3' por el puerto donde se conectó tu Arduino en tu PC
# (En Linux o Mac suele ser algo como '/dev/ttyUSB0' o '/dev/ttyACM0')
PUERTO_SERIAL = 'COM3'  
BAUDIOS = 9600

# Ruta automática hacia la carpeta data/
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_EXCEL = os.path.join(DIRECTORIO_ACTUAL, "..", "data", "registro_personas.xlsx")

# ==============================================================================
# INICIALIZACIÓN DE EXCEL
# ==============================================================================
# Asegurar que la carpeta data exista
os.makedirs(os.path.dirname(RUTA_EXCEL), exist_ok=True)

if not os.path.exists(RUTA_EXCEL):
    wb = Workbook()
    ws = wb.active
    ws.title = "Conteo"
    # Encabezados de las columnas
    ws.append(["ID Evento", "Fecha", "Hora", "Sensor", "Incremento"])
    wb.save(RUTA_EXCEL)
    print(f"[OK] Archivo creado en: {RUTA_EXCEL}")

# ==============================================================================
# CONEXIÓN SERIAL CON ARDUINO FÍSICO
# ==============================================================================
total_personas = 0

try:
    print(f"Intentando conectar con Arduino en {PUERTO_SERIAL}...")
    # Apertura del puerto USB
    arduino = serial.Serial(PUERTO_SERIAL, BAUDIOS, timeout=1)
    
    # IMPORTANTE: Al abrir el puerto serial físico, Arduino se reinicia por seguridad.
    # Debemos esperar 2 segundos a que el microcontrolador arranque.
    time.sleep(2)
    print("¡Arduino conectado con éxito! Esperando detecciones de los sensores...\n")

    while True:
        if arduino.in_waiting > 0:
            # Leer la línea enviada por el Arduino
            linea = arduino.readline().decode('utf-8', errors='ignore').strip()

            # Filtrar solo eventos válidos
            if linea in ["SENSOR_1", "SENSOR_2", "SENSOR_3"]:
                total_personas += 1
                ahora = datetime.now()
                fecha_str = ahora.strftime("%Y-%m-%d")
                hora_str = ahora.strftime("%H:%M:%S")

                print(f"[+] Cruzó una persona por {linea} a las {hora_str} | Total: {total_personas}")

                # Guardar el registro en Excel
                try:
                    wb = load_workbook(RUTA_EXCEL)
                    ws = wb["Conteo"]
                    ws.append([total_personas, fecha_str, hora_str, linea, 1])
                    wb.save(RUTA_EXCEL)
                except PermissionError:
                    print("⚠️ ALERTA: Cierra el archivo de Excel en tu computadora para permitir guardar los datos.")

except serial.SerialException as e:
    print(f"\n❌ Error al abrir el puerto {PUERTO_SERIAL}: {e}")
    print("\n--- Puertos COM disponibles detectados en tu equipo ---")
    puertos = serial.tools.list_ports.comports()
    if puertos:
        for p in puertos:
            print(f" -> {p.device} ({p.description})")
    else:
        print(" -> No se detectó ningún dispositivo conectado por USB.")
    print("------------------------------------------------------")

except KeyboardInterrupt:
    print("\nDeteniendo servidor... Conexión cerrada.")

finally:
    if 'arduino' in locals() and arduino.is_open:
        arduino.close()
