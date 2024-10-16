from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

# List of supported locales
SUPPORTED_LOCALES = ['en', 'fr']

# Configuration for default locale
app.config['BABEL_DEFAULT_LOCALE'] = 'en'

@babel.localeselector
def get_locale():
    # Check if the locale parameter is in the URL
    locale = request.args.get('locale')
    if locale in SUPPORTED_LOCALES:
        return locale
    # Return default locale if no valid locale is provided
    return request.accept_languages.best_match(SUPPORTED_LOCALES)

@app.route('/')
def index():
    return render_template('4-index.html')

if __name__ == "__main__":
    app.run(debug=True)
