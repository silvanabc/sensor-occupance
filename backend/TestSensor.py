import unittest
import sensor
from SensorException import SensorException

class TestSensor(unittest.TestCase):
    def tearDown(self):
        #cleaning the variables before each method
        sensor.sensors_count = {}
        sensor.sensors_log = {}

    def test_get_count_no_sensor_id(self):
        assert sensor.get_count(56) == 0

    def test_get_count_with_sensor_id(self):
        id, count = 1, 10
        sensor.sensors_count[id] = count
        assert sensor.get_count(id) == count
    

    def test_reg_movement_in_greater_than_out(self):
        id, in_, out, date = 1, 10, 5, '10/10/2020'
        sensor.register_movement(id, date, in_, out)
        assert sensor.sensors_count[id] == in_ - out
    
    def test_reg_movement_in_lower_than_out_throws_exception(self):
        print('2')
        id, in_, out, date = 1, 3, 5, '10/10/2020'

        self.assertRaises(SensorException, sensor.register_movement, id, date, in_, out)

    def test_reg_movement_out_zero(self):
        id, in_, out, date = 1, 10, 0, '10/10/2020'
        sensor.register_movement(id, date, in_, out)
        assert sensor.sensors_count[id] == in_ - out
    
    def test_reg_movement_registered_sensor(self):
        id = 1
        in_1, out_1, date = 5, 2, '10/10/2020'
        sensor.register_movement(id, date, in_1, out_1)

        in_2, out_2, date = 5, 3, '11/10/2020'
        sensor.register_movement(id, date, in_2, out_2)

        assert sensor.sensors_count[id] == in_1 + in_2 - out_1 - out_2

    def test_reg_movement_out_greater_than_registered_throws_exception(self):
        id = 1
        in_1, out_1, date = 1, 0, '10/10/2020'
        sensor.register_movement(id, date, in_1, out_1)

        in_2, out_2, date = 1, 3, '11/10/2020'

        self.assertRaises(SensorException, sensor.register_movement, id, date, in_2, out_2)
    
    def test_reg_movement_out_lower_registered_sensor_but_greater_than_in(self):
        id = 1
        in_1, out_1, date = 5, 2, '10/10/2020'
        sensor.register_movement(id, date, in_1, out_1)

        in_2, out_2, date = 1, 2, '11/10/2020'
        sensor.register_movement(id, date, in_2, out_2)

        assert sensor.sensors_count[id] == in_1 + in_2 - out_1 - out_2


if __name__ == '__main__':
    unittest.main()