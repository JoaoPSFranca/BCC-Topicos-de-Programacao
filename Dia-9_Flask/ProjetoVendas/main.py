from flask import Flask, render_template, request, redirect
from model.Client import Client
from model.Sale import Sale
from model.Product import Product
from model.ItemSale import SaleItem
from dao.ControllerDefault import Controller

app = Flask(__name__)
controller = Controller()
clients = []
products = []
sales = []
itemSales = []

@app.route('/clients/create')
def client_create():
    return render_template('clients/create.html',
                           titulo='Criar Cliente')

@app.route('/clients')
def client_list():
    # clients = controller.search_all(Client())
    # print(clients)
    cli = Client()
    cli.idclient = 1
    cli.name = 'Lucas'
    cli.address = 'Rua 1'
    clients.append(cli)
    return render_template('clients/list.html',
                           clients=clients,
                           active_page='clients')

@app.route('/index')
def old_index():
    return render_template('Index.html', titulo='Index')

@app.route("/")
def index():
    # clients = controller.search_all(Client())
    # print(clients)
    # products = controller.search_all(Product())
    # print(products)
    # sales = controller.search_all(Sale())
    # print(sales)
    # itemSales = controller.search_all(SaleItem())
    # print(itemSales)
    # return render_template('Index.html', titulo='Index', clients=clients, products=products, sales=sales)
    dashboard_data = {
        "total_clientes": len(clients),
        "total_produtos": len(products),
        "total_vendas": len(sales)
    }
    return render_template('home.html', data=dashboard_data)

if __name__ == '__main__':
    app.run(debug=True)