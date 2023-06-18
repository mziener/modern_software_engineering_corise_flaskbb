import pytest
from playwright.sync_api import Page, expect
import flask

from flaskbb import create_app
from flaskbb.extensions import db
from flaskbb.configs.testing import TestingConfig
from flaskbb.utils.populate import create_default_groups, create_default_settings
from flaskbb.utils.translations import compile_translations
import os

os.environ['FLASK_ENV'] = 'development'


###################################################################
# CoRise TODO: add a new fixture `translations` that calls the
# `compile_translations` function from flaskbb.utils.translations

# ADD CODE HERE

@pytest.fixture(scope="session")
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        db.create_all()
        create_default_groups()
        create_default_settings()
        compile_translations()
    return app

def test_load_home_page(live_server, page: Page):
    # Hint: Check out `flask.url_for` helper function to get the external url for 
    # an endpoint. Then go to it using playwright's `page.goto(url)`
    # TODO: ADD CODE HERE

    url = flask.url_for('forum.index', _external=True)
    page.goto(url)
    expect(page).to_have_title("FlaskBB - A lightweight forum software in Flask")

    pass

###################################################################