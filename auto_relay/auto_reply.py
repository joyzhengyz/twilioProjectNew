from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def auto_reply():
    resp = twilio.twiml.Response()
    resp.message("Hello from CS 643, my name is Yezhen Zheng")
    return str(resp)
if __name__ == "__main__":
    app.run(debug=True)
