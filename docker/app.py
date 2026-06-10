import os

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "sqlite:////data/users.db",
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)


@app.before_request
def create_tables():
    db.create_all()


@app.get("/")
def index():
    users = User.query.order_by(User.id.asc()).all()
    return render_template("index.html", users=users)


@app.post("/users")
def add_user():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()

    if name and email:
        exists = User.query.filter_by(email=email).first()
        if not exists:
            db.session.add(User(name=name, email=email))
            db.session.commit()

    return redirect(url_for("index"))


@app.post("/users/<int:user_id>/delete")
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
