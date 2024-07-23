from flask import Flask

# Create Flask Environment
app = Flask(__name__)

# Avoid Circular Import
from source import routes
