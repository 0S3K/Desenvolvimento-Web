from flask import Flask, request
#Calcular area e perimetro de um retangulo
app = Flask(__name__)


@app.route('/atividade03_Exercicio01', methods=['POST'])
def calcularRetangulo():
    largura = (float(request.form['largura']))
    altura = (float(request.form['altura']))
    area = (largura * altura)
    perimetro = (2 * (largura + altura))

    if largura > 0 and altura > 0:
        return f"Largura: {largura} <br> Altura: {altura} <br> Área: {area} <br> Perímetro: {perimetro}"
    return "Informe números positivos maiores que zero"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
