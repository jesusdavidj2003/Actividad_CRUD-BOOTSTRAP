from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ──────────────────────────────────────────
#  BASE DE DATOS FALSA  (lista en memoria)
#  Se reinicia cada vez que reinicias Flask
# ──────────────────────────────────────────
productos = [
    {"id": 1, "nombre": "Cuaderno",   "cantidad": 50, "precio": 1.20, "Marca": "Norma"},
    {"id": 2, "nombre": "Lapiz",     "cantidad": 30, "precio": 0.80, "Marca": "Faber-Castell"},
    {"id": 3, "nombre": "Esfero",   "cantidad": 20, "precio": 0.90, "Marca": "Bic"},
    {"id": 4, "nombre": "Borrador",   "cantidad": 20, "precio": 0.90, "Marca": "pelikan"},
    {"id": 5, "nombre": "Sacapuntas",   "cantidad": 20, "precio": 0.90, "Marca": "Maped"},
    {"id": 6, "nombre": "Colores",   "cantidad": 20, "precio": 0.90, "Marca": "Crayola"},
    {"id": 7, "nombre": "Regla",   "cantidad": 20, "precio": 0.90, "Marca": "Staedler"},
    {"id": 8, "nombre": "Pegante",   "cantidad": 20, "precio": 0.90, "Marca": "Colbón"},
]
siguiente_id = 4


# ── READ ──────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", productos=productos)


# ── CREATE ────────────────────────────────
@app.route("/agregar", methods=["POST"])
def agregar():
    global siguiente_id
    productos.append({
        "id":       siguiente_id,
        "nombre":   request.form["nombre"],
        "cantidad": int(request.form["cantidad"]),
        "precio":   float(request.form["precio"]),
        "Marca":    request.form["Marca"]  #Nueva Linea de Codigo: Jesus David Jimenez Martinez 08/04/2026
    })
    siguiente_id += 1
    return redirect(url_for("index"))


# ── UPDATE ────────────────────────────────
@app.route("/editar/<int:id>", methods=["POST"])
def editar(id):
    for p in productos:
        if p["id"] == id:
            p["nombre"]   = request.form["nombre"]
            p["cantidad"] = int(request.form["cantidad"])
            p["precio"]   = float(request.form["precio"])
    return redirect(url_for("index"))


# ── DELETE ────────────────────────────────
@app.route("/eliminar/<int:id>")
def eliminar(id):
    productos[:] = [p for p in productos if p["id"] != id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
