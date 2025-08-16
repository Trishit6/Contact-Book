from flask import Flask, render_template
import os

def create_app():
    app= Flask(__name__, instance_relative_config=False)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY','dev'),
        DATABASE=os.path.join(app.instance_path,'attendance.sqlite'),
    )
    app.config.from_pyfile('config.py', silent=True)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

  
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('home.html'), 404
    
    from . import db
    db.init_app(app)

    from . import home
    app.register_blueprint(home.bp,url_prefix="/")
    app.add_url_rule('/',endpoint='index')

    from . import contact
    app.register_blueprint(contact.bp,url_prefix="/contact")
    app.add_url_rule('/contact/',endpoint='index')
    
    from . import about
    app.register_blueprint(about.bp,url_prefix="/about")
    app.add_url_rule('/about/',endpoint='index')
 
    return app
