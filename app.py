from crypt import methods
from http.client import responses

from flask import Flask, request, jsonify
from DataModel.CalibrationData import CalibrationData
from DataModel.XRayMap import XRayMap

app = Flask(__name__)


@app.route('/calibration', methods=['POST'])
def calibration():
    data = request.get_json()
    try:
        calibration_data = CalibrationData(**data)
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Invalid Input Data: {str(e)}"
        }), 400

    print(f"Data: {calibration_data}")

    #get your input data from the request from the variable calibration_data
    # process your input data
    #generate response and add it to response_data
    response_data = {
        "status": "ok",
        "message": f"Calibration Data Received: {calibration_data}"
    }

    return jsonify(response_data), 200

@app.route('/xray-map-tissue-thickness', methods=['POST'])
def xray_mapping():
    data = request.get_json()
    try:
        x_ray_map_data = XRayMap(**data)
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Invalid Input Data: {str(e)}"
        }), 400

    print(f"Data: {x_ray_map_data}")


    response_data = {
        "status": "ok",
        "message": f"x_ray_map_data Data Received: {x_ray_map_data}"
    }

    return jsonify(response_data), 200

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
