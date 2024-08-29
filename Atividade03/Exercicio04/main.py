from flask import Flask, request

app = Flask(__name__)

@app.route('/IMC', methods=['POST'])
def calcularIMC():
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])
    imc = peso / (altura ** 2)
    
    def conversaoIMC(peso, altura):
        if peso <= 0:
            return "Peso deve ser maior que 0."
        elif altura <= 0:
            return "Altura informada deve ser maior que 0."
        else:
            return imc
    
    def faixaIndice(imc):
        if imc < 18.5:
            return "Abaixo do peso."
        elif imc < 24.9:
            return "Peso normal."
        elif imc < 29.9:
            return "Sobrepeso."
        else:
            return "Obesidade."
    
    informacaoIMC = conversaoIMC(peso, altura)


    informacaoIndice = faixaIndice(imc)
    
    return f"Seu IMC é {informacaoIMC:.2f}. Classificação: {informacaoIndice}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
