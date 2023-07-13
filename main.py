from flask import Flask, render_template, url_for, redirect, request, session, jsonify
from config import config
from db.db_connection import create_tables
import db.db_controller as db_controller
import data_controllers.person_controller as person_cont
from datetime import date
from datetime import timedelta

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/login')

@app.route("/personaPost", methods=["POST"])
def insert_persona():
    persona = request.get_json()
    nombre_persona = persona["nombre_persona"]
    numero_telefonico = persona["numero_telefonico"]
    tipo_persona = persona["tipo_persona"]
    correo_persona = persona["correo_persona"]
    contraseña = persona["contraseña"]
    resultado = db_controller.insert_persona(nombre_persona, numero_telefonico, tipo_persona, correo_persona, contraseña)
    return jsonify(resultado)

@app.route('/personasGet', methods=["GET"])
def get_personas():
    personas = db_controller.get_personas()
    return jsonify(personas)

@app.route('/direccionesGet', methods=["GET"])
def get_direcciones():
    direcciones = db_controller.get_direcciones()
    return jsonify(direcciones)

@app.route("/productoPost", methods=["POST"])
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

@app.route("/direccionPost", methods=["POST"])
def insert_direccion():
    direccion = request.get_json()
    pais = direccion["pais"]
    ciudad = direccion["ciudad"]
    departamento = direccion["departamento"]
    codigo_postal = direccion["codigo_postal"]
    direccion2 = direccion["direccion"]
    complemento = direccion["complemento"]
    persona_id_persona = direccion["persona_id_persona"]
    resultado = db_controller.insert_direccion(pais, ciudad, departamento, codigo_postal, direccion2, complemento, persona_id_persona)
    return jsonify(resultado)

@app.route("/pedidoDel/<id_pedido>", methods=["DELETE"])
def delete_pedido(id_pedido):
    result = db_controller.delete_pedido(id_pedido)
    return jsonify(result)

@app.route('/enviosGet', methods=["GET"])
def get_envios():
    envios = db_controller.get_envios()
    return jsonify(envios)



@app.route('/login', methods=['GET', 'POST'])
def login():
    response = [False, '']
    if request.method == 'POST':
        response = person_cont.verifyClient(request.form['email'], request.form['password'])
        if response[0]:
            session['user_id'] = response[2]
            session['user_type'] = response[3]
            return redirect('/home')

    return render_template('login.html', alert = response[1])


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    response = [False, '']
    if request.method == 'POST':
        response = person_cont.verifyClientRegister(request.form)
        if response[0]:
            session['user_id'] = response[2]
            session['user_type'] = response[3]
            return redirect('/home')
    
    return render_template('signin.html', alert = response[1])


@app.route('/home')
def home():
    return render_template('home.html')

class cart():
    cartProducts = []
    
    @classmethod
    def addProduct(cls, product):
        id = 1
        if len(cls.cartProducts) != 0:
            for cartProduct in cls.cartProducts:
                id = int(cartProduct['id'])+1 

        cls.cartProducts.append({'id':id, 'product':product})
    
    @classmethod
    def delProduct(cls, id):
        for cartProduct in cls.cartProducts:
            if cartProduct['id'] == id:
                cls.cartProducts.remove(cartProduct)
                return
            
    @classmethod
    def doOrder(cls):
        for i in range(len(cls.cartProducts)):  
            cls.cartProducts.pop()

@app.route('/addProduct/<int:idProd>', methods=['POST'])
def addProduct(idProd):
    if request.method == 'POST':
        product = db_controller.get_producto_by_id(idProd)
        cart.addProduct({'id_producto':idProd, 'precio':int(product[5]), 'nombre':product[1], 'cantidad':int(request.form['quantity'])})
        
    return redirect('/products')

@app.route('/delProduct/<int:id>', methods=['POST'])
def delProduct(id):
    cart.delProduct(id)
    return redirect('/products')


@app.route('/products', methods=['GET', 'POST'])
def products():
    products = []
    products = person_cont.formatProductos(db_controller.get_productos())
    
    if request.method == 'POST':
        if request.form["talla"] != "on" and request.form["talla"] != "todas":
            products = person_cont.formatProductos(db_controller.get_productos_by_talla(request.form["talla"]))
        
    return render_template('products.html', products = products, cartProducts = cart.cartProducts)


@app.route('/manage-products', methods=['GET', 'POST'])
def adminProducts():
    
    if request.method == 'POST':
        data = request.form
        db_controller.insert_producto(data["nombre_producto"],data["categoria"],data["talla"], data["marca"], data["precio"], data["cantidad_disponible"])
        # return redirect('/home')
    products = person_cont.formatProductos(db_controller.get_productos())
    return render_template('manage-products.html', products = products, cartProducts = cart.cartProducts) 


@app.route('/orders', methods=['GET', 'POST'])
def orders():
    # if request.method == 'POST':
    person_cont.doOrder(cart.cartProducts)
    cart.doOrder()
    
    orders = person_cont.formatPedidos(db_controller.get_pedidos_by_id_persona(session['user_id']))
    orderDetails = person_cont.formatDetallesPedido(db_controller.get_detalles_pedidos())
    products = person_cont.formatProductos(db_controller.get_productos())

    return render_template('orders.html', orders = orders, orderDetails = orderDetails, products = products)

@app.route('/shipments')
def shipments():
    orders = person_cont.formatPedidos(db_controller.get_pedidos_by_id_persona(session['user_id']))
    adresses = person_cont.formatDirecciones(db_controller.get_direccion_by_id_persona(session['user_id']))
    shipments = person_cont.formatEnvios(db_controller.get_envios_by_id_persona(session['user_id']))

    return render_template('shipments.html', shipments = shipments, orders = orders, adress = adresses[0])

@app.route('/manage-shipments')
@app.route('/manage-shipments/<int:idShip>', methods=['POST'])
def manageShipment(idShip = None):
    if request.method == 'POST':
        fechaHoy = date.today()
        db_controller.update_envio(idShip, fechaHoy, fechaHoy + timedelta(days=5), 'Enviando')

    orders = person_cont.formatPedidos(db_controller.get_pedidos())
    adresses = person_cont.formatDirecciones(db_controller.get_direcciones())
    shipments = person_cont.formatEnvios(db_controller.get_envios_pendientes())
    
    return render_template('manageShipments.html', shipments = shipments, orders = orders, adresses = adresses)

@app.route('/account')
def account():
    users = person_cont.formatPersonas(db_controller.get_persona_by_id(session["user_id"]))
    adresses = person_cont.formatDirecciones(db_controller.get_direccion_by_id_persona(session['user_id']))

    return render_template('account.html', user = users[0], adress = adresses[0])


@app.route('/update-account', methods=['GET', 'POST'])
def updateAccount():
    if request.method == 'POST':
        data = request.form
        
        db_controller.update_persona(session['user_id'], data['name'], data['cellphone'])
        adress = person_cont.formatDirecciones(db_controller.get_direccion_by_id_persona(session['user_id']))
        dataAd = adress[0]
        db_controller.update_direccion(dataAd['id_direccion'], data['country'], data['city'], data['department'], data['postal_code'], data['adress'], data['aditional_info'])

        return redirect('/account')
    
    users = person_cont.formatPersonas(db_controller.get_persona_by_id(session["user_id"]))
    adresses = person_cont.formatDirecciones(db_controller.get_direccion_by_id_persona(session['user_id']))

    return render_template('updateAccount.html', user = users[0], adress = adresses[0])


@app.route('/logout')
def logout():
   session.pop('user_id', None) 
   session.pop('user_type', None)
   return redirect('/login')


if __name__ == '__main__':
    create_tables()
    app.config.from_object(config['development'])
    app.run(debug=True)