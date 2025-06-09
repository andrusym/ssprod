
from flask import Flask, request, jsonify
from bots.order_executor import execute_order
from bots.ml_engine import score_strategy

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return "SkyStrike backend is live", 200

@app.route('/score', methods=['POST'])
def score():
    data = request.get_json()
    result = score_strategy(data)
    return jsonify(result)

@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()
    response = execute_order(data)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8501)
