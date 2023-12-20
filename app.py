from flask import (
        Flask, 
        request, 
        jsonify, 
        send_from_directory)
import logging
import json

app = Flask(__name__,
            template_folder='.',
            static_folder='.',
            static_url_path='')

@app.route('/health')
def health():
    return 'ok'

@app.route('/')
def test():
    return send_from_directory('./', 'index.html')

if __name__ == "__main__":
    app.run(debug=True, 
            use_reloader=False,
            port="7000"
            )
