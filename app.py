from flask import Flask, jsonify
from repository.database import db
from models.payment import Payment

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "MY_SECRET_KEY"

db.init_app(app)

@app.route("/payments/pix", methods=["POST"])
def create_pix_payment():
    return jsonify({"message": "Pix payment created"})

@app.route("/payments/pix/confirm", methods=["POST"])
def confirm_pix_payment():
    return jsonify({"message": "Pix payment confirmed"})

@app.route("/payments/pix/<int:payment_id>", methods=["GET"])
def get_pix_payment_page(payment_id):
    return "Pix payment page"

if __name__ == "__main__":
    app.run(debug=True)
