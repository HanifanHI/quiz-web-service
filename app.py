from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/hitung", methods=["POST"])
def hitung():
    berat = float(request.form['berat'])
    tinggi = float(request.form["tinggi"])

    bmi = berat / (tinggi/100)**2

    if bmi < 18.5:
        ket = 'Kurus'
    elif bmi > 18.5 and bmi < 25:
        ket = 'Normal'
    elif bmi > 25 and bmi < 40:
        ket = 'Berlebih'
    else:
        ket = 'Bahaya'
    
    hasil = {"BMI": bmi, "Keterangan": ket, "response": 200}
    return jsonify(hasil)

if __name__ == '__main__':
    app.run(debug = True, port=8080)