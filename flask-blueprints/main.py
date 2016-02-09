# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:34:29 2016

@author: saqibullah
"""

from flask import Flask
from admin import admin
from user import user

app = Flask(__name__)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(user, url_prefix='/user')

app.run()