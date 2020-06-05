from flask import Flask, render_template, request, redirect, url_for
from utils import database


app = Flask(__name__)

# create sqlite3 table if not already existing
database.create_blog_posts_table()


@app.route('/')
def home():
	blog_posts = database.get_all_blog_posts()
	return render_template('home.jinja2', blog_posts=blog_posts)


@app.route('/post/<int:post_id>')
def post(post_id):
	post_id, title, content = database.get_blog_post(post_id)
	if not post_id:
		return render_template('404.jinja2', message=f'A post with id {post_id} was not found.')
	return render_template('post.jinja2', post_id=post_id, title=title, content=content)


@app.route('/post/create', methods=['GET', 'POST'])
def create():
	if request.method == 'POST':
		title = request.form.get('title')
		content = request.form.get('content')
		post_id = database.insert_blog_post(title, content)
		return redirect(url_for('post', post_id=post_id))
	return render_template('create.jinja2')


@app.route('/delete/<int:post_id>')
def delete(post_id):
	database.delete_blog_post(post_id)
	return redirect(url_for('home'))


@app.route('/post/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
	if request.method == 'POST':
		title = request.form.get('title')
		content = request.form.get('content')
		database.update_blog_post(title, content, post_id)
		return redirect(url_for('post', post_id=post_id))
	post_id, title, content = database.get_blog_post(post_id)
	if not post_id:
		return render_template('404.jinja2', message=f'A post with id {post_id} was not found.')
	return render_template('update.jinja2', title=title, content=content, post_id=post_id)


if __name__ == '__main__':
	app.run()
