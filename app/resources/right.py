from app import app


@app.route('/right', methods=['GET'])
def get_right():
    # do something
    pass

@app.route('/right', methods=['POST'])
def add_right():
    # do something
    pass

@app.route('/right', methods=['DELETE'])
def delete_right():
    # do something
    pass

@app.route('/right', methods=['PATCH'])
def update_right():
    # do something
    pass
