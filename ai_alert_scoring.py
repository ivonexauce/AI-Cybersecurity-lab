import json

# Simple AI-style logic for alert scoring
def score_alert(alert):
    score = 0
    if "ICMP" in alert:
        score += 20
    if "Priority: 2" in alert:
        score += 30
    return score

def analyze_wazuh(filename):
    with open(filename) as f:
        data = json.load(f)
        score = data["rule"]["level"] * 10
        print(f"Wazuh Alert Score: {score} - {data['rule']['description']}")

def analyze_snort(filename):
    with open(filename) as f:
        alert = f.read()
        score = score_alert(alert)
        print(f"Snort Alert Score: {score} - Ping Detected")

# Run both
analyze_snort("snort_alerts/snort_output.log")
analyze_wazuh("wazuh_alerts/wazuh_sample.json")
