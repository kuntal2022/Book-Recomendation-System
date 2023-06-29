from flask import Flask, render_template, redirect, request
import pickle

app = Flask(__name__, static_url_path='/static')
app.use_static_for_external_files = True

# Load the necessary data from pickle files
top_50_books = pickle.load(open('top_50_books.pkl', 'rb'))
pitable = pickle.load(open('pitable.pkl', 'rb'))
similarity_scr = pickle.load(open("similarity_scr.pkl", 'rb'))
reco_x = pickle.load(open("reco_x.pkl", 'rb'))

@app.route("/")
def index():
    return render_template('index.html',
                           book_name=list(top_50_books["Book-Title"].values),
                           author=list(top_50_books["Book-Author"].values),
                           avg_rating=list(top_50_books["avg_rating"].values),
                           publisher=list(top_50_books["Publisher"].values),
                           pic=list(top_50_books["Image-URL-S"].values),
                           cnt_rating=list(top_50_books["Num_ratings"].values)
                           )

@app.route("/recommend")
def recommend():
    return render_template('final.html', x=[1, 2, 3, 4, 5])

if __name__ == "__main__":
    app.run(debug=True)
