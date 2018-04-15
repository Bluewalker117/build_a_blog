from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['DEBUG'] = True  

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build_a_blog:build_a_blog@localhost:8889/build_a_blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

#creating DB in Python
class Blog(db.Model):
    
    id = db.Column(db.Integer, primary_key=True) #will give a unique ID to each databse entry
    title = db.Column(db.String(120))
    body = db.Column(db.String(600))


    def __init__(self, title, body):
        self.title = title
        self.body = body






@app.route("/add", methods=['GET','POST'])
def add_blog():

    if request.method == 'POST':
        new_blog_body = request.form['blog_body']
        new_blog_title = request.form['blog_title']
          
   #     if new_blog_title.strip()=="":
   #         flash("Your blog is not titled. It will need a title and a knighthood to be posted.")
   #         return render_template("add.html", )
   #     if new_blog_body() == "":
   #         error = "Your blog is invisible. You can't read what you can't see.  Please add visible text."
   #         return redirect("/?error=" + error)
   #     else:
        blog_title = request.form['blog_title']
        blog_body = request.form['blog_body']
        new_blog = Blog(blog_title, blog_body)
        db.session.add(new_blog)
        db.session.commit()

    return render_template('add.html')
    

@app.route('/', methods=['POST', 'GET'])
def index():


    blogs = Blog.query.all()
    return render_template('blog_posts.html', blogs=blogs)

app.secret_key = 'key'

if __name__ == '__main__':
    app.run() 