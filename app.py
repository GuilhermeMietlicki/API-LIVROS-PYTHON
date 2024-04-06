# API - É um lugar para disponibilizar recursos e/ou funcionalidades
# 1. Objetivo - Criar uma API que disponibiliza a consulta, criação, edição e exclusão de livros.
# 2. URL base - Localhost.com
# 3. Endpoints - 

# - localhost/livros/(GET)
# - localhost/livros/id(GET)
# - localhost/livro/id(PUT)
# - localhost/livro/id(DELETE)
# 4. Quais recursos - Livros
from flask import Flask, jsonify, request

app = Flask (__name__)

Livros = [
{
    'id': 1,
    'título': 'O Senhor dos Anéis - A Sociedade do Anel',
    'autor': 'J.R.R Tolkien'
},
{
    'id': 2,
    'título': 'Harry Potter e a Pedra Filosofal',
     'autor': 'J.k Howling'
},
{
    'id': 3,
    'título': 'James Clear',
    'autor': 'Hábitos Atômicos'
},


]
# Consultar(todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
   return jsonify(Livros)

# Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livro:
     if livro.get('id') == id:
        return jsonify(Livros)
    

# Editar
@app.route('/livros/<int:id>/update',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(Livros):
     if livro.get('id') == id:
        livro[indice].update(livro_alterado)
    return jsonify(livro[indice])
#Criar 
@app.route('/livros',methods=['POST'])
def criar_novo_livro():

    novo_livro = request.get_json()
    Livros.append(novo_livro)
    
    return jsonify (Livros)

# Excluir
@app.route("/livros/<int:id>/delete", methods=["DELETE"])
def excluir_livro(id):
    for indice, livro in enumerate(livro):
        if livro.get('id')==id: 
            del livro [indice]
            
            return  jsonify(livro)          
       
            
            
            app.run(port=5000,host='localhost',debug=True)