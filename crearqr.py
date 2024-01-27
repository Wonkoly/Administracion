# pip install qrcode
# pip install pillow

# Importar la libreria
import qrcode

# Crear la clase
class Qr():
    # Implementar el constructor
    def __init__(self):
        super().__init__()

    # Metodo para generar el qr
    def crear_nuevo_qr(self, curp, rol):
        # Algoritmo para crear el QR
        qr = qrcode.QRCode(error_correction = qrcode.constants.ERROR_CORRECT_H)
        # String con los datos del QR
        codigo = curp + "-" + rol
        # Añadir el codigo al QR
        qr.add_data(codigo)
        # Crear el QR
        qr.make()
        # Generar la imagen
        qrimg = qr.make_image(fill_color="#000000", back_color="#FFFFFF").convert("RGB")

        # Guardar la imagen
        ruta = "C:/Users/soporte/Desktop/Python BD/Administracion"

        if rol == "Administrativo":
            qrimg.save(f"{ruta}/Administrativos/{codigo}.png")
        elif rol == "Estudiante":
            qrimg.save(f"{ruta}/Estudiantes/{codigo}.png")
        elif rol == "Externo":
            qrimg.save(f"{ruta}/Externos/{codigo}.png")
        elif rol == "Operativo":
            qrimg.save(f"{ruta}/Operativos/{codigo}.png")
        elif rol == "Profesor":
            qrimg.save(f"{ruta}/Profesores/{codigo}.png")

        print("QR generado con exito")
