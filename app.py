from flask import Flask, request, jsonify, send_file
from PythonScripts.self_drivencar import Accelerator,Accident, airbags_burstout
import cv2
import os

app = Flask(__name__)


'''@app.route('/airbags', methods=['GET','POST'])
def accident_event_api():
    airbags_deployed = False

    if request.method == 'GET':
        event_id = request.args.get('accident_id', default="401")
    else:
        data = request.get_json(silent=True) or request.form or {}
        event_id = data.get('accident_id', "401")

    if event_id == "401":
        result = airbags_burstout(event_id)
        airbags_deployed = True if result is None else bool(result)

    # when deployed, create/overwrite the image and return it immediately
    if airbags_deployed:
        src_path = os.path.join(os.getcwd(), 'accident.jpg')
        out_path = os.path.join(os.getcwd(), 'airbags_deployment.jpg')

        img = cv2.imread(src_path)
        if img is None:
            return jsonify({'error': 'source image not found', 'source': src_path}), 404

        # draw indicator and save
        cv2.circle(img, (200, 200), 100, (0, 255, 0), -1)
        saved = cv2.imwrite(out_path, img)
        if saved and os.path.exists(out_path):
            return send_file(out_path, mimetype='image/jpeg')
        else:
            return jsonify({'error': 'failed to write output image', 'path': out_path}), 500

    # default response when no image to return
    return jsonify({'airbags_deployed': airbags_deployed}), 200'''

@app.route('/accident_impact', methods=['GET'])
def accident_impact_api():
    
    VEHICLE_TYPE_WEIGHT = {
        "suv": 1.3,        # heavier → more inertia → higher damage potential
        "sedan": 1.0,
        "hatchback": 0.8
    }

    COLLISION_FACTOR = {
        "car": 1.0,
        "suv": 1.2,
        "truck": 1.8,
        "bus": 2.0,
        "motorcycle": 0.5
    }

    #user has to input parameters via GET request
    vehicle_type = request.args.get('vehicle_type')
    speed_str = request.args.get('speed')
    collider_type = request.args.get('collider_type')

    if not vehicle_type:
        return jsonify({'error': 'vehicle_type is required'}), 400
    vehicle_type = vehicle_type.lower()
    if vehicle_type not in VEHICLE_TYPE_WEIGHT:
        return jsonify({'error': 'invalid vehicle_type'}), 400
    vehicle_type_weight = VEHICLE_TYPE_WEIGHT[vehicle_type]
    
    if not speed_str:
        return jsonify({'error': 'speed is required'}), 400
    try:
        speed = float(speed_str)
    except ValueError:
        return jsonify({'error': 'speed must be a number'}), 400
    
    if not collider_type:
        return jsonify({'error': 'collider_type is required'}), 400
    collider_type = collider_type.lower()
    if collider_type not in COLLISION_FACTOR:
        return jsonify({'error': 'invalid collider_type'}), 400
    collision_factor = COLLISION_FACTOR[collider_type]
    mass = 1500  # average mass in kg

    accn = Accelerator(5)        # example acceleration in m/s²
    force = mass*accn.acceleration          # example force in arbitrary units
    

    impact_score = Accident.calculate_impact(vehicle_type, vehicle_type_weight, speed, force, collider_type, collision_factor)

    if impact_score > 80:
        feedback = {"feedback": "High structural damage. Replace bumper, hood, headlights, airbags."}
    elif impact_score > 60:
        feedback = {"feedback": "Moderate damage. Replace bumper, grills, radiator holders."}
    elif impact_score > 40:
        feedback = {"feedback": "External damage. Minor dents, repaint."}
    else:
        feedback = {"feedback": "Light impact. Cosmetic repair only."}

    return jsonify({
        'vehicle_type': vehicle_type,
        'vehicle_type_weight': vehicle_type_weight,
        'speed_mph': speed,
        'force': force,
        'collider_type': collider_type,
        'collision_factor': collision_factor,
        'impact_score': impact_score,
        'feedback': feedback
    }), 200
    
if __name__ == '__main__':
    app.run(debug=True)