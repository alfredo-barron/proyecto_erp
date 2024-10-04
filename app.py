from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from config import Config

# Crear una instancia de la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)

# Configurar la base de datos
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
csrf = CSRFProtect(app)

# Importar y registrar blueprints
from controllers.cuentas_controller import cuentas
#from controllers.libro_mayor_controller import libro_mayor_bp
#from controllers.activos_fijos_controller import activos_fijos_bp
# Aquí importarías otros blueprints según tus módulos del ERP

# Registrar blueprints en la aplicación
app.register_blueprint(cuentas)
#app.register_blueprint(libro_mayor_bp)
#app.register_blueprint(activos_fijos_bp)
# Registrar otros blueprints según tus módulos del ERP

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Manejo de error 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
