from flask import Flask, render_template, redirect, request
import pickle, numpy as np, pandas as pd

top_50_books=pickle.load(open('top_50_books.pkl', 'rb'))
pitable=pickle.load(open('pitable.pkl', 'rb'))

similarity_scr=pickle.load(open("similarity_scr.pkl", 'rb'))

final_books = pickle.load(open("final_books.pkl", 'rb'))




app=Flask(__name__)
app.use_static_for_external_files = True

@app.route("/")

def index():
    
    

    return render_template('index.html',
    book_name=list(top_50_books["Book-Title"].values),
    author=list(top_50_books["Book-Author"].values),
    avg_rating=list(top_50_books["avg_rating"].values ),
    publisher=list(top_50_books["Publisher"].values),
    pic=list(top_50_books["Image-URL-S"].values),
    cnt_rating=list(top_50_books["Num_ratings"].values))

@app.route("/recomend_ui")
def recomend_ui():
   return render_template('final.html')


@app.route("/recomend_books", methods=['POST'])
def recomend_book():
   user_input= str(request.form.get('user_input'))
  
   in_dex= np.where(pitable.index==user_input)[0][0]
   sim_index= sorted(list(enumerate(similarity_scr[in_dex])), key=lambda x: x[1], reverse=True)[1:6]
   recomnded_book=[]
   for i in sim_index:
        items=[]
        items.append(pitable.index[i[0]])
        items.append(final_books[final_books["Book-Title"]==\
                          pitable.index[i[0]]].drop_duplicates("Book-Title")["Book-Author"].values[0])
        items.append(final_books[final_books["Book-Title"]==\
                          pitable.index[i[0]]].drop_duplicates("Book-Title")["Publisher"].values[0])
        items.append(final_books[final_books["Book-Title"]==\
                          pitable.index[i[0]]].drop_duplicates("Book-Title")["Image-URL-S"].values[0])
        items.append(final_books[final_books["Book-Title"]==\
                          pitable.index[i[0]]].drop_duplicates("Book-Title")["Book-Rating"].values[0])
        return items
  
   
   
   
  # return render_template('final.html' )

if __name__=="__main__":
    app.run(debug=True)
