"""
    csh-pings-backend.py - The main file for the CSH Pings Backend.
    Copyright (C) 2026 R. Mamet <flower@csh.rit.edu>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import flask
from flask import Flask, request, jsonify
from flask_pyoidc import OIDCAuthentication
from flask_pyoidc.provider_configuration import ProviderConfiguration, ClientMetadata
from flask_pyoidc.user_session import UserSession

from markupsafe import escape

from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config.update(
    OIDC_REDIRECT_URI = os.environ['OIDC_REDIRECT_URI'],
    SECRET_KEY = os.environ['SECRET_KEY']
)
config = ProviderConfiguration(issuer=os.getenv('OIDC_ISSUER'),
                               client_metadata=ClientMetadata(
                                    os.getenv('OIDC_CLIENT_ID'),
                                    os.getenv('OIDC_CLIENT_SECRET')))

auth = OIDCAuthentication({'default': config},app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/status")
def status():
    return "You are connected :3"

@app.route('/api')
@auth.oidc_auth('default')
def index():
    user_session = UserSession(flask.session)
    return jsonify(access_token=user_session.access_token,
                   id_token=user_session.id_token,
                   userinfo=user_session.userinfo)

@app.route('/logout')
@auth.oidc_logout
def logout():
    return "You've been successfully logged out!"


@app.route("/api/status")
@auth.oidc_auth('default')
def authed_status():
    user_session = UserSession(flask.session)
    username = escape(user_session.userinfo['preferred_username'])
    return f"Hi @{username}, you are connected and authenticated :)"
