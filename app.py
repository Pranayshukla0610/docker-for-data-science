from flask import Flask, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
	return "Docker + Flask + Data Science running on AWS EC2!"

@app.route("/sample")
def sample():
	data = {
		"mean": float(np.mean([1,2,3,4,5])),
		"sum": int(np.sum([1,2,3,4,5]))
	}
	return jsonify(data)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
