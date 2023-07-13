from db.db_connection import get_db

# ---------------- persona ----------------
def get_personas():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_persona, nombre_persona, numero_telefonico, tipo_persona, correo_persona, contraseña FROM personas"
    cursor.execute(query)
    return cursor.fetchall()

def get_persona_by_id(id_persona):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_persona, nombre_persona, numero_telefonico, tipo_persona, correo_persona, contraseña FROM personas WHERE id_persona = ?"
    cursor.execute(query, [id_persona])
    return cursor.fetchall()

def get_actual_persona(correo_persona):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_persona, tipo_persona FROM personas WHERE correo_persona = ?"
    cursor.execute(query, [correo_persona])
    return cursor.fetchone()

def insert_persona(nombre_persona, numero_telefonico, tipo_persona, correo_persona, contraseña):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO personas(nombre_persona, numero_telefonico, tipo_persona, correo_persona, contraseña) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, [nombre_persona, numero_telefonico, tipo_persona, correo_persona, contraseña])
    db.commit()
    return True

def update_persona(id_persona, nombre_persona, numero_telefonico):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE personas SET nombre_persona = ?, numero_telefonico = ? WHERE id_persona = ?"
    cursor.execute(query, [nombre_persona, numero_telefonico, id_persona])
    db.commit()
    return True

def delete_persona(id_persona):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM personas WHERE id_persona = ?"
    cursor.execute(query, [id_persona])
    db.commit()
    return True


# ---------------- DIRECCION ----------------
def get_direcciones():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_direccion, pais, ciudad, departamento, codigo_postal, direccion, complemento, persona_id_persona FROM direcciones"
    cursor.execute(query)
    return cursor.fetchall()

def get_direccion_by_id(id_direccion):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT pais, ciudad, departamento, codigo_postal, direccion, complemento, persona_id_persona FROM direcciones WHERE id_direccion = ?"
    cursor.execute(query, [id_direccion])
    return cursor.fetchone()

def get_direccion_by_id_persona(id_persona):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_direccion, pais, ciudad, departamento, codigo_postal, direccion, complemento, persona_id_persona FROM direcciones WHERE persona_id_persona = ?"
    cursor.execute(query, [id_persona])
    return cursor.fetchall()

def insert_direccion(pais, ciudad, departamento, codigo_postal, direccion, complemento, persona_id_persona):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO direcciones(pais, ciudad, departamento, codigo_postal, direccion, complemento, persona_id_persona) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(query, [pais, ciudad, departamento, codigo_postal, direccion, complemento, persona_id_persona])
    db.commit()
    return True

def update_direccion(id_direccion, pais, ciudad, departamento, codigo_postal, direccion, complemento):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE direcciones SET pais = ?, ciudad = ?, departamento = ?, codigo_postal = ?, direccion = ?, complemento = ? WHERE id_direccion = ?"
    cursor.execute(query, [pais, ciudad, departamento, codigo_postal, direccion, complemento, id_direccion])
    db.commit()
    return True

def delete_direccion(id_direccion):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM direcciones WHERE id_direccion = ?"
    cursor.execute(query, [id_direccion])
    db.commit()
    return True


# ---------------- PRODUCTOS ----------------
def get_productos():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_producto, nombre_producto, categoria, talla, marca, precio, cantidad_disponible FROM productos"
    cursor.execute(query)
    return cursor.fetchall()

def get_producto_by_id(id_producto):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_producto, nombre_producto, categoria, talla, marca, precio, cantidad_disponible FROM productos WHERE id_producto = ?"
    cursor.execute(query, [id_producto])
    return cursor.fetchone()

def get_productos_by_talla(talla):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_producto, nombre_producto, categoria, talla, marca, precio, cantidad_disponible FROM productos WHERE talla = ?"
    cursor.execute(query, [talla])
    return cursor.fetchall()

def insert_producto(nombre_producto, categoria, talla, marca, precio, cantidad_disponible):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO productos(nombre_producto, categoria, talla, marca, precio, cantidad_disponible) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(query, [nombre_producto, categoria, talla, marca, precio, cantidad_disponible])
    db.commit()
    return True

def update_producto(id_producto, nombre_producto, categoria, talla, marca, precio, cantidad_disponible):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE productos SET nombre_producto = ?, categoria = ?, talla = ?, marca = ?, precio = ?, cantidad_disponible = ? WHERE id_producto = ?"
    cursor.execute(query, [nombre_producto, categoria, talla, marca, precio, cantidad_disponible, id_producto])
    db.commit()
    return True

def delete_producto(id_producto):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM productos WHERE id_producto = ?"
    cursor.execute(query, [id_producto])
    db.commit()
    return True





# ---------------- ENVIOS ----------------
def get_envios():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_envio, fecha_envio, fecha_entrega, estado_envio, direccion_id_direccion FROM envios"
    cursor.execute(query)
    return cursor.fetchall()

def get_envios_pendientes():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_envio, fecha_envio, fecha_entrega, estado_envio, direccion_id_direccion FROM envios WHERE estado_envio = 'Pendiente'"
    cursor.execute(query)
    return cursor.fetchall()

def get_envio_by_id(id_envio):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_envio, fecha_envio, fecha_entrega, estado_envio , direccion_id_direccion FROM envios WHERE id_envio = ?"
    cursor.execute(query, [id_envio])
    return cursor.fetchone()

def get_actual_envio():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT MAX(id_envio) FROM envios"
    cursor.execute(query)
    return cursor.fetchone()

def get_envios_by_id_persona(persona_id_persona):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_envio, fecha_envio, fecha_entrega, estado_envio, direccion_id_direccion FROM envios, pedidos WHERE pedidos.persona_id_persona = ? AND pedidos.envio_id_envio = envios.id_envio" 
    cursor.execute(query, [persona_id_persona])
    return cursor.fetchall()

def insert_envio(fecha_envio, fecha_entrega, estado_envio, direccion_id_direccion):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO envios(fecha_envio, fecha_entrega, estado_envio, direccion_id_direccion) VALUES (?, ?, ?, ?)"
    cursor.execute(query, [fecha_envio, fecha_entrega, estado_envio, direccion_id_direccion])
    db.commit()
    return True


def update_envio(id_envio, fecha_envio, fecha_entrega, estado_envio):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE envios SET fecha_envio = ?, fecha_entrega = ?, estado_envio = ? WHERE id_envio = ?"
    cursor.execute(query, [fecha_envio, fecha_entrega, estado_envio, id_envio])
    db.commit()
    return True


def delete_envio(id_envio):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM envios WHERE id_envio = ?"
    cursor.execute(query, [id_envio])
    db.commit()
    return True


# ---------------- PEDIDOS ----------------
def get_pedidos():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_pedido, fecha_pedido, total_pedido, persona_id_persona, envio_id_envio FROM pedidos"
    cursor.execute(query)
    return cursor.fetchall()

def get_pedido_by_id(id_pedido):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_pedido, fecha_pedido, total_pedido, persona_id_persona, envio_id_envio FROM pedidos WHERE id_pedido = ?"
    cursor.execute(query, [id_pedido])
    return cursor.fetchone()

def get_actual_pedido():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT MAX(id_pedido) FROM pedidos"
    cursor.execute(query)
    return cursor.fetchone()

def get_pedidos_by_id_persona(persona_id_persona):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_pedido, fecha_pedido, total_pedido, persona_id_persona, envio_id_envio FROM pedidos WHERE persona_id_persona = ?"
    cursor.execute(query, [persona_id_persona])
    return cursor.fetchall()

def insert_pedido(fecha_pedido, total_pedido, persona_id_persona, envio_id_envio):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO pedidos(fecha_pedido, total_pedido, persona_id_persona, envio_id_envio) VALUES (?, ?, ?, ?)"
    cursor.execute(query, [fecha_pedido, total_pedido, persona_id_persona, envio_id_envio])
    db.commit()
    return True

def update_pedido(id_pedido, fecha_pedido, total_pedido, persona_id_persona, envio_id_envio):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE pedidos SET fecha_pedido = ?, total_pedido = ?,  persona_id_persona = ?, envio_id_envio = ? WHERE id_pedido = ?"
    cursor.execute(query, [fecha_pedido, total_pedido, persona_id_persona, envio_id_envio, id_pedido ])
    db.commit()
    return True

def delete_pedido(id_pedido):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM pedidos WHERE id_pedido = ?"
    cursor.execute(query, [id_pedido])
    db.commit()
    return True




# ---------------- DETALLES PEDIDOS ----------------
def get_detalles_pedidos():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_detalles, cantidad_ordenada, pedido_id_pedido, producto_id_producto FROM detalles_pedidos"
    cursor.execute(query)
    return cursor.fetchall()

def get_detalles_pedidos_by_id(id_detalles):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_detalles, cantidad_ordenada, pedido_id_pedido, producto_id_producto FROM detalles_pedidos WHERE id_detalles = ?"
    cursor.execute(query, [id_detalles])
    return cursor.fetchone()

def insert_detalles_pedidos(cantidad_ordenada, pedido_id_pedido, producto_id_producto):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO detalles_pedidos(cantidad_ordenada, pedido_id_pedido, producto_id_producto) VALUES (?, ?, ?)"
    cursor.execute(query, [cantidad_ordenada, pedido_id_pedido, producto_id_producto])
    db.commit()
    return True


def update_detalles_pedidos(id_detalles, cantidad_ordenada, pedido_id_pedido, producto_id_producto):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE detalles_pedidos SET cantidad_ordenada = ?, pedido_id_pedido = ?, producto_id_producto = ? WHERE id_detalles = ?"
    cursor.execute(query, [cantidad_ordenada, pedido_id_pedido, producto_id_producto, id_detalles ])
    db.commit()
    return True


def delete_detalles_pedidos(id_detalles):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM detalles_pedidos WHERE id_detalles = ?"
    cursor.execute(query, [id_detalles])
    db.commit()
    return True




