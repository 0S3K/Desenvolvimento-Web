from flask import Flask, request

app = Flask(__name__)

@app.route('/celsius', methods=['POST'])
def temperaturaCelsius():
    temperaturaCelsius = float (request.form['valorCelsius'])
    temperaturaCelsiusConvertida = (temperaturaCelsius * (9/5)) + 32
    
    return f"Temperatura informada: {temperaturaCelsius} <br> Temperatura convertida para Fahrenheit: {temperaturaCelsiusConvertida:.2f}"
        
 

@app.route('/fahrenheit', methods=['POST'])
def temperaturaFahrenheit():
    temperaturaFahrenheit = float (request.form['calcularFahrenheit'])
    temperaturaFahrenheitConvertida = (temperaturaFahrenheit - 32) * (5/9)
    
    return f"Temperatura infromada: {temperaturaFahrenheit} <br> Temperatura convertida para Celsius: {temperaturaFahrenheitConvertida:.2f}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
