from flask import render_template, redirect, url_for
from app import app, crandom
import config

@app.route('/')
@app.route('/index')
def index():
    champions = crandom.load_champion_data()
    return render_template('index.html',
                           title='Home',
                           champions=champions)

@app.route('/random')
def random():
    choice = crandom.get_random_champion_name()
    name = choice.get("proper_name")
    img = choice.get("internal_name")
    quip = crandom.get_a_quip()
    link = config.OPGG_URL + "/champion/" + img
    return render_template('random.html',
                           name=name,
                           img=img,
                           quip=quip,
                           link=link)

@app.route('/marksman')
def marksman():
    choice = crandom.get_random_marksman()
    name = choice.get("proper_name")
    img = choice.get("internal_name")
    quip = crandom.get_a_quip()
    link = config.OPGG_URL + "/champion/" + img
    return render_template('random.html',
                           name=name,
                           img=img,
                           quip=quip,
                           link=link)

@app.route('/mage')
def mage():
    choice = crandom.get_random_mage()
    name = choice.get("proper_name")
    img = choice.get("internal_name")
    quip = crandom.get_a_quip()
    link = config.OPGG_URL + "/champion/" + img
    return render_template('random.html',
                           name=name,
                           img=img,
                           quip=quip,
                           link=link)

@app.route('/tank')
def tank():
    choice = crandom.get_random_tank()
    name = choice.get("proper_name")
    img = choice.get("internal_name")
    quip = crandom.get_a_quip()
    link = config.OPGG_URL + "/champion/" + img
    return render_template('random.html',
                           name=name,
                           img=img,
                           quip=quip,
                           link=link)

@app.route('/support')
def support():
    choice = crandom.get_random_support()
    name = choice.get("proper_name")
    img = choice.get("internal_name")
    quip = crandom.get_a_quip()
    link = config.OPGG_URL + "/champion/" + img
    return render_template('random.html',
                           name=name,
                           img=img,
                           quip=quip,
                           link=link)

@app.route('/fighter')
def fighter():
    choice = crandom.get_random_fighter()
    name = choice.get("proper_name")
    img = choice.get("internal_name")
    quip = crandom.get_a_quip()
    link = config.OPGG_URL + "/champion/" + img
    return render_template('random.html',
                           name=name,
                           img=img,
                           quip=quip,
                           link=link)

@app.route('/assassin')
def assassin():
    choice = crandom.get_random_assassin()
    name = choice.get("proper_name")
    img = choice.get("internal_name")
    quip = crandom.get_a_quip()
    link = config.OPGG_URL + "/champion/" + img
    return render_template('random.html',
                           name=name,
                           img=img,
                           quip=quip,
                           link=link)

@app.route('/reload')
def reload():
    crandom.reload()
    return redirect(url_for('index'))