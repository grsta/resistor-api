from flask import Flask, request, jsonify

app = Flask(__name__)

color_codes = {
    "Black": {"digit": 0, "multiplier": 1, "tolerance": None, "temp_coeff": None},
    "Brown": {"digit": 1, "multiplier": 10, "tolerance": 1, "temp_coeff": 100},
    "Red": {"digit": 2, "multiplier": 100, "tolerance": 2, "temp_coeff": 50},
    "Orange": {"digit": 3, "multiplier": 1000, "tolerance": None, "temp_coeff": 15},
    "Yellow": {"digit": 4, "multiplier": 10000, "tolerance": None, "temp_coeff": 25},
    "Green": {"digit": 5, "multiplier": 100000, "tolerance": 0.5, "temp_coeff": None},
    "Blue": {"digit": 6, "multiplier": 1000000, "tolerance": 0.25, "temp_coeff": 10},
    "Violet": {"digit": 7, "multiplier": 10000000, "tolerance": 0.1, "temp_coeff": 5},
    "Gray": {"digit": 8, "multiplier": 100000000, "tolerance": 0.05, "temp_coeff": None},
    "White": {"digit": 9, "multiplier": 1000000000, "tolerance": None, "temp_coeff": None},
    "Gold": {"digit": None, "multiplier": 0.1, "tolerance": 5, "temp_coeff": None},
    "Silver": {"digit": None, "multiplier": 0.01, "tolerance": 10, "temp_coeff": None},
    "None": {"digit": None, "multiplier": None, "tolerance": 20, "temp_coeff": None}
}

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    band_type = data.get('bandType')
    bands = data.get('bands', [])

    try:
        digits = []
        if band_type == 4:
            digits = [color_codes[bands[0]]['digit'], color_codes[bands[1]]['digit']]
            multiplier = color_codes[bands[2]]['multiplier']
            tolerance = color_codes[bands[3]]['tolerance']
            value = int(''.join(map(str, digits))) * multiplier
            result = f"{value} Ω ±{tolerance}%"
        elif band_type == 5:
            digits = [color_codes[bands[0]]['digit'], color_codes[bands[1]]['digit'], color_codes[bands[2]]['digit']]
            multiplier = color_codes[bands[3]]['multiplier']
            tolerance = color_codes[bands[4]]['tolerance']
            value = int(''.join(map(str, digits))) * multiplier
            result = f"{value} Ω ±{tolerance}%"
        elif band_type == 6:
            digits = [color_codes[bands[0]]['digit'], color_codes[bands[1]]['digit'], color_codes[bands[2]]['digit']]
            multiplier = color_codes[bands[3]]['multiplier']
            tolerance = color_codes[bands[4]]['tolerance']
            temp_coeff = color_codes[bands[5]]['temp_coeff']
            value = int(''.join(map(str, digits))) * multiplier
            result = f"{value} Ω ±{tolerance}% {temp_coeff}ppm/°C"
        else:
            return jsonify({'error': 'Invalid band type'}), 400

        return jsonify({'resistance': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
