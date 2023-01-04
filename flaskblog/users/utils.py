import os
import secrets
from PIL import Image
from flask import url_for, current_app
from ioe_email_stuff import send_email
from flaskblog.config import Config

def save_picture(form_picture) -> str:
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (150, 150)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)
    return picture_fn

def send_reset_email(user):

    config = Config()
    username = config.MAIL_USERNAME
    password = config.MAIL_PASSWORD

    token = user.get_reset_token()
    body = f"""
    <html>
        <head></head>
        <body>
            <p>To reset your password, click <a href="{url_for('users.reset_token', token=token, _external=True)}">here</a> or visit the following link:</p>
            <small>{url_for('users.reset_token', token=token, _external=True)}</small>
            <p>If you did not make this request then simply ignore this email.</p>
        </body>
    </html>
"""
    send_email("Password Reset Request", body=body, username=username, passwd=password, to=user.email, cc="george@georgestools.com;")

