from flask import Flask, request

app = Flask(__name__)

@app.route('/capital', methods=['POST'])
def calculoJuros():
    capitalInicial = float(request.form['capitalInicial'])
    anos = float(request.form['anos'])
    porcentagemJuros = float(request.form['porcentagem'])

    def jurosAnual(anos, capitalInicial, porcentagemJuros):
        if anos < 1:
            return "Quantidade de anos informados não gerou nenhum rendimento."
        elif capitalInicial < 1:
            return "Quantidade de capital insuficiente."
        elif porcentagemJuros < 0:
            return "Porcentagem informada menor para o cálculo."
        else:
            montante = capitalInicial + (capitalInicial * (porcentagemJuros / 100) * anos)
            montante
            return montante

    imprimirDados = jurosAnual(anos, capitalInicial, porcentagemJuros)
    return f"Capital Inicial: {capitalInicial} <br>Juros (porcentagem): {porcentagemJuros} <br>Anos: {anos} <br>Valor do seu capital com juros: {imprimirDados:.2f}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

