from utils.database_connection import DatabaseConnection
from typing import List, Tuple
import sqlite3

"""
database management for web-blog
"""

blog_titles = []

def create_blog_posts_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS blog_posts(id integer primary key, title text, content text)')


def get_all_blog_posts():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM blog_posts')
        all_blog_posts = cursor.fetchall()
    return all_blog_posts


def get_blog_post(post_id):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT title, content FROM blog_posts WHERE id=?", (post_id,))
        blog_post = cursor.fetchone()
        title = blog_post[0]
        content = blog_post[1]
    return post_id, title, content


def insert_blog_post(title: str, content: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO blog_posts (title, content) VALUES (?, ?)', (title, content))
        post_id = cursor.lastrowid
    return post_id


def delete_blog_post(post_id: int) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM blog_posts WHERE id=?', (post_id,))
    return


def update_blog_post(title: str, content: str, post_id: int):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE blog_posts SET title = ?, content = ? WHERE id = ?', (title, content, post_id))
    return
