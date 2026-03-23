



from flask import Flask
app = Flask (_name_)

@app.route("/")
def home():
	return "Hello Devops"

app.run(host="0.0.0.0", port=5000)



@app.route(/"test")
def test():
	return "Test route"

















