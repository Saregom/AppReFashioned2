from flask import Flask, jsonify, request
import db_controller
from db import create_tables

app = Flask(__name__)

#persona
@app.route('/personas', methods=["GET"])
def get_personas():
    personas = db_controller.get_personas()
    return jsonify(personas)


@app.route("/persona", methods=["POST"])
def insert_persona():
    persona = request.get_json()
    nombre_persona = persona["nombre_persona"]
    numero_telefonico = persona["numero_telefonico"]
    correo_persona = persona["correo_persona"]
    contraseña = persona["contraseña"]
    resultado = db_controller.insert_persona(nombre_persona, numero_telefonico, correo_persona, contraseña)
    return jsonify(resultado)


@app.route("/persona", methods=["PUT"])
def update_persona():
    persona = request.get_json()
    id_persona = persona["id_persona"]
    nombre_persona = persona["nombre_persona"]
    numero_telefonico = persona["numero_telefonico"]
    correo_persona = persona["correo_persona"]
    contraseña = persona["contraseña"]
    resultado = db_controller.update_persona(id_persona, nombre_persona, numero_telefonico, correo_persona, contraseña)
    return jsonify(resultado)


@app.route("/persona/<id_persona>", methods=["DELETE"])
def delete_persona(id_persona):
    resultado = db_controller.delete_persona(id_persona)
    return jsonify(resultado)


@app.route("/persona/<id_persona>", methods=["GET"])
def get_persona_by_id(id_persona):
    persona = db_controller.get_persona_by_id(id_persona)
    return jsonify(persona)

#direcciones

@app.route('/direcciones', methods=["GET"])
def get_direcciones():
    direcciones = db_controller.get_direcciones()
    return jsonify(direcciones)


@app.route("/direccion", methods=["POST"])
def insert_direccion():
    direccion = request.get_json()
    pais = direccion["pais"]
    ciudad = direccion["ciudad"]
    departamento = direccion["departamento"]
    codigo_postal = direccion["codigo_postal"]
    direccion = direccion["direccion"]
    complemento = direccion["complemento"]
    persona_id_persona = direccion["persona_id_persona"]
    resultado = db_controller.insert_direccion(pais, ciudad, departamento, codigo_postal, direccion, complemento, persona_id_persona)
    return jsonify(resultado)


@app.route("/direccion", methods=["PUT"])
def update_direccion():
    direccion = request.get_json()
    id_direccion = direccion["id_direccion"]
    pais = direccion["pais"]
    ciudad = direccion["ciudad"]
    departamento = direccion["departamento"]
    codigo_postal = direccion["codigo_postal"]
    direccion = direccion["direccion"]
    complemento = direccion["complemento"]
    persona_id_persona = direccion["persona_id_persona"]
    resultado = db_controller.update_direccion(id_direccion, pais, ciudad, departamento, codigo_postal, direccion, complemento, persona_id_persona)
    return jsonify(resultado)


@app.route("/direccion/<id_direccion>", methods=["DELETE"])
def delete_direccion(id_direccion):
    result = db_controller.delete_direccion(id_direccion)
    return jsonify(result)


@app.route("/direccion/<id_direccion>", methods=["GET"])
def get_direccion_by_id(id_direccion):
    direccion = db_controller.get_direccion_by_id(id_direccion)
    return jsonify(direccion)

#productos
@app.route('/productos', methods=["GET"])
def get_productos():
    productos = db_controller.get_productos()
    return jsonify(productos)


@app.route("/producto", methods=["POST"])
def insert_producto():
    producto = request.get_json()
    nombre_producto = producto["nombre_producto"]
    categoria = producto["categoria"]
    talla = producto["talla"]
    marca = producto["marca"]
    precio = producto["precio"]
    cantidad_disponible = producto["cantidad_disponible"]
    resultado = db_controller.insert_producto(nombre_producto, categoria, talla, marca, precio, cantidad_disponible)
    return jsonify(resultado)


@app.route("/producto", methods=["PUT"])
def update_producto():
    producto = request.get_json()
    id_producto = producto["id_producto"]
    nombre_producto = producto["nombre_producto"]
    categoria = producto["categoria"]
    talla = producto["talla"]
    marca = producto["marca"]
    precio = producto["precio"]
    cantidad_disponible = producto["cantidad_disponible"]
    resultado = db_controller.update_producto(id_producto, nombre_producto, categoria, talla, marca, precio, cantidad_disponible)
    return jsonify(resultado)


@app.route("/producto/<id_producto>", methods=["DELETE"])
def delete_producto(id_producto):
    result = db_controller.delete_producto(id_producto)
    return jsonify(result)


@app.route("/producto/<id_producto>", methods=["GET"])
def get_producto_by_id(id_producto):
    producto = db_controller.get_producto_by_id(id_producto)
    return jsonify(producto)

#envios
@app.route('/envios', methods=["GET"])
def get_envios():
    envios = db_controller.get_envios()
    return jsonify(envios)

@app.route("/envio/<id_envio>", methods=["GET"])
def get_envio_by_id(id_envio):
    pedido = db_controller.get_envio_by_id(id_envio)
    return jsonify(pedido)

@app.route("/envio", methods=["POST"])
def insert_envio():
    envio = request.get_json()
    fecha_envio = envio["fecha_envio"]
    fecha_entrega = envio["fecha_entrega"]
    estado_envio = envio["estado_envio"]
    direccion_id_direccion = envio["direccion_id_direccion"]
    resultado = db_controller.insert_envio(fecha_envio, fecha_entrega, estado_envio, direccion_id_direccion)
    return jsonify(resultado)

@app.route("/envio", methods=["PUT"])
def update_envio():
    envio = request.get_json()
    id_envio = envio["id_envio"]
    fecha_envio = envio["fecha_envio"]
    fecha_entrega = envio["fecha_entrega"]
    estado_envio = envio["estado_envio"]
    direccion_id_direccion = envio["direccion_id_direccion"]
    resultado = db_controller.update_envio(id_envio, fecha_envio, fecha_entrega, estado_envio, direccion_id_direccion)
    return jsonify(resultado)

@app.route("/envio/<id_envio>", methods=["DELETE"])
def delete_envio(id_envio):
    result = db_controller.delete_envio(id_envio)
    return jsonify(result)


#pedidos
@app.route('/pedidos', methods=["GET"])
def get_pedidos():
    pedidos = db_controller.get_pedidos()
    return jsonify(pedidos)


@app.route("/pedido", methods=["POST"])
def insert_pedido():
    pedido = request.get_json()
    fecha_pedido = pedido["fecha_pedido"]
    total_pedido = pedido["total_pedido"]
    persona_id_persona = pedido["persona_id_persona"]
    envio_id_envio = pedido["envio_id_envio"]
    resultado = db_controller.insert_pedido(fecha_pedido, total_pedido, persona_id_persona, envio_id_envio)
    return jsonify(resultado)


@app.route("/pedido", methods=["PUT"])
def update_pedido():
    pedido = request.get_json()
    id_pedido = pedido["id_pedido"]
    fecha_pedido = pedido["fecha_pedido"]
    total_pedido = pedido["total_pedido"]
    persona_id_persona = pedido["persona_id_persona"]
    envio_id_envio = pedido["envio_id_envio"]
    resultado = db_controller.update_pedido(id_pedido, fecha_pedido, total_pedido, persona_id_persona, envio_id_envio)
    return jsonify(resultado)


@app.route("/pedido/<id_pedido>", methods=["DELETE"])
def delete_pedido(id_pedido):
    result = db_controller.delete_pedido(id_pedido)
    return jsonify(result)


@app.route("/pedido/<id_pedido>", methods=["GET"])
def get_pedido_by_id(id_pedido):
    pedido = db_controller.get_pedido_by_id(id_pedido)
    return jsonify(pedido)

#Detalles pedidos
@app.route('/pedidoss', methods=["GET"])
def get_pedidos():
    pedidos = db_controller.get_pedidos()
    return jsonify(pedidos)


@app.route("/pedidos", methods=["POST"])
def insert_pedidos():
    detalles_pedido = request.get_json()
    cantidad_ordenada = detalles_pedido["cantidad_ordenada"]
    pedido_id_pedido = detalles_pedido["pedido_id_pedido"]
    producto_id_producto = detalles_pedido["producto_id_producto"]
    resultado = db_controller.insert_pedidos(cantidad_ordenada, pedido_id_pedido, producto_id_producto)
    return jsonify(resultado)


@app.route("/pedidos", methods=["PUT"])
def update_pedidos():
    detalles_pedido = request.get_json()
    id_detalles = detalles_pedido["id_detalles"]
    cantidad_ordenada = detalles_pedido["cantidad_ordenada"]
    pedido_id_pedido = detalles_pedido["pedido_id_pedido"]
    producto_id_producto = detalles_pedido["producto_id_producto"]
    resultado = db_controller.update_pedidos(id_detalles, cantidad_ordenada, pedido_id_pedido, producto_id_producto)
    return jsonify(resultado)


@app.route("/pedidos/<id_detalles>", methods=["DELETE"])
def delete_pedidos(id_detalles):
    result = db_controller.delete_pedidos(id_detalles)
    return jsonify(result)


@app.route("/pedidos/<id_detalles>", methods=["GET"])
def get_pedidos_by_id(id_detalles):
    pedidos = db_controller.get_pedidos_by_id(id_detalles)
    return jsonify(pedidos)

#facturas
@app.route('/facturas', methods=["GET"])
def get_facturas():
    facturas = db_controller.get_facturas()
    return jsonify(facturas)


@app.route("/factura", methods=["POST"])
def insert_facturas():
    factura = request.get_json()
    fecha_emision = factura["fecha_emision"]
    metodo_pago = factura["metodo_pago"]
    monto_total = factura["monto_total"]
    pedido_id_pedido = factura["pedido_id_pedido"]
    persona_id_persona =factura["persona_id_persona"]
    resultado = db_controller.insert_factura(fecha_emision, metodo_pago, monto_total, pedido_id_pedido, persona_id_persona)
    return jsonify(resultado)


@app.route("/factura", methods=["PUT"])
def update_factura():
    factura = request.get_json()
    id_factura = factura["id_factura"]
    fecha_emision = factura["fecha_emision"]
    metodo_pago = factura["metodo_pago"]
    monto_total = factura["monto_total"]
    pedido_id_pedido = factura["pedido_id_pedido"]
    persona_id_persona =factura["persona_id_persona"]
    resultado = db_controller.update_factura(id_factura, fecha_emision, metodo_pago, monto_total, pedido_id_pedido, persona_id_persona)
    return jsonify(resultado)


@app.route("/factura/<id_factura>", methods=["DELETE"])
def delete_factura(id_factura):
    result = db_controller.delete_factura(id_factura)
    return jsonify(result)


@app.route("/factura/<id_factura>", methods=["GET"])
def get_factura_by_id(id_factura):
    factura = db_controller.get_factura_by_id(id_factura)
    return jsonify(factura)


""" @app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response """


if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(debug=False)
