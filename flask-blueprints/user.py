# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:39:28 2016

@author: saqibullah
"""
from flask import Blueprint

user = Blueprint('user', __name__)
    
@user.route('/greeting')
def greeting():
    return 'Hello, lowly normal user!'