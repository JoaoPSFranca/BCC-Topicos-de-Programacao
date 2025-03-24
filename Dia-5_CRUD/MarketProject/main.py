from datetime import date
from model.Sale import Sale
from model.ItemSale import ItemSale
from model.Client import Client
from model.Product import *
from controller.ControllerDefault import Controller

def validate_client():
    control = Controller()

    while True:
        cli = Client()
        cli.idclient = int(input("Informe código do cliente: "))
        if control.search(cli) is None:
            print("Informe um código de cliente válido. ")
        else:
            return cli

def create_client():
    client = Client()
    client.name = input("Informe o nome do cliente: ")
    client.address = input("Informe o endereco do cliente: ")
    client.city = input("Informe a Cidade do cliente: ")
    client.uf = input("Informe o UF do cliente: ")
    client.cep = input("Informe o CEP: ")

    return client

def create_product():
    prod = Product()
    prod.name = input("Informe o nome do produto: ")
    prod.amount = input("Informe a quantidade de produtos: ")
    prod.price = input("Informe o valor do produto: ")
    return prod

def show_clients():
    control = Controller()
    clients = control.search_all(Client())

    if len(clients) == 0:
        print("Nenhum cliente cadastrado. ")
        return

    print("\nLista de Clientes: \n")
    for client in clients:
        print(f"Codigo: {client.idclient}")
        print(f"Nome: {client.name}")
        print(f"Endereço: {client.address}")
        print(f"Cidade: {client.city}")
        print(f"UF: {client.uf}")
        print(f"CEP: {client.cep}")
        print(f"Crédito: {client.credit}")
        print(f"Balanço: {client.balance}\n")

def show_products():
    control = Controller()
    products = control.search_all(Product())

    if len(products) == 0:
        print("Nenhum producto cadastrado. ")
        return

    for product in products:
        print(f"Codigo: {product.idproduct}")
        print(f"Nome: {product.name}")
        print(f"Quantidade: {product.amount}")
        print(f"Preço: {product.price}\n")

def show_item_sale(items):
    print("\nItems: ")
    for item in items:
        print(f"Produto: {item.product.name}  |  Quantidade: {item.amount}  |  Valor: {item.price}")

def show_sale(sale):
    print(f"Código: {sale.idsale}")
    print(f"Data: {sale.date_str()}")
    print(f"Cliente: {sale.client.name}")
    show_item_sale(sale.items)
    print(f"\nValor Total: {sale.valor_total}")

def show_sales(sales):
    for sale in sales:
        show_sale(sale)

def create_item_sale(sale):
    item = ItemSale()
    control = Controller()

    while True:
        prod = Product()
        prod.idproduct = int(input("Informe o código do produto: "))
        prod = control.search(prod)
        if prod is None:
            print("Informe um código válido. ")
        else:
            break

    item.product = prod
    item.idsale = sale.idsale
    item.amount = int(input("Informe o quantidade de produtos: "))
    item.price = item.amount * prod.price

    sale.total += item.price

    return item

def create_sale():
    sale = Sale()
    control = Controller()

    actual_date = date.today()
    sale.date = actual_date.strftime('%d/%m/%Y')

    sale.client = validate_client()

    sale.idsale = control.max_code(sale) + 1
    sale.total = 0
    while True:
        sale.items.append(create_item_sale(sale))
        resp = input("Deseja cadastrar mais um item? 's' para continuar: ")
        print()
        if resp.lower() != "s":
            break

    return sale

def get_sales():
    control = Controller()
    sale = Sale()
    sale.client = validate_client()
    return control.search_sale_client(sale)

def menu():
    print(f"""Menu:
1 - Cadastrar cliente
2 - Cadastrar produto
3 - Listar clientes
4 - Listar produtos
5 - Listar vendas de um cliente
6 - Mostrar venda específica de um cliente
7 - Efetuar venda para um cliente
0 - Sair
""")
    try:
        opt = input("Opção desejada: ")
        opt = int(opt)
        if opt > 7 or opt < 0:
            print("Opção inválida. Informe valores entre 0 e 7")
        else:
            return opt
    except KeyboardInterrupt:
        print("Era só ter digitado 0 cara. ")
    except Exception as e:
        print(f"Algo deu errado: {str(e)}")
    return -1

def opcoes(opt):
    # Criar Cliente V
    if opt == 1:
        control = Controller()
        client = create_client()
        client.idclient = control.max_code(client) + 1
        control.insert(client)
        print()

    # Criar Produto V
    elif opt == 2:
        control = Controller()
        prod = create_product()
        prod.idproduct = control.max_code(prod) + 1
        control.insert(prod)
        print()

    # Mostrar Clientes V
    elif opt == 3:
        show_clients()

    # Mostrar Produtos V
    elif opt == 4:
        print("\nLista de Produtos: \n")
        show_products()

    # Listar Vendas de um Cliente V
    elif opt == 5:
        sales = get_sales()

        if len(sales) == 0:
            print(f"Nenhuma venda cadastrada no cliente especificado. ")
        else:
            show_sales(sales)

    # Mostrar Venda específica de um cliente V
    elif opt == 6:
        sales = get_sales()
        number_sale = int(input("Informe o número da venda: "))

        if len(sales) == 0:
            print(f"Venda não encontrada. ")

            if number_sale <= 0 or number_sale >= len(sales):
                print("Número da venda inválido. ")
            else:
                show_sale(sales[number_sale - 1])

    # Criar Venda V
    elif opt == 7:
        control = Controller()
        sale = create_sale()
        control.insert(sale)

if __name__ == '__main__':
    print("Bem vindo ao mini Sistema de Vendas. ")
    verify = True

    while verify:
        op = menu()
        if op == 0:
            verify = False
        else:
            opcoes(op)
