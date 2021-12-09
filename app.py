from flask import Flask, render_template, redirect, url_for, request
from guilds import Guild

app = Flask(__name__)

@app.route('/')
def welcome():
	names_of_instructors = ["Elie", "Tim", "Matt"]
	random_name = "Tom"
	return render_template('index.html', names=names_of_instructors, name=random_name)

@app.route('/second')
def second():
	return "WELCOME TO THE SECOND PAGE!"

@app.route('/title')
def title():
	return render_template('title.html')

# we need to do something when the form is submitted
@app.route('/data')
def print_name():
	first = request.args.get('first')
	last = request.args.get('last')
	return f"You put {first} {last}"


duplo = Guild(name='duplo')
lego = Guild(name='lego')
knex = Guild(name='knex')

guilds = [duplo,lego,knex]

@app.route('/guilds', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		# gather the value of an input with a name attribute of "name"
		guilds.append(Guild(request.form['name']))
		# respond with a redirect to the route which has a function called "index" (in this case that is '/Guilds')
		return redirect(url_for('index'))
	# if the method is GET, just return index.html
	return render_template('index.html', guilds=guilds)


@app.route('/guilds/new')
def new():
	return render_template('new_guild.html')


@app.route('/guilds/<int:id>', methods=["GET", "DELETE"])
def show(id):
	# Refactored using a generator so that we do not need to do [0]!
	found_guild = next(guild for guild in  guilds if guild.id == id)
	
	if request.method == b"DELETE":
		guilds.remove(found_guild)
		return redirect(url_for('index'))
	
	# if we are showing information about a guild
	return render_template('show_guild.html', guild=found_guild)

