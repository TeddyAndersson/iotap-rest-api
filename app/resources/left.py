from app import app


@app.route('/left', methods=['GET'])
def get_left():
    # do something
    pass

@app.route('/left', methods=['POST'])
def add_left():
    # do something
    pass

@app.route('/left', methods=['DELETE'])
def delete_left():
    # do something
    pass

@app.route('/left', methods=['PATCH'])
def update_left():
    # do something
    pass
