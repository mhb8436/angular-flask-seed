#!/usr/bin/env python
import os
from server import create_app
from config import Config

app = create_app(Config)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	debug = os.environ.get('FLASK_DEBUG', '0') == '1'
	app.run(debug=debug, host='0.0.0.0', port=port)
