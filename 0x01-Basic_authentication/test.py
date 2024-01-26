from flask import Flask, request

app = Flask(__name__)

# Function to be executed before each request
@app.before_request
def before_request():
    print("Executing before_request function.")
    # You can perform any setup or validation tasks here if needed.
    # For example, you can access request data using `request` object.

# Route definition
@app.route('/hello')
def index():
    user_agent = request.headers.get('User-Agent')
    user_auth = request.headers
    #('Authorization')
    #print(request.path)
    #print(user_agent)
    #if 'Authorization' in user_agent:
    print(type(user_auth))
    print(user_auth.get('Authorization'))
    
    
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

