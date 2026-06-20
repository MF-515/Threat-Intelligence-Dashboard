from flask import Flask, render_template
import csv

app = Flask(__name__)

DATA_FILE = "threat_data.csv"

@app.route("/")
def dashboard():
    threats = []

    with open(DATA_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Failed Attempts"] = int(row["Failed Attempts"])
            threats.append(row)

    total_ips = len(threats)
    total_attempts = sum(t["Failed Attempts"] for t in threats)
    high_risk = sum(1 for t in threats if t["Risk Level"] == "HIGH")
    medium_risk = sum(1 for t in threats if t["Risk Level"] == "MEDIUM")
    low_risk = sum(1 for t in threats if t["Risk Level"] == "LOW")

    return render_template(
        "dashboard.html",
        threats=threats,
        total_ips=total_ips,
        total_attempts=total_attempts,
        high_risk=high_risk,
        medium_risk=medium_risk,
        low_risk=low_risk
    )

if __name__ == "__main__":
    app.run(debug=True)
