from flask import Flask, render_template
import requests as request
#import redirect as redirect

app = Flask(__name__)
@app.route("/create", methods=("GET", "POST"))
#@login_required
def create():
   """Create a new post for the current user."""
   if request.method == "POST":
       title = request.form["title"]
       body = request.form["body"]
       error = None

       if not title:
           error = "Title is required."

       if error is not None:
           flash(error)
       else:
           db = get_db()
           db.execute(
               "INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)",
               (title, body, g.user["id"]),
           )
           db.commit()
           return redirect(url_for("blog.index"))

   return render_template("blog/create.html")