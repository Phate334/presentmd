import os
from pathlib import Path

from flask import current_app, redirect, render_template, abort
from . import main
from .entity import IndexEntity


@main.route('/', methods=['GET'])
def index():
    return redirect('/present/')


@main.route('/present/')
def present_index():
    data_path = Path(current_app.config['DATA_PATH'])
    entities = [
        IndexEntity(s.relative_to(data_path))
        for s in sorted(data_path.iterdir(), key=lambda x: x.is_file())
    ]
    return render_template('index.html', entities=entities)


@main.route('/present/<path:target>', methods=['GET'])
def present(target):
    data_path = Path(current_app.config['DATA_PATH'])
    target_path = data_path.joinpath(Path(target))
    if target.endswith('.md'):
        return render_template(
            'present.html',
            title=target_path.parts[-1].replace('.md', ''),
            raw_md='/md/' + target)
    elif target_path.is_dir():
        entities = [
            IndexEntity(s.relative_to(data_path))
            for s in sorted(target_path.iterdir(), key=lambda x: x.is_file())
        ]
        return render_template('index.html', entities=entities)
    else:
        abort(404)


@main.route('/md/<path:target>', methods=['GET'])
def raw_md(target):
    data_path = Path(current_app.config['DATA_PATH'])
    target_path = data_path.joinpath(Path(target))
    with open(target_path, 'rb') as f:
        return f.read()