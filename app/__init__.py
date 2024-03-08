from flask import Flask , render_template, redirect
from flask_migrate import Migrate
from app.config import Config
from .shipping_form import ShippingForm
from map.map import map
from .models import db, Package

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/', methods=["GET"])
def root_endpoint():
    packages = Package.query.all()
    print("Here's your steam pacakge:", packages)
    return render_template('package_status.html', packages=packages)



@app.route("/new_package", methods=["GET", "POST"])
def newPackage():
    form = ShippingForm()
    if form.validate_on_submit():
        data = form.data
        print("This is our daddy:", data)
        new_package = Package(sender=data["sender_name"],
                              recipient=data["recipient_name"],
                              origin=data["origin"],
                              destination=data["destination"],
                              location=data["origin"])
        db.session.add(new_package)
        db.session.commit()
        Package.advance_all_locations()
        return redirect('/')

    return render_template("shipping_request.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():

    if form.validate_on_submit():
        data = form.data
        print("This is our daddy:", data)
        new_package = Package(sender=data["sender_name"],
                              recipient=data["recipient_name"],
                              origin=data["origin"],
                              destination=data["destination"],
                              location=data["origin"])
        db.session.add(new_package)
        db.session.commit()
        Package.advance_all_locations()
        return redirect('/')
    return render_template('login.html', packages=packages)



@app.route("/new_package", methods=["GET", "POST"])
