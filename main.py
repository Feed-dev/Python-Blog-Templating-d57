# main.py
from flask import Flask, render_template, abort
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    posts = Post.get_posts()
    return render_template("index.html", posts=posts)


@app.route('/post/<int:blog_id>')
def blog_post(blog_id):
    posts = Post.get_posts()
    post = next((post for post in posts if post['id'] == blog_id), None)
    if post is None:
        abort(404)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)

