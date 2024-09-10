function calcularJuros() {
    // Obter os valores dos campos
    let capital = parseFloat(document.getElementById('capital').value);
    let taxa = parseFloat(document.getElementById('taxa').value) / 100;
    let tempo = parseFloat(document.getElementById('tempo').value);

    let montante = capital * Math.pow((1 + taxa), tempo);

    document.getElementById('resultado').innerText = "Montante Acumulado (M): R$ $" + montante.toFixed(2);
}