from flask import Flask, request, jsonify
from safety import airbags_burstout
import cv2
from django.http import HttpResponse

app = Flask(__name__)
@app.route('/airbags', methods=['POST'])
def accident_event_api(acc_id,car):

    #requesting for information from the client side
    event_id = acc_id
    if event_id == "401":
        #excute the airbags burstout function
        airbags_burstout(event_id)
        airbags_deployed = (event_id == "Accident")

    response = {
        'accident_id': event_id,
        'airbags_deployed': airbags_deployed
    }

    #create a visual with computer vision to show airbags deployment
    if airbags_deployed:
        img = cv2.imread('car_accident.jpg')
        cv2.putText(img, 'Airbags Deployed', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imwrite('airbags_deployment.jpg', img)
        response['image'] = 'airbags_deployment.jpg'

    return HttpResponse(jsonify(response), status=200)

