"""
A basic starter app  with the Flask framework and PyMongo
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_HOST'] = 'localhost'
app.config['MONGO_PORT'] = '27017'
app.config['MONGO_DBNAME'] = "TopHits"

# connect to MongoDB with the defaults
# mongo    = PyMongo(app)

mongo = PyMongo(app, config_prefix='MONGO')

value = 0
@app.route('/')
def returnValues():
    if request.method == 'GET':
        songs = mongo.db.songs.find()
        return render_template('gallery.html', songs=songs)


@app.route('/',methods=['GET','POST'])
def getArtistValue():

    artist_name = request.form['search']

    if request.method == 'GET':
        songs = mongo.db.songs.find()
        return render_template('gallery.html', songs=songs)

        # search the artist with name

    if request.method == 'POST':
        songs = mongo.db.songs.find({'artist_name': artist_name})
        return render_template('gallery.html', songs=songs)

    if artist_name == "":
        songs = mongo.db.songs.find({'artist_name': artist_name})
        return render_template('gallery.html', songs=songs)


@app.route('/query/<number>')
def aboutUs(number):
        number = int(number)

        #== == == == == == == == == == == == == == == == == == == == == =
        # what are the 5 songs with lowest tempi across all year?
        #----------------------------------------------------------------
        # db.songs.find().sort({tempo: +1}).limit(5).pretty()

        if number == 1 :
            songs = mongo.db.songs.find().sort([('tempo', 1)]).limit(5)
            return render_template('gallery.html', songs=songs)

        # == == == == == == == == == == == == == == == == == == == == == =
        # what are the 5 songs witgh minimum sound quality?
        # ----------------------------------------------------------------
        #  db.songs.find().sort({Sound_quality:-1}).limit(5).pretty()

        elif number == 2 :
            songs = mongo.db.songs.find().sort([('Sound_quality', -1)]).limit(5)
            return render_template('gallery.html', songs=songs)

        # == == == == == == == == == == == == == == == == == == == == == =
        # what are the top 10 songs with maximum energy across all years?
        # ----------------------------------------------------------------
        #  db.songs.find().sort({energy:-1}).limit(10).pretty()

        elif number == 3 :
            songs = mongo.db.songs.find().sort([('energy', -1)]).limit(10)
            return render_template('gallery.html', songs=songs)

        # == == == == == == == == == == == == == == == == == == == == == =
        # what are the 10 most danceable songs from the 2000's
        # ----------------------------------------------------------------
        #  db.songs.find().sort({danceability:-1},{"years":"2000s"}).limit(10).pretty()

        elif number == 4 :
            songs = mongo.db.songs.find({"years": "2000s"}).sort([('danceability', -1)]).limit(10)
            return render_template('gallery.html', songs=songs)

        # == == == == == == == == == == == == == == == == == == == == == =
        # What are the top 5 most pleasant songs across all years?
        # ----------------------------------------------------------------
        #  db.songs.find().sort({valence:1}).limit(5).pretty()

        elif number == 5 :
            songs = mongo.db.songs.find().sort([('valence', 1)]).limit(5)
            return render_template('gallery.html', songs=songs)


        # if artist_name == "":
        #     songs = mongo.db.songs.find()
        #     return render_template('gallery.html', songs=songs)
        # else:
        #     songs = mongo.db.songs.find({'artist_name': artist_name})
        #     songs1 = mongo.db.songs.find({'song_title': artist_name})
        # return render_template('gallery.html', songs=songs)

@app.route('/year/<yearNumberStr>')
def yearSearch(yearNumberStr):

    yearNumberInt = int(yearNumberStr)

    if yearNumberInt == 1950:
        songs = mongo.db.sngs.find({'years': '1950s'})

    if yearNumberInt == 1960:
        songs = mongo.db.songs.find({'years': '1960s'})

    if yearNumberInt == 1970:
        songs = mongo.db.songs.find({'years': '1970s'})

    if yearNumberInt == 1980:
        songs = mongo.db.songs.find({'years': '1980s'})

    if yearNumberInt == 1990:
        songs = mongo.db.songs.find({'years': '1990s'})

    if yearNumberInt == 2000:
        songs = mongo.db.songs.find({'years': '2000s'})

    return render_template('gallery.html', songs = songs)

if __name__ == '__main__':
    app.run(debug=True) # I will see any error messages occure due to this true
