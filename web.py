import os
from pathlib import Path
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.before_first_request
def init():
    data_path = Path(app.config['DATA_PATH'])
    data_path.mkdir(parents=True, exist_ok=True)
