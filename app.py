from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/', methods =['GET', 'POST'])
def pagina_inicial():
    km_mes = 0
    emissao = 0
    resultado = None

    if request.method == 'POST':
        distancia = float(request.form['distancia'])
        dias = int(request.form['dias'])
        transporte = float(request.form['transporte'])


        km_mes = distancia * dias * 4
        emissao = km_mes * transporte

        resultado = True

    return render_template('index.html',
                           km_mes = km_mes,
                           emissao = emissao,
                           resultado = resultado)

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')









if __name__ == '__main__':
    app.run(debug=True)