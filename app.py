from flask import Flask, render_template, request

app = Flask(__name__)


conteudos = []
registros = []

@app.route('/', methods=['GET', 'POST'])
def principal(): 
    if request.method == 'POST':
        conteudos.append(request.form.get('conteudo'))
    return render_template('index.html',
                            conteudos=conteudos
                           )


@app.route('/diario', methods=['GET', 'POST'])  
def diario():
    if request.method == 'POST':
        if request.form.get('aluno') and request.form.get('nota'):
            aluno = request.form.get('aluno')
            nota = request.form.get('nota')
            registros.append({
                'aluno': aluno,
                'nota': nota
            })
    return render_template('sobre.html', registros=registros)

app.run(debug=True)