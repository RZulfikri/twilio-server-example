from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
# @app.route('/api/twilio')
# def twilio_api():
#     from twilio.rest import Client

#     # Your Account Sid and Auth Token from twilio.com/console
#     account_sid = 'AC23864c65f09d9ef4ad2ae91315303185'
#     auth_token = 'f34b0ef4a9587c5e329b0f206ffebf47'
#     client = Client(account_sid, auth_token)

#     new_key = client.new_keys.create()

#     auth = {
#         'key': new_key.sid,
#         'secret': new_key.secret
#     }
#     print(new_key.secret)

#     return jsonify(auth)

@app.route('/api/twilio/video', methods=['GET'])
def twilio_api_video():
    from twilio.jwt.access_token import AccessToken
    from twilio.jwt.access_token.grants import VideoGrant
    from twilio.rest import Client

    name = request.args.get('name')
    room = request.args.get('room')

    print(name)
    print(room)

    # Substitute your Twilio AccountSid and ApiKey details
    account_sid = 'place your account id here'
    auth_token = 'palce your auth token here'
    client = Client(account_sid, auth_token)

    new_key = client.new_keys.create()

    ACCOUNT_SID = account_sid
    API_KEY_SID = new_key.sid
    API_KEY_SECRET = new_key.secret

    # Create an Access Token
    token = AccessToken(ACCOUNT_SID, API_KEY_SID, API_KEY_SECRET)

    # Set the Identity of this token
    token.identity = name

    # Grant access to Video
    grant = VideoGrant(room=room)
    token.add_grant(grant)

    # Serialize the token as a JWT
    jwt = token.to_jwt()

    print(jwt)

    return jsonify({
        'token': jwt, 
        'name': name, 
        'room': room
        })
