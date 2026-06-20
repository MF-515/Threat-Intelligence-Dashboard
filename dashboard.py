import csv

DATA_FILE = "threat_data.csv"

threats = []

with open(DATA_FILE, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        threats.append(row)

total_ips = len(threats)
high_risk = 0
medium_risk = 0
low_risk = 0
total_attempts = 0

for threat in threats:
    attempts = int(threat["Failed Attempts"])
    total_attempts += attempts

    if threat["Risk Level"] == "HIGH":
        high_risk += 1
    elif threat["Risk Level"] == "MEDIUM":
        medium_risk += 1
    elif threat["Risk Level"] == "LOW":
        low_risk += 1

html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Threat Intelligence Dashboard</title>
</head>
<body>
    <h1>Threat Intelligence Dashboard</h1>

    <h2>Security Summary</h2>
    <p>Total Suspicious IPs: {total_ips}</p>
    <p>Total Failed Attempts: {total_attempts}</p>
    <p>High Risk IPs: {high_risk}</p>
    <p>Medium Risk IPs: {medium_risk}</p>
    <p>Low Risk IPs: {low_risk}</p>

    <h2>Threat Details</h2>

    <table border="1">
        <tr>
            <th>IP Address</th>
            <th>Failed Attempts</th>
            <th>Risk Level</th>
            <th>Country</th>
        </tr>
"""

for threat in threats:
    html += f"""
        <tr>
            <td>{threat["IP Address"]}</td>
            <td>{threat["Failed Attempts"]}</td>
            <td>{threat["Risk Level"]}</td>
            <td>{threat["Country"]}</td>
        </tr>
    """

html += """
    </table>
</body>
</html>
"""

with open("dashboard.html", "w") as file:
    file.write(html)

print("Dashboard generated successfully: dashboard.html")
