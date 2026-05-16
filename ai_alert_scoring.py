import json
import re
from collections import defaultdict

HIGH_ALERT_THRESHOLD = 3


def parse_snort_alerts(filepath):
    alerts = []
    try:
        with open(filepath) as f:
            raw = f.read()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filepath}")
        return alerts

    for block in raw.strip().split("\n\n"):
        lines = block.strip().split("\n")
        if len(lines) < 3:
            continue
        alert = {
            "type": "",
            "classification": "",
            "priority": 0,
            "src_ip": "",
            "dst_ip": "",
            "timestamp": "",
        }
        for line in lines:
            m = re.search(r"\[\*\*\] \[\d+:\d+:\d+\] (.+?) \[\*\*\]", line)
            if m:
                alert["type"] = m.group(1).strip()
            m = re.search(r"\[Classification: (.+?)\]", line)
            if m:
                alert["classification"] = m.group(1)
            m = re.search(r"\[Priority: (\d+)\]", line)
            if m:
                alert["priority"] = int(m.group(1))
            m = re.search(
                r"(\d+\.\d+\.\d+\.\d+)\s*->\s*(\d+\.\d+\.\d+\.\d+)", line
            )
            if m:
                alert["src_ip"] = m.group(1)
                alert["dst_ip"] = m.group(2)
            m = re.search(r"^(\d+/\d+-\d+:\d+:\d+\.\d+)", line)
            if m:
                alert["timestamp"] = m.group(1)
        alerts.append(alert)
    return alerts


def score_alert(alert):
    score = 0
    if "ICMP" in alert["type"]:
        score += 20
    if "Port Scan" in alert["classification"]:
        score += 40
    score += alert["priority"] * 10
    return score


def analyze_snort(filepath):
    alerts = parse_snort_alerts(filepath)
    if not alerts:
        return [], {}

    ip_counts = defaultdict(int)
    for a in alerts:
        if a["src_ip"]:
            ip_counts[a["src_ip"]] += 1

    print("=" * 60)
    print("  Snort Alert Analysis")
    print("=" * 60)
    for a in alerts:
        s = score_alert(a)
        flag = ""
        if ip_counts[a["src_ip"]] >= HIGH_ALERT_THRESHOLD:
            flag = " <<< REPEATED IP"
        print(
            f"  [{a['timestamp']}] Score: {s:>3}  "
            f"{a['src_ip']} -> {a['dst_ip']}  |  {a['type']}{flag}"
        )

    print(
        f"\n  --- IP Alert Frequency (threshold: {HIGH_ALERT_THRESHOLD}) ---"
    )
    for ip, count in sorted(ip_counts.items(), key=lambda x: -x[1]):
        status = "FLAGGED" if count >= HIGH_ALERT_THRESHOLD else "OK"
        print(f"    {ip}: {count} alerts [{status}]")

    return alerts, ip_counts


def analyze_wazuh(filepath):
    try:
        with open(filepath) as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] Wazuh file not found: {filepath}")
        return
    except json.JSONDecodeError:
        print(f"[ERROR] Wazuh file is not valid JSON: {filepath}")
        return

    score = data["rule"]["level"] * 10
    print(f"\n{'=' * 60}")
    print("  Wazuh Alert Analysis")
    print("=" * 60)
    print(f"  Score: {score}")
    print(
        f"  Rule:  {data['rule']['description']} "
        f"(ID: {data['rule']['id']}, Level: {data['rule']['level']})"
    )
    print(f"  Agent: {data['agent']['name']} (ID: {data['agent']['id']})")
    print(f"  File:  {data['location']}")
    print(f"  Source IP: {data['srcip']}")


def main():
    alerts, ip_counts = analyze_snort("snort_alerts/snort_output.log")
    analyze_wazuh("wazuh_alerts/wazuh_sample.json")

    if ip_counts:
        print(f"\n  --- Summary ---")
        for ip, count in sorted(ip_counts.items(), key=lambda x: -x[1]):
            if count >= HIGH_ALERT_THRESHOLD:
                print(
                    f"  >>> {ip} triggered {count} alerts "
                    f"— flagged for investigation"
                )


if __name__ == "__main__":
    main()
