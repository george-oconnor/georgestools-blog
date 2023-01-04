import keyring, json

linux = False

if linux == True:
    with open('/etc/config.json') as config_file:
        config = json.load(config_file)

class Config:
    if linux == True:
        SECRET_KEY = config.get('SECRET_KEY')
        SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
        MAIL_USERNAME = config.get('EMAIL_USER')
        MAIL_PASSWORD = config.get('EMAIL_PASS')
    else:
        SECRET_KEY = keyring.get_password("georgestools-blog", "app-secret-key")
        SQLALCHEMY_DATABASE_URI = keyring.get_password("georgestools-blog", "database-uri")
        MAIL_USERNAME = keyring.get_password("georgestools-blog", "taa-username")
        MAIL_PASSWORD = keyring.get_password("georgestools-blog", "taa-password")

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True