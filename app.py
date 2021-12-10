import os
#import sqlite3
from helpers import *
from termcolor import colored
from markdown import markdown

from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
from sqlalchemy import create_engine, select
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request, url_for, redirect, session, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"
socketio = SocketIO(app)

users = []
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:TheMonaLisa@localhost:5432/discord"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/discord"
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    results = db.session.execute("SELECT U.Guild_ID, G.Guild_name FROM USER_HAS_ROLE_IN_GUILD AS U, GUILD AS G WHERE U.User_ID = 'U613704' AND U.Guild_ID = G.Guild_ID;").fetchall()
    print(results)
    return render_template("searched.html", results=results)


@app.route("/room/<string:room_id>", methods=["GET", "POST"])
def room(room_id):
    user_results = db.session.execute("SELECT User_ID, Role_Name FROM USER_HAS_ROLE_IN_GUILD WHERE Guild_ID = :g_id;", {"g_id": room_id}).fetchall()
    channel_results = db.session.execute("SELECT DISTINCT Channel_ID,Channel_name FROM ROLE_GIVEN_ACCESS_TO_CHANNEL natural join CHANNEL WHERE Guild_ID = :g_id;", {"g_id": room_id}).fetchall()
    return render_template("users_guild.html", user_results=user_results, channel_results = channel_results)

@app.route("/channel/<string:ch_id>", methods=["GET", "POST"])
def messages(ch_id):
    results = db.session.execute("SELECT Message_ID, User_ID, \"text\" FROM MESSAGE_SENT_IN_CHANNEL natural join message WHERE Channel_id = :ch_id;", {"ch_id": ch_id}).fetchall()
    print(results)
    return render_template("message.html", results=results)

@app.route("/channel/thread/<string:ch_id>", methods=["GET", "POST"])
def thread(ch_id):
    results = db.session.execute("SELECT Thread_ID, Thread_Name FROM THREAD WHERE Channel_id = :ch_id;", {"ch_id": ch_id}).fetchall()
    print(results)
    return render_template("thread.html", results=results)

@app.route("/channel/pinned_messages/<string:ch_id>", methods=["GET", "POST"])
def pinned_messages(ch_id):    
    results = db.session.execute("SELECT M.Message_ID, ME.text FROM MESSAGE_SENT_IN_CHANNEL AS M, MESSAGE AS ME WHERE ME.Message_ID = M.Message_ID AND Me.Pinned = 1 AND M.Channel_ID = :ch_id;", {"ch_id": ch_id}).fetchall()
    print(results)
    return render_template("pinned_messages.html", results=results)

@app.route("/users/<string:u_id>", methods=["GET", "POST"])
def user_guild_details(u_id):    
    results = db.session.execute("SELECT U.Guild_ID, G.Guild_Icon, G.GUild_Name FROM USER_HAS_ROLE_IN_GUILD AS U, GUILD AS G WHERE U.User_ID = :u_id AND U.Guild_ID = G.Guild_ID;", {"u_id": u_id}).fetchall()
    print(results)
    return render_template("user_guild_details.html", results=results)

@app.route("/users", methods=["GET", "POST"])
def channel_guild_user():
    url_request = request.args.to_dict(flat = False)
    print(url_request)
    u_id  = (url_request['u_id'][0]).replace('%','')
    g_id  = (url_request['g_id'][0]).replace('%','')
    print("U_ID", u_id)
    print("G_ID", g_id)    
    results = db.session.execute("SELECT Channel_Name FROM CHANNEL WHERE Channel_ID IN (SELECT C.Channel_ID FROM USER_HAS_ROLE_IN_GUILD AS U, ROLE_GIVEN_ACCESS_TO_CHANNEL AS C WHERE U.User_ID = :u_id AND U.Role_name = C.Role_name AND U.Guild_ID = C.Guild_ID AND U.Guild_ID = :g_id);", {"u_id": u_id,"g_id": g_id}).fetchall()
    print(results)
    return render_template("channel_guild_user.html", results=results)

@app.route("/users/messages/<string:u_id>", methods=["GET", "POST"])
def message_limited_time(u_id):
    results = db.session.execute("select m.message_id, m.text from message_sent_in_channel as mc, message as m where m.message_id = mc.message_id and mc.user_id = :u_id;", {"u_id": u_id}).fetchall()
    print(results)
    return render_template("message_limited_time.html", results=results)

@app.route("/users/permission", methods=["GET", "POST"])
def channel_create_permission():
    url_request = request.args.to_dict(flat = False)
    print(url_request)
    u_id  = (url_request['u_id'][0]).replace('%','')
    g_id  = (url_request['g_id'][0]).replace('%','')
    print("U_ID", u_id)
    print("G_ID", g_id)
    results = db.session.execute("SELECT U.User_ID FROM USER_HAS_ROLE_IN_GUILD AS U WHERE U.User_ID = :u_id AND U.Guild_id = :g_id AND 5 >= (SELECT COUNT(*) FROM CHANNEL AS C WHERE C.Guild_ID = U.Guild_ID) AND EXISTS (SELECT * FROM ROLE AS R WHERE R.Role_Name = U.Role_Name AND R.Guild_ID = U.Guild_ID AND Manage_Channels = 1);", {"u_id": u_id,"g_id": g_id}).fetchall()
    print(results)
    return render_template("channel_create_permission.html", results=results)

if __name__ == "__main__":
    socketio.run(app)
