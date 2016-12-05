#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import app
import os

#run app on correct port
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
