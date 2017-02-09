from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    blog_title = 'Awsome Blog'  # fake blog title
    posts = [  # fake array of posts
        { 
            'title': 'First blog', 
            'content': 'This is my first blog!' 
        },
        { 
            'title': 'Second blog', 
            'content': 'Second blog for flask blog.' 
        }
    ]
    return render_template("index.html",
                           blog_title=blog_title,
                           posts=posts)
