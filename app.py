import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Setzt das Arbeitsverzeichnis auf den Ordner, in dem app.py liegt
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("Current Working Directory:", os.getcwd())  # Überprüfe das aktuelle Arbeitsverzeichnis

# Lade alle Filme
def load_movies():
    file_path = "movies.txt"
    if not os.path.exists(file_path):
        print(f"Die Datei {file_path} wurde nicht gefunden!")
        return ["Die Datei 'movies.txt' wurde nicht gefunden."]
    
    with open(file_path, "r") as f:
        filme = [line.strip() for line in f.readlines() if line.strip()]
    
    return filme

@app.route("/", methods=["GET"])
def index():
    # Lade alle Filme
    movies = load_movies()
    
    # Suchparameter
    search_query = request.args.get("search")
    if search_query:
        movies = [movie for movie in movies if search_query.lower() in movie.lower()]

    return render_template("startseite.html", movies=movies)

# Starte App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)



