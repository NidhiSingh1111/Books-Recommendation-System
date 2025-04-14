from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

popular = pickle.load(open('BOOKS.pkl', 'rb'))
pt = pickle.load(open('final_rating.pkl', 'rb'))
similar = pickle.load(open('Similar.pkl', 'rb'))
books = pd.read_csv('Books.csv')

app = Flask(__name__)

avg_ratings = [round(rating, 2) for rating in popular['Avg_Rating'].values]

@app.route('/')
def index():
    return render_template('index.html',
                           book_name= list(popular['Book-Title'].values),
                           author= list(popular['Book-Author'].values),
                           publish_year= list(popular['Year-Of-Publication'].values),
                           image= list(popular['Image-URL-M'].values),
                           votes= list(popular['Ratings'].values),
                           rating= avg_ratings)

@app.route('/recommend')
def recommend_books():
    return render_template('recommend.html')

@app.route('/recommends', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similar[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    return render_template('recommend.html', data=data)

@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)