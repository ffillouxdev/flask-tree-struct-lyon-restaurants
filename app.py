# app.py
from flask import Flask, render_template, request, redirect
from db import db
from data_structures.tree import Arbre, Noeud_

from db.db_operations import (
    add_restaurant,
    add_type,
    add_arrondissement,
    get_all_restaurants,
    get_all_types,
    get_all_arrondissements,
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask_db.sqlite3"
db.init_app(app)


def create_tree():
    arbre = Arbre()
    restaurants = get_all_restaurants()
    arrondissements = get_all_arrondissements()
    typeRests = get_all_types()

    arrondissement_nodes = {}
    type_nodes = {}

    for restaurant in restaurants:
        if restaurant.idArrondissement not in arrondissement_nodes:
            for arrondissement in arrondissements:
                if arrondissement.idArrondissement == restaurant.idArrondissement:
                    arrondissement_node = arbre.ajouter_arrondissement(
                        arrondissement_nom=arrondissement.arrondissement
                    )
                    arrondissement_nodes[restaurant.idArrondissement] = arrondissement_node
                    break
        else:
            arrondissement_node = arrondissement_nodes[restaurant.idArrondissement]

        type_key = (restaurant.idArrondissement, restaurant.idTypeRest)
        if type_key not in type_nodes:
            for type_rest in typeRests:
                if type_rest.idTypeRest == restaurant.idTypeRest:
                    type_node = arbre.ajouter_type_resto(arrondissement_node, type_rest.typeRest)
                    type_nodes[type_key] = type_node
                    break
        else:
            type_node = type_nodes[type_key]

        restaurant_node = Noeud_({
            "nom": restaurant.nom,
            "coords": restaurant.coords,
            "description": restaurant.description,
        })
        type_node.ajouter_enfant(restaurant_node)

    arbre.afficher_arbre()
    return arbre


@app.route("/")
def root():
    return render_template("index.html", arbre=create_tree(), ville="Lyon")

@app.route("/about")
def about():
    return render_template("about.html", arbre=create_tree(), ville="Lyon")

@app.route("/admin")
def admin():
    restaurants = get_all_restaurants()
    temp_types = {
        type_rest.idTypeRest: type_rest.typeRest for type_rest in get_all_types()
    }
    temp_arrondissements = {
        arrondissement.idArrondissement: arrondissement.arrondissement
        for arrondissement in get_all_arrondissements()
    }

    restaurant_list = []
    for restaurant in restaurants:
        restaurant_data = {
            "nom": restaurant.nom,
            "arrondissement": temp_arrondissements.get(
                restaurant.idArrondissement, "Unknown"
            ),
            "type": temp_types.get(restaurant.idTypeRest, "Unknown"),
            "description": restaurant.description,
            "coords": restaurant.coords,
        }
        restaurant_list.append(restaurant_data)

    return render_template(
        "admin.html",
        arbre=create_tree(),
        ville="Lyon",
        restaurants=restaurant_list,
        types=get_all_types(),
        arrondissements=get_all_arrondissements(),
    )


@app.route("/add_restaurant", methods=["POST"])
def add_restaurant_route():
    nom = request.form["nom"]
    arrondissement_form = request.form["arrondissement"]
    typeRest = request.form["type"]
    description = request.form["description"]
    coords = request.form["coords"]

    add_restaurant(nom, arrondissement_form, typeRest, description, coords)

    return redirect("/admin")


@app.route("/add_type", methods=["POST"])
def add_type_route():
    type_rest = request.form["typeRest"]
    description = request.form["description"]

    add_type(type_rest, description)

    return redirect("/admin")


@app.route("/add_arrondissement", methods=["POST"])
def add_arrondissement_route():
    arrondissement = request.form["arrondissement"]

    add_arrondissement(arrondissement)

    return redirect("/admin")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(host="localhost", port=8080, debug=True)
