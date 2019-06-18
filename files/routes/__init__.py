from flask import current_app as app
from pathlib import Path
from importlib import import_module

p = Path('./files/routes')
# Loops through all the files in above folder and imports them
with app.app_context():
    [import_module(route) for route in ['.'.join(list(x.parts[:-1]) + list(x.parts[-1].split('.py')))[:-1] for x in [x for x in list(p.glob('**/*.py')) if x.parts[-1] != '__init__.py']]]
        