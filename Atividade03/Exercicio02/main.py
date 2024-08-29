from flask import Flask, request

app = Flask(__name__)

@app.route('/raiz', methods=['POST'])
def calcular_raiz():
    numeroRaiz = float(request.form['numeroRaiz'])

    def imprimirRaiz(numeroRaiz):
        calculoRaiz = numeroRaiz ** 0.5
        if calculoRaiz.is_integer():
            return f"Raiz quadrada de {numeroRaiz} é: {int(calculoRaiz)}"
        else:
            return f"A raiz quadrada de {numeroRaiz} é aproximadamente: {calculoRaiz:.2f}"

    resultadoRaiz = imprimirRaiz(numeroRaiz)
    return resultadoRaiz

@app.route('/potencia', methods=['POST'])
def calcular_potencia():
    base = float(request.form['base'])
    expoente = float(request.form['expoente'])

    def imprimirPotencia(base, expoente):
        calcularPotencia = base ** expoente
        return f"{base} elevado à potência {expoente} é: {calcularPotencia}"

    resultadoPotencia = imprimirPotencia(base, expoente)
    return resultadoPotencia

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
