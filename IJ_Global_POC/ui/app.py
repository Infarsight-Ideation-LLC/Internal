from flask import Flask, render_template, jsonify, request

import subprocess

import os
 
app = Flask(__name__)
 
@app.route("/")

def home():

    return render_template("index.html")
 
 
@app.route("/run_scraper", methods=["POST"])

def run_scraper():
 
    print("Running scraper")
 
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 
    scraper_path = os.path.join(base_dir, "scripts", "scrapper.py")
 
    subprocess.run(["python", scraper_path])
 
    return jsonify({"status": "success"})
 
 
@app.route("/reports")

def get_reports():
 
    report_path = os.path.join(os.path.dirname(__file__), "..", "config", "reports.json")
 
    if os.path.exists(report_path):

        import json

        with open(report_path) as f:

            data = json.load(f)

    else:

        data = []
 
    return jsonify(data)
 
 
if __name__ == "__main__":

    app.run(debug=True)
 