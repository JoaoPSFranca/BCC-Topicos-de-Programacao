from datetime import date
from model.ItemVenda import ItemVenda
from controller.Controller import Controller

def mostrarProdutos(produtos):
    for produto in produtos:
        print(f"Codigo: {produto.codproduto}\nNome: {produto.nome}\nPreço: {produto.preco}\n")

def listarProdutos():
    control = Controller("produtos")
    produtos = control.list_all()
    if produtos != -1:
        mostrarProdutos(produtos)
    return produtos

def cadastrarCliente():
    nome = input("Informe o nome do cliente: ")
    endereco = input("Informe o endereco do cliente: ")
    return nome, endereco

def cadastrarProduto():
    nome = input("Informe o nome do produto: ")
    preco = input("Informe o preco do produto: ")
    return nome, preco

def validarCliente(cli, clientes):
    for cliente in clientes:
        if cliente.codcliente == int(cli):
            return False

    return True

def validarProduto(prod, produtos):
    for produto in produtos:
        if produto.codproduto == int(prod):
            return False

    return True

def removerProduto(produtos, code):
    prod = None
    for produto in produtos:
        if int(produto.codproduto) == code:
            prod = produto
            produtos.remove(produto)
            break
    return produtos, prod

def cadastrarItemVenda(codigo, produtos):
    print("Produtos Disponiveis: ")
    mostrarProdutos(produtos)

    while True:
        prod = int(input("Informe o código do produto: "))
        if validarProduto(prod, produtos):
            print("Informe um código válido. ")
        else:
            break

    quantidade = int(input("Informe o quantidade de produtos: "))
    produtos, produto = removerProduto(produtos, prod)

    return ItemVenda(codigo, prod, quantidade, (quantidade * produto.preco)), produtos

def formatarItemsVenda(items):
    string = f"{items[0].codvenda} \\ {items[0].codproduto} \\ {items[0].qtde} \\ {items[0].valor} "
    for item in items[1:]:
        string += f"/ {item.codvenda} \\ {item.codproduto} \\ {item.qtde} \\ {item.valor} "
    return string

def cadastrarVenda():
    items = []
    control = Controller("vendas")

    code = control.max_code() + 1

    data_atual = date.today()
    data = data_atual.strftime('%d/%m/%Y')

    cliControl = Controller("clientes")
    clientes = cliControl.list_all()

    while True:
        cli = input("Informe código do cliente: ")
        if validarCliente(cli, clientes):
            print("Informe um código de cliente válido. ")
        else:
            break

    total = 0

    verify = True
    produtos = listarProdutos()

    while verify and produtos:
        item, produtos = cadastrarItemVenda(code, produtos)
        total += item.valor
        items.append(item)
        resp = input("Deseja cadastrar mais um item? 's' para continuar: ")
        if resp.lower() != "s":
            verify = False

        print()

    iv = formatarItemsVenda(items)

    return code, data, total, cli, iv

def mostrarClientes(clientes):
    print("\nLista de Clientes: \n")
    for cliente in clientes:
        print(f"Codigo: {cliente.codcliente}\nNome: {cliente.nome}\nEndereço: {cliente.endereco}\n")

def mostrarItemVendas(itemVendas):
    prodControl = Controller("produtos")
    produtos = prodControl.list_all()

    print("Items: ")
    for item in itemVendas:
        produtos, prod = removerProduto(produtos, int(item.codproduto))
        print(f"Produto: {prod.nome}  |  Quantidade: {item.qtde}  |  Valor: {item.valor}")

    print()

def mostrarVenda(venda):
    cliControl = Controller("clientes")
    cliente = cliControl.get_entity(venda.codcliente)

    print(f"\nCodigo: {venda.codvenda}\nData: {venda.data}\nCliente: {cliente.nome}\n")
    mostrarItemVendas(venda.itens)
    print(f"Valor Total: {venda.valor_total}\n")

def mostrarVendas(vendas):
    for venda in vendas:
        mostrarVenda(venda)

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
    if opt == 1:
        control = Controller("clientes")
        nome, endereco = cadastrarCliente()
        code = control.max_code() + 1
        control.save(f"{code} | {nome} | {endereco}\n")
        print()
    elif opt == 2:
        control = Controller("produtos")
        nome, preco = cadastrarProduto()
        code = control.max_code() + 1
        control.save(f"{code} | {nome} | {preco}\n")
        print()
    elif opt == 3:
        control = Controller("clientes")
        clientes = control.list_all()
        if clientes != -1:
            mostrarClientes(clientes)
    elif opt == 4:
        print("\nLista de Produtos: \n")
        listarProdutos()
    elif opt == 5:
        control = Controller("vendas")

        cliControl = Controller("clientes")
        clientes = cliControl.list_all()

        while True:
            codigo = input("Informe o codigo do cliente: ")
            if validarCliente(codigo, clientes):
                print("Informe um código válido. ")
            else:
                break

        vendas = control.list_vendas_cliente(codigo)

        if vendas != -1:
            if vendas:
                mostrarVendas(vendas)
            else:
                print("\nNenhuma venda encontrada relacionada ao cliente. \n")
    elif opt == 6:
        control = Controller("vendas")

        cliControl = Controller("clientes")
        clientes = cliControl.list_all()

        while True:
            codigo = input("Informe o codigo do cliente: ")
            if validarCliente(codigo, clientes):
                print("Informe um código válido. ")
            else:
                break

        numero_venda = int(input("Informe o número da venda: "))
        venda = control.venda_cliente(codigo, numero_venda)

        if venda != -1:
            if venda is None:
                print(f"Venda não encontrada. ")
            else:
                mostrarVenda(venda)
    elif opt == 7:
        control = Controller("vendas")
        code, data, total, cli, iv = cadastrarVenda()
        control.save(f"{code} | {data} | {total} | {cli} | {iv}\n")

if __name__ == '__main__':
    print("Bem vindo ao mini Sistema de Vendas. ")
    verify = True

    while verify:
        op = menu()
        if op == 0:
            verify = False
        else:
            opcoes(op)
