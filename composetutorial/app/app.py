from flask import Flask, redirect, url_for, request, render_template, make_response, session, abort, flash
from flask_sqlalchemy import SQLAlchemy
import json
from flask import render_template

app = Flask(__name__)
app.secret_key = 'ABCDDD123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test:test1234@db/mysql'

db = SQLAlchemy(app)


class pm(db.Model):
    Product_ID = db.Column('Product_ID', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    discription = db.Column(db.String(50))
    supplier = db.Column(db.String(200))
    price = db.Column(db.String(10))

    def __init__(self, name, discription, supplier, price):
        self.name = name
        self.discription = discription
        self.supplier = supplier
        self.price = price


@app.route('/show_all')
def show_all():
    return render_template('show_all.html', pmes=pm.query.all())


@app.route('/')
def show():
    db.create_all()
    print("Welcome")
    return "Welcome"


@app.route('/show_new')
def show_new():
    return render_template('newpm.html')


@app.route('/new_supplier', methods=['POST', 'GET'])
def new_supplier():
    if request.method == 'POST':
        pm = pm(request.form['nm'], request.form['discription'], request.form['add'], request.form['price'])
        db.session.add(pm)
        db.session.commit()
    return render_template('show_all.html', pmes=pm.query.all())


@app.route('/update_supplier', methods=['POST', 'GET'])
def update_supplier():
    if request.method == 'POST':
        print
        "InsProduct_IDe POST"
        try:
            Product_Product_ID = request.form['Product_ID']
            pm = pm.query.filter_by(Product_ID=Product_ID).first()
            pm.name = request.form['nm']
            pm.supplier = request.form['add']
            pm.discription = request.form['discription']
            pm.price = request.form['price']
            db.session.commit()
        except:
            msg = "error during update operation"
            print
            msg
    return render_template('show_all.html', pmes=pm.query.all())


@app.route('/show_update', methods=['POST', 'GET'])
def show_update():
    Product_ID = request.args.get('Product_ID')
    pm = pm.query.filter_by(Product_ID=Product_ID).first()
    return render_template('update_supplier.html', pm=pm)


@app.route('/delete_supplier')
def delete_supplier():
    Product_ID = request.args.get('Product_ID')
    pm = pm.query.filter_by(Product_ID=Product_ID).first()
    db.session.delete(pm)
    db.session.commit()
    return render_template('show_all.html', pmes=pm.query.all())


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
