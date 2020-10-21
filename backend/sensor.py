from SensorException import SensorException

sensors_count = {}
sensors_log = {}

def register_movement(sensor_id, date, in_, out):
    total = int(in_) - int(out)

    if sensor_id in sensors_log:
        sensors_log[sensor_id].append({date: date, in_: in_, out: out})

        if sensors_count[sensor_id] + total < 0:
            raise SensorException('Error in registering the movement: quantity of people out not allowed.')
        
        sensors_count[sensor_id] += total
    else:
        if total < 0:
            raise SensorException('Error in registering the movement: quantity of people out not allowed.')
        sensors_log[sensor_id] = [{date: date, in_: in_, out: out}]
        sensors_count[sensor_id] = total

def get_count(sensor_id):
    if sensor_id in sensors_count:
        return sensors_count[sensor_id]
    return 0
