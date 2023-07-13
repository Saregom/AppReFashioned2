import db.db_controller as db_controller
from flask import session
from datetime import date
from datetime import timedelta

# ---------------- PERSONAS ----------------
def formatPersonas(persons):
    personas = []
    for persona in persons:
        persona = {
            "id_persona": persona[0],
            "nombre_persona": persona[1],
            "numero_telefonico": persona[2],
            "tipo_persona": persona[3],
            "correo_persona": persona[4],
            "contraseña": persona[5]
        }
        personas.append(persona)
    return personas


def verifyClient(email, password):
    PERSONAS = formatPersonas(db_controller.get_personas())
    correcto = False

    for persona in PERSONAS:
        if persona['correo_persona'] == email and persona['contraseña'] == password:
            print(persona)
            correcto = True
    
    if correcto:
        personaActual = db_controller.get_actual_persona(email)
        
        return [True, 'Acceso concedido', personaActual[0], personaActual[1]]
    else:
        return [False, 'Datos invalidos']
        
def verifyClientRegister(data):
    PERSONAS = formatPersonas(db_controller.get_personas())

    for persona in PERSONAS:
        if persona['correo_persona'] == data['email']:
            return [False, 'Correo ya existe']
        if data['password'] != data['confirm_password']: 
            return [False, 'Las contraseñas no coinciden']

    db_controller.insert_persona(data['name'], data['cellphone'], 'CLIENTE', data['email'], data['password'])
    personaActual = db_controller.get_actual_persona(data['email'])
    db_controller.insert_direccion(data['country'], data['city'], data['department'], data['postal_code'], data['adress'], data['aditional_info'], personaActual[0])

    return [True, 'Cuenta creada', personaActual[0], personaActual[1]]

# ---------------- DIRECCIONES ----------------
def formatDirecciones(adresses):
    direcciones = []
    for direccion in adresses:
        direccion = {
            "id_direccion": direccion[0],
            "pais": direccion[1],
            "ciudad": direccion[2],
            "departamento": direccion[3],
            "codigo_postal": direccion[4],
            "direccion": direccion[5],
            "complemento": direccion[6],
            "persona_id_persona": direccion[7]
        }
        direcciones.append(direccion)
    return direcciones

# ---------------- PRODUCTOS ----------------
def formatProductos(products):
    productos = []
    for producto in products:
        producto = {
            "id_producto": producto[0],
            "nombre_producto": producto[1],
            "categoria": producto[2],
            "talla": producto[3],
            "marca": producto[4],
            "precio": producto[5],
            "cantidad_disponible": producto[6]
        }
        productos.append(producto)
    return productos

# ---------------- PEDIDOS ----------------
def formatPedidos(orders):
    pedidos = []
    for pedido in orders:
        pedido = {
            "id_pedido": pedido[0],
            "fecha_pedido": pedido[1],
            "total_pedido": pedido[2],
            "persona_id_persona": pedido[3],
            "envio_id_envio": pedido[4]
        }
        pedidos.append(pedido)
    return pedidos


def doOrder(cartProducts):
    total = 0
    if len(cartProducts) != 0:
        fechaHoy = date.today()

        direccion = db_controller.get_direccion_by_id_persona(session["user_id"])
        db_controller.insert_envio('Pendiente', 'Pendiente', "Pendiente", direccion[0][0])

        for order in cartProducts:
            product = order['product']
            total += product["precio"]*product["cantidad"]
        
        envio_actual = db_controller.get_actual_envio()
        db_controller.insert_pedido(fechaHoy, total, session["user_id"], envio_actual[0])

        pedido_actual = db_controller.get_actual_pedido()
        for order in cartProducts:
            product = order['product']
            db_controller.insert_detalles_pedidos(product["cantidad"], pedido_actual[0], product["id_producto"])


# ---------------- DETALLE PEDIDO ----------------
def formatDetallesPedido(details):
    detalles = []
    for detalle in details:
        detalle = {
            "id_detalles": detalle[0],
            "cantidad_ordenada": detalle[1],
            "pedido_id_pedido": detalle[2],
            "producto_id_producto": detalle[3]
        }
        detalles.append(detalle)
    return detalles

# ---------------- ENVIOS ----------------
def formatEnvios(shipments):
    envios = []
    for envio in shipments:
        envio = {
            "id_envio": envio[0],
            "fecha_envio": envio[1],
            "fecha_entrega": envio[2],
            "estado_envio": envio[3],
            "direccion_id_direccion": envio[4]
        }
        envios.append(envio)
    return envios