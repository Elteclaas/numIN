import serial
import time
import os
from datetime import datetime
from openpyxl import Workbook, load_workbook

# Configuración con RFC2217 hacia Wokwi
DIRECCION_WOKWI = 'rfc2217://localhost:4000'
BAUDIOS = 9600
NOMBRE_EXCEL = "registro_personas.xlsx"

# Inicializar o verificar archivo Excel
if not os.path.exists(NOMBRE_EXCEL):
    wb = Workbook()
    ws = wb.active
    ws.title = "Conteo"
    ws.append(["ID Evento", "Fecha", "Hora", "Sensor", "Incremento"])
    wb.save(NOMBRE_EXCEL)
    print(f"Archivo {NOMBRE_EXCEL} creado.")

total_contador = 0

try:
    # serial_for_url permite conectar vía RFC2217 al simulador
    print(f"Conectando a Wokwi en {DIRECCION_WOKWI}...")
    arduino = serial.serial_for_url(DIRECCION_WOKWI, baudrate=BAUDIOS, timeout=1)
    time.sleep(1)
    print("¡Conexión establecida con éxito! Esperando detecciones en la simulación...")

    while True:
        if arduino.in_waiting > 0:
            linea = arduino.readline().decode('utf-8', errors='ignore').strip()
            
            if linea in ["SENSOR_1", "SENSOR_2", "SENSOR_3"]:
                total_contador += 1
                ahora = datetime.now()
                fecha_str = ahora.strftime("%Y-%m-%d")
                hora_str = ahora.strftime("%H:%M:%S")

                print(f"[+] Detección en {linea} a las {hora_str} | Total: {total_contador}")

                # Guardar en Excel
                wb = load_workbook(NOMBRE_EXCEL)
                ws = wb["Conteo"]
                ws.append([total_contador, fecha_str, hora_str, linea, 1])
                wb.save(NOMBRE_EXCEL)

except serial.SerialException as e:
    print(f"Error al conectar con Wokwi: {e}")
    print("Asegúrate de haber iniciado la simulación en VS Code antes de ejecutar este script.")
except KeyboardInterrupt:
    print("\nScript detenido.")
finally:
    if 'arduino' in locals() and arduino.is_open:
        arduino.close()