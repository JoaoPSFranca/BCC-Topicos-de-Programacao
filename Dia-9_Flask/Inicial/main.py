from flask import Flask, render_template, request, redirect

app = Flask(__name__)
dados = []
dadosProdutos = []

@app.route("/")
def index():
    return render_template('index.html', titulo='Página Inicial')

# @app.route('/')
# def principal():
#     return 'Minha primeira aplicação Flask!<br>Menu Principal'

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html',titulo='Cadastrar')

@app.route('/cadastrarProduto')
def cadastrar_produto():
    return render_template('cadastroProduto.html',titulo='Cadastrar Produto')

@app.route('/salvar',methods=['POST'])
def salvar():
    id = int(request.form['id'])
    nome = request.form['nome']
    endereco = request.form['endereco']
    dados.append({'id': id, 'nome': nome, 'endereco': endereco})
    return redirect('/lista')

@app.route('/salvarProduto',methods=['POST'])
def salvar_produto():
    id = int(request.form['id'])
    nome = request.form['nome']
    quantidade = int(request.form['quantidade'])
    valor = float(request.form['valor'])
    dadosProdutos.append({'id': id, 'nome': nome, 'quantidade': quantidade, 'valor': valor})
    return redirect('/listaProdutos')

@app.route('/lista')
def listar():
    return render_template('lista.html',
                           lista=dados,
                           titulo='Lista de Pessoas Cadastradas')

@app.route('/listaProdutos')
def listar_produtos():
    return render_template('listaProdutos.html',
                           lista=dadosProdutos,
                           titulo='Lista de Produtos Cadastradas')

@app.route('/remover/<int:id>')
def remover(id):
    dados.pop(id-1)
    return redirect('/lista')

@app.route('/removerProduto/<int:id>')
def remover_produto(id):
    dadosProdutos.pop(id-1)
    return redirect('/listaProdutos')

@app.route('/editar/<int:id>')
def editar(id):
    pessoa = next((p for p in dados if int(p['id']) == int(id)),
                  None)
    if pessoa:
        return render_template('editar.html',
                                                 pessoa=pessoa)
    return redirect('/lista')

@app.route('/editarProduto/<int:id>')
def editar_produto(id):
    produto = next((p for p in dados if int(p['id']) == int(id)),
                  None)
    if produto:
        return render_template('editarProduto.html',
                                                 produto=produto)
    return redirect('/listaProduto')

@app.route('/atualizar', methods=['POST'])
def atualizar():
    global dados
    id = int(request.form['id'])
    nome = request.form['nome']
    endereco = request.form['endereco']

    for p in dados:
        if int(p['id']) == id:
            p['nome'] = nome
            p['endereco'] = endereco
            break
    return redirect('/lista')

@app.route('/atualizarProduto', methods=['POST'])
def atualizar_produto():
    global dados
    id = int(request.form['id'])
    nome = request.form['nome']
    quantidade = int(request.form['quantidade'])
    valor = float(request.form['valor'])

    for p in dados:
        if int(p['id']) == id:
            p['nome'] = nome
            p['quantidade'] = quantidade
            p['valor'] = valor
            break
    return redirect('/listaProdutos')

@app.route('/contato')
def contato():
    return render_template('contato.html',email='vfmaziero@hotmail.com')

@app.route('/buscar')
def buscar():
    return render_template('buscar.html')

@app.route('/resultado')
def resultado():
    try:
        id_busca = int(request.args.get('id'))
        pessoa = next((p for p in dados if int(p['id']) == int(id_busca)), None)
    except (ValueError, TypeError):
        pessoa = None
    return render_template('resultado.html', pessoa=pessoa)

if __name__ == '__main__':
    app.run(debug=True)