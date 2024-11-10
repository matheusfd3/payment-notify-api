from flask import Flask, jsonify, request, send_file, render_template
from repository.database import db
from models.payment import Payment
from datetime import datetime, timedelta
from payments.pix import Pix

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "MY_SECRET_KEY"

db.init_app(app)

@app.route("/payments/pix", methods=["POST"])
def create_pix_payment():
    data = request.get_json()

    if "amount" not in data:
        return jsonify({"message": "Amount is required"}), 400
    
    expiration_data = datetime.now() + timedelta(minutes=30)

    new_payment = Payment(amount=data["amount"], expiration_date=expiration_data)

    pix = Pix()
    pix_payment = pix.create_payment()

    new_payment.bank_payment_id = pix_payment["bank_payment_id"]
    new_payment.qr_code = pix_payment["qr_code_path"]

    db.session.add(new_payment)
    db.session.commit()

    return jsonify({"message": "Pix payment created", "payment": new_payment.to_dict()})

@app.route("/payments/pix/qr_code/<file_name>", methods=["GET"])
def get_qr_code(file_name):
    return send_file(f"static/qr_codes/{file_name}.png", mimetype="image/png")

@app.route("/payments/pix/confirm", methods=["POST"])
def confirm_pix_payment():
    return jsonify({"message": "Pix payment confirmed"})

@app.route("/payments/pix/<int:payment_id>", methods=["GET"])
def get_pix_payment_page(payment_id):
    payment = Payment.query.get(payment_id)
    return render_template("payment.html", 
                           payment_id=payment_id, 
                           amount=payment.amount, 
                           host="http://127.0.0.1:5000", 
                           qr_code=payment.qr_code)

if __name__ == "__main__":
    app.run(debug=True)
