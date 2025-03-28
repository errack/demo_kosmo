import configparser

# Crear archivo de configuración si no existe
def create_config():
    config = configparser.ConfigParser()
    config['SERVER'] = {
        'HOST': '127.0.0.1',
        'PORT': '5000'
    }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


config = configparser.ConfigParser()
config.read('config.ini')


if not config.has_section('SERVER'):
    create_config()
    config.read('config.ini')


def get_config_value(section, key, default):
    return config.get(section, key, fallback=default)
