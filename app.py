from flask import Flask
from subprocess import run, PIPE

from flask import logging, Flask, render_template, request
import os
import numpy as np
import librosa
from joblib import load
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!2"
