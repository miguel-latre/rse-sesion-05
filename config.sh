py -m venv .venv
chmod +x .venv/Scripts/activate
.venv/bin/activate
pip install -U pytest
pytest --version
