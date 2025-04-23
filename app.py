from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/analisar-textura", methods=["POST"])
def analisar_textura():
    data = request.get_json()
    texto = data.get("texto", "")
    if not texto:
        return jsonify({"erro": "Texto não fornecido"}), 400

    resultado = {
        "sonoridade": "Textura sonora intensa, com aliterações em R e S.",
        "estrutura_frasal": "Frases curtas, com ritmo firme e pausas claras.",
        "escolha_lexical": "Vocabulário sensorial e simbólico como 'rugoso' e 'cálido'.",
        "ambiguidade": "Expressões poéticas com interpretações múltiplas.",
        "cadencia_temporal": "Ritmo acelerado com uso intencional de pausas.",
        "conotacao_cultural": "Referências culturais de resiliência e sensibilidade.",
        "relatorio_geral": "Texto com alta textura linguística, evocativo e simbólico."
    }
    return jsonify(resultado)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "versao": "1.0.0",
        "autor": "Professor Doutor Fernando Antonio Dal Piero"
    })

if __name__ == "__main__":
    app.run(debug=True)
