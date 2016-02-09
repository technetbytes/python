# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:37:28 2016

@author: saqibullah
"""
from flask import Blueprint

admin = Blueprint('admin', __name__)
  
@admin.route('/greeting')
def greeting():
    return 'Hello, administrative user!'