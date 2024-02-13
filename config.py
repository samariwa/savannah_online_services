config_params = ''
#Localhost PostgreSQL credentials

service = "postgresql+psycopg2"
host = "localhost"
database = "postgres"
username = ""
password = ""
port = "5432"

# Connection
conn_string = f"{service}://{username}:{password}@{host}:{port}/{database}"
config_params += str(conn_string) + ' '


# MAILTRAP
mail_usr = 'e32affdcce6399'
config_params += str(mail_usr)+' '
mail_pwd = 'dcee4e76a5d5f6'
config_params += str(mail_pwd)+' '

# heroku app secret key
public_app_secret =  'Public91ff0af85cff35940ba46adf'
config_params += str(public_app_secret) + ' '
# localhost app secret key
local_app_secret =  '91ff0af85cff35940ba46adfLOCAL'
config_params += str(local_app_secret) + ' '

"""
# heroku google recaptcha
H_RECAPTCHA_PUBLIC_KEY = '6LeeTYsmAAAAAIOX76nWIj2-T6-FjKKRoGwffZnG'
config_params += str(H_RECAPTCHA_PUBLIC_KEY) + ' '
H_RECAPTCHA_PRIVATE_KEY = '6LeeTYsmAAAAAJgt_UeEsp8IJGU7J7nKCjgrW1IE'
config_params += str(H_RECAPTCHA_PRIVATE_KEY) + ' '
"""

# recaptcha For localhost
L_RECAPTCHA_PUBLIC_KEY = '6Ld_DqAaAAAAAIVKl_AmFc4qhHItRTT75yqbmhtR'
config_params += str(L_RECAPTCHA_PUBLIC_KEY) + ' '
L_RECAPTCHA_PRIVATE_KEY = '6Ld_DqAaAAAAAC_Xp5g6yDr5XPjC1oIlMGZwX5cS'
config_params += str(L_RECAPTCHA_PRIVATE_KEY) + ' '

# Organization settings
organization = {
    "mobile": "0711111111",
    "email": "info@savannah.com",
    "location": "This location"
}

config_params += str(organization.get('mobile')) + ' '
config_params += str(organization.get('email')) + ' '
config_params += str(organization.get('location'))


print(config_params)