from app import app


@app.route('/up', methods=['GET'])
def get_up():
    # do something
    pass

@app.route('/up', methods=['POST'])
def add_up():
    # do something
    pass

@app.route('/up', methods=['DELETE'])
def delete_up():
    # do something
    pass

@app.route('/up', methods=['PATCH'])
def update_up():
    # do something
    pass
