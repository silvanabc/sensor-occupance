from flask import Flask, request, abort
from SensorException import SensorException


import sensor


app = Flask(__name__)

@app.errorhandler(SensorException)
def handle_sensor_exception(error):
    print(error)
    return {'message': str(error)}, 400

@app.errorhandler(Exception)
def handle_exception(error):
    print(error)
    return {'message': "Internal Error"}, 500


@app.route('/api/webhook', methods=['POST'])
def webhook():
    form = request.form

    ##TODO: messages
    if not form:
        return {"message": "Bad request."}, 400
    
    if 'date' not in form:
        return {"message": "Please inform a date."}, 400

    if 'in' not in form:
        return {"message": "Please inform the quantity of people who go into the room."}, 400
    
    if 'out' not in form:
        return {"message": "Please inform the quantity of people who go out the room."}, 400
    

    if 'sensor' not in form:
        return {"message": "Please inform the sensor."}, 400
    
    if not form['in'].isdigit():
        return {"message": "Invalid value 'in'."}, 400

    if not form['out'].isdigit():
        return {"message": "Invalid value 'out'."}, 400
    
         
    sensor.register_movement(form['sensor'],form['date'], int(form['in']), int(form['out']))
    
    return {"result":"Event successfully registered"}


@app.route('/api/occupance/<sensor_id>', methods=['GET'])
def occupance(sensor_id):
    return {"inside": sensor.get_count(sensor_id)}