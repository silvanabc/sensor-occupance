This project refers to an api, written in Python and using Flask, that enables to save and display information from the sensors.


As no database was used, the data is stored in memory.



### Endpoints
The api has two endpoints:

``` POST /api/webhook```
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `sensor` | `string` | **Required**. The sensor id |
| `date` | `date` | **Required**. The registered date |
| `in` | `integer` | **Required**. The number of people that entered the room  |
| `out` | `integer` | **Required**. The number of people that left the room |



``` GET /api/occupance/?sensor_id=123```
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `sensor_id` | `string` | **Required**. The sensor id|

Response: 
```sh 
{"inside": integer}
```


### Available Scripts

In the project directory, you can run:

`flask run`
Runs the api in the development mode.

`python -m unittest TestSensor.py`
Launches the test runner.

