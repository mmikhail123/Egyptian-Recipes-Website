from flask import Flask, render_template, redirect, url_for, request
import os

app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'IMG')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER


@app.route("/")
def home():
    koshary = os.path.join(app.config['UPLOAD_FOLDER'], 'Koshary.jpg')
    molokhia = os.path.join(app.config['UPLOAD_FOLDER'], 'molokhia.jpg')
    macbech = os.path.join(app.config['UPLOAD_FOLDER'], 'macbech.jpg')
    falafel = os.path.join(app.config['UPLOAD_FOLDER'], 'falafel.jpg')
    goulash = os.path.join(app.config['UPLOAD_FOLDER'], 'goulash.jpg')
    hawawashi = os.path.join(app.config['UPLOAD_FOLDER'], 'hawawashi.jpg')
    kofta = os.path.join(app.config['UPLOAD_FOLDER'], 'kofta.jpg')
    mahshi = os.path.join(app.config['UPLOAD_FOLDER'], 'mahshi.jpg')
    mombar = os.path.join(app.config['UPLOAD_FOLDER'], 'mombar.jpg')
    return render_template('home.html', user_image = koshary, molo_image = molokhia, macbech_image = macbech, falafel_image = falafel, 
    goulash_image = goulash, hawawashi_image = hawawashi, kofta_image = kofta, mahshi_image = mahshi, mombar_image = mombar)


@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/koshary/')
def koshary():
    return render_template('koshary.html')

@app.route('/molokhia/')
def molokhia():
    return render_template('molokhia.html')

@app.route('/macbech/')
def macbech():
    return render_template('macbech.html')

@app.route('/falafel/')
def falafel():
    return render_template('falafel.html')

@app.route('/goulash/')
def goulash():
    return render_template('goulash.html')

@app.route('/hawawashi/')
def hawawashi():
    return render_template('hawawashi.html')

@app.route('/kofta/')
def kofta():
    return render_template('kofta.html')

@app.route('/mahshi/')
def mahshi():
    return render_template('mahshi.html')

@app.route('/mombar/')
def mombar():
    return render_template('mombar.html')

if __name__ == '__main__':
    app.run(debug=True)