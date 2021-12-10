import sqlite3
import os

from flask import Flask, render_template, request, url_for, redirect, session, jsonify
from flask_socketio import SocketIO, emit
from werkzeug.security import check_password_hash, generate_password_hash
from termcolor import colored
from markdown import markdown
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

from helpers import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"
socketio = SocketIO(app)

users = []

db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:TheMonaLisa@localhost:5432/discord"

# if not os.getenv('DATABASE_URL'):
#     conn = sqlite3.connect("db.sqlite3", check_same_thread=False)
#     c = conn.cursor()
# else:
#     import sentry_sdk
#     from sentry_sdk.integrations.flask import FlaskIntegration

#     sentry_sdk.init(
#         dsn=os.getenv("sentry_dsn"),
#         integrations=[FlaskIntegration()]
#     )
#     engine = create_engine(os.getenv("DATABASE_URL"))
#     db = scoped_session(sessionmaker(bind=engine))
#     conn = db()
#     c = conn


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET"])
@login_required
def search():
    # if request.args.get("search"):
    results = db.session.execute("SELECT U.Guild_ID, G.Guild_name FROM USER_HAS_ROLE_IN_GUILD AS U, GUILD AS G WHERE U.User_ID = 'U613704' AND U.Guild_ID = G.Guild_ID;").fetchall()
    print(results)
    return render_template("searched.html", results=results)


@app.route("/room/<string:room_id>", methods=["GET", "POST"])
@login_required
def room(room_id):
    
    user_results = db.session.execute("SELECT User_ID, Role_Name FROM USER_HAS_ROLE_IN_GUILD WHERE Guild_ID = :g_id;", {"g_id": room_id}).fetchall()
    channel_results = db.session.execute("SELECT DISTINCT Channel_ID,Channel_name FROM ROLE_GIVEN_ACCESS_TO_CHANNEL natural join CHANNEL WHERE Guild_ID = :g_id;", {"g_id": room_id}).fetchall()
    

    
    return render_template("users_guild.html", user_results=user_results, channel_results = channel_results)

@app.route("/channel/<string:ch_id>", methods=["GET", "POST"])
@login_required
def messages(ch_id):
    
    results = db.session.execute("SELECT Message_ID, User_ID, \"text\" FROM MESSAGE_SENT_IN_CHANNEL natural join message WHERE Channel_id = :ch_id;", {"ch_id": ch_id}).fetchall()
    print(results)
    

    
    return render_template("message.html", results=results)

@app.route("/channel/thread/<string:ch_id>", methods=["GET", "POST"])
@login_required
def thread(ch_id):
    
    results = db.session.execute("SELECT Thread_ID, Thread_Name FROM THREAD WHERE Channel_id = :ch_id;", {"ch_id": ch_id}).fetchall()
    print(results)
    

    
    return render_template("thread.html", results=results)

@app.route("/channel/pinned_messages/<string:ch_id>", methods=["GET", "POST"])
@login_required
def pinned_messages(ch_id):
    
    results = db.session.execute("SELECT M.Message_ID, ME.text FROM MESSAGE_SENT_IN_CHANNEL AS M, MESSAGE AS ME WHERE ME.Message_ID = M.Message_ID AND Me.Pinned = 1 AND M.Channel_ID = :ch_id;", {"ch_id": ch_id}).fetchall()
    print(results)
    

    
    return render_template("pinned_messages.html", results=results)


@app.route("/users/<string:u_id>", methods=["GET", "POST"])
@login_required
def user_guild_details(u_id):
    
    results = db.session.execute("SELECT U.Guild_ID, G.Guild_Icon, G.GUild_Name FROM USER_HAS_ROLE_IN_GUILD AS U, GUILD AS G WHERE U.User_ID = :u_id AND U.Guild_ID = G.Guild_ID;", {"u_id": u_id}).fetchall()
    print(results)
    

    
    return render_template("user_guild_details.html", results=results)

@app.route("/users", methods=["GET", "POST"])
@login_required
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
@login_required
def message_limited_time(u_id):
    
    results = db.session.execute("select m.message_id, m.text from message_sent_in_channel as mc, message as m where m.message_id = mc.message_id and mc.user_id = :u_id;", {"u_id": u_id}).fetchall()
    print(results)
    

    
    return render_template("message_limited_time.html", results=results)

@app.route("/users/permission", methods=["GET", "POST"])
@login_required
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


# @socketio.on("broadcast message")
# def message_display(data):
#     ts = timestamp()
#     if session.get("user_id"):
#         user = c.execute("SELECT username FROM users WHERE user_id=:id", {"id": session["user_id"]}).fetchall()[0][0]
#     else:
#         user = "unknown"

#     if data["message"] != "" or True in [not s or s.isspace() for s in data["message"]]:
#         messages = data["message"].split("\n")
#         markdowns = []
#         for m in messages:
#             markdowns.append(markdown(m))
#         markdowns = "<br>".join(markdowns)
#         # print(markdowns)
#         c.execute("INSERT INTO messages (message, author, room, timestamp) VALUES (:m, :a, :r, :t)", {"m": markdowns, "a": user, "r": data["room_id"], "t": ts})
#         conn.commit()
#         emit("show message", {"message": markdowns, "timestamp": ts, "name": user, "room_id": data["room_id"]}, broadcast=True)


# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         # check if the form is valid

#             if not request.form.get("email") or not request.form.get("password") or not request.form.get("confirmation") or not request.form.get("username"):
#                 return "please fill out all fields"

#             if request.form.get("password") != request.form.get("confirmation"):
#                 return "password confirmation doesn't match password"

#             # check if email exist in the database
#             exist = c.execute("SELECT * FROM users WHERE email=:email OR username=:username", {"email": request.form.get("email"), "username": request.form.get("username")}).fetchall()

#             if len(exist) != 0:
#                 return "user already registered"

#             # hash the password
#             pwhash = generate_password_hash(request.form.get("password"), method="pbkdf2:sha256", salt_length=8)

#             # insert the row
#             c.execute("INSERT INTO users (email, password, username) VALUES (:email, :password, :username)", {"email": request.form.get("email"), "password": pwhash, "username": request.form.get("username")})
#             conn.commit()

#             # return success
#             return "registered successfully!"
#     else:
#         return render_template("register.html")


# @app.route("/login", methods=["GET", "POST"])
# def login():

#     if request.method == "POST":
#         # check the form is valid
#         if not request.form.get("username") or not request.form.get("password"):
#             return "please fill out all required fields"

#         # check if email exist in the database
#         user = c.execute("SELECT * FROM users WHERE email=:email OR username=:username", {"email": request.form.get("username"), "username": request.form.get("username")}).fetchall()

#         if len(user) != 1:
#             return render_template("login.html", message1="Invalid username/email")

#         # check the password is same to password hash
#         pwhash = user[0][3]
#         if check_password_hash(pwhash, request.form.get("password")) == False:
#             return render_template("login.html", message2="Password doesn't match")

#         # login the user using session
#         session["user_id"] = user[0][0]

#         # return success
#         return redirect("/")

#     else:
#         return render_template("login.html")


# @app.route("/logout")
# @login_required
# def logout():
#     session.clear()
#     return redirect(url_for("login"))


# @app.route("/create-room", methods=["GET", "POST"])
# @login_required
# def create_room():
#     if request.method == "POST":
#         while True:
#             room_id = random_str()
#             rooms = c.execute("SELECT * FROM rooms WHERE room_id=:r_id", {"r_id": room_id}).fetchall()
#             if len(rooms) == 0:
#                 c.execute("INSERT INTO rooms (room_id, name, description, status) VALUES (:r_id, :name, :desc, :status)", {"r_id": room_id, "name": request.form.get("name"), "desc": request.form.get("description"), "status": request.form.get('status')})
#                 conn.commit()
#                 break

#         c.execute("INSERT INTO user_room (user_id, room_id, role) VALUES (:u_id, :r_id, 'owner')", {"r_id": room_id, "u_id": session.get("user_id")})
#         conn.commit()
#         username = c.execute("SELECT username FROM users WHERE user_id=:id", {"id": session.get("user_id")}).fetchall()[0][0]
#         c.execute("INSERT INTO messages (message, author, room, timestamp) VALUES (:m, :a, :r, :t)", {"m": f"Welcome {username}!", "a": "Bot", "r": room_id, "t": timestamp()})
#         conn.commit()
#         socketio.emit("new people joined", {"message": f"Welcome {username}!", "room": room_id}, broadcast=True)
#         return redirect(f"/room/{room_id}")
#     else:
#         return render_template("create-room.html")


# @socketio.on("disconnect")
# def exist():
#     print(session.get("user_id"), "disconnected!")
#     username = c.execute("SELECT username FROM users WHERE user_id=:id", {"id": session["user_id"]}).fetchall()[0][0]
#     users.remove(username)
#     if not username in users:
#         emit("update status", {"user": username, "status": "offline"}, broadcast=True)


# @socketio.on("connect")
# def connect():
#     print(str(session.get("user_id")) + " connected!")
#     if session.get("user_id") == None:
#         print("hi")
#         return False
#     username = c.execute("SELECT username FROM users WHERE user_id=:id", {"id": session["user_id"]}).fetchall()[0][0]
#     users.append(username)
#     room = []
#     rooms = c.execute("SELECT room_id FROM user_room WHERE user_id=:u_id", {"u_id": session.get("user_id")}).fetchall()
#     for r in rooms:
#         room.append(r[0])
#     emit("update status", {"user": username, "status": "online", "room_id": room}, broadcast=True)


# @app.route("/api")
# def api():
#     if request.args.get("api") == "users":
#         room_id = request.args.get("room_id")
#         user = []
#         for i in users:
#             u_id = c.execute("SELECT user_id FROM users WHERE username=:u", {"u": i}).fetchall()[0][0]
#             print(u_id)
#             if len(c.execute("SELECT room_id FROM user_room WHERE user_id=:u_id AND room_id=:r_id", {"u_id": u_id, "r_id": room_id}).fetchall()) != 0:
#                 user.append(i)
#         return jsonify(users=list(set(user)))

#     elif request.args.get("api") == "messages":
#         room_id = request.args.get("room_id")
#         messages = []
#         dbms = c.execute("SELECT * FROM messages WHERE room=:r_id", {"r_id": room_id}).fetchall()
#         for d in dbms:
#             messages.append({"author": d[1], "message": d[2], "timestamp": d[4]})
#         return jsonify(messages=messages)


# @app.route("/dm", methods=["GET"])
# @login_required
# def dm():
#     messages = c.execute("SELECT * FROM messages WHERE room=:room", {"room": str(session.get('user_id'))}).fetchall()
#     username = c.execute("SELECT username FROM users WHERE user_id=:u_id", {"u_id": session["user_id"]}).fetchall()[0][0]
#     return render_template("dm.html", messages=messages, username=username)


# @socketio.on("dm")
# def dm_socket(data):
#     ts = timestamp()
#     user_id = c.execute("SELECT * FROM users WHERE username=:name", {"name": data["username"]}).fetchall()[0][0]
#     c.execute("INSERT INTO messages (author, message, room, timestamp) VALUES (:a, :m, :r, :t)", {"a": data["author"], "m": data["message"], "r": user_id, "t": ts})
#     conn.commit()
#     emit("broadcast dm", {"author": data["author"], "receiver": data["username"], "t": ts, "message": data["message"]})


# @app.route("/@me")
# def me():
#     rooms = c.execute("SELECT * FROM user_room WHERE user_id=:u_id", {"u_id": session["user_id"]}).fetchall()
#     rs = []
#     for r in rooms:
#         name = c.execute("SELECT name FROM rooms WHERE room_id=:r_id", {"r_id": r[1]}).fetchall()[0][0]
#         rs.append((name, r[1], r[2]))
#     return render_template("me.html", rooms=rs)
#     # return str(rooms)


# @app.route("/delete/<string:r_id>")
# @login_required
# def delete_room(r_id):
#     status = c.execute("SELECT * FROM user_room WHERE user_id=:u_id AND room_id=:r_id").fetchall()
#     if len(status) == 0 or status[0][2] != "owner":
#         return "you are not an owner, can't delete this room"
#     c.execute("DELETE FROM messages WHERE room=:r_id", {"r_id": r_id})
#     c.execute("DELETE FROM rooms WHERE room_id=:r_id", {"r_id": r_id})
#     c.execute("DELETE FROM user_room WHERE room_id=:r_id", {"r_id": r_id})
#     conn.commit()
#     return redirect("/@me")


# class Guild(db.Model):

#     count = 1
#     __tablename__ = 'guild'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True, index=True)
#     # guild_count = Guild.count
#     # Guild.count += 1

if __name__ == "__main__":
    socketio.run(app) # , host="0.0.0.0", port=2000, debug=True
    # app.app_context().push()
    # db.create_all()
    # guild_entry = Guild(name = "Arushi_guild")
    # db.session.add(guild_entry)
    # db.session.commit()
    # statement = select(Guild.name)
    # result = db.session.execute(statement).all()
    # print(result)
