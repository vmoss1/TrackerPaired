from flask import Flask , render_template, redirect
from app.config import Config
from .shipping_form import ShippingForm
from map.map import map

app = Flask(__name__)


app.config.from_object(Config)


@app.route("/")
def index():
    return "<h1>Package Tracker<h1>"



@app.route("/new_package", methods=["GET", "POST"])
def newPackage():
    form = ShippingForm()
    if form.validate_on_submit():
        new_submition = {
            # "id": len() + 1
            "sender_name": form.data["sender_name"],
            "recipient_name": form.data["recipient_name"],
            "origin": form.data["origin"],
            "destination": form.data["destination"],
            "express_shipping": form.data["express_shipping"],
        }
        # map.append(new_submition)
        return redirect('/')

    return render_template("shipping_request.html", form=form)
