# AI-Powered Cybersecurity Lab
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Welcome to my mini cybersecurity lab that brings together AI and security tools for both enterprise networks and blockchain applications.

---

## What's Inside

| Layer       | Tool     | Purpose |
|-------------|----------|---------|
| Network IDS | Snort    | Detect network-level threats (e.g., port scans, ping sweeps) |
| Host SIEM   | Wazuh    | Detect file tampering, unauthorized access |
| AI Analysis | Python   | Score and analyze Snort/Wazuh alerts; flag repeated offending IPs |
| Blockchain  | Slither  | Static analysis of smart contracts |

---

## Lab Architecture

```
               [Internet]
                    |
               [Snort IDS]
                    |
               [Wazuh SIEM]
                    |
            [Python AI Analyzer]
                    |
      [Smart Contract Security (Slither)]
```

---

## Folder Structure

```
ai-cybersecurity-lab/
│
├── snort_alerts/
│   └── snort_output.log
├── wazuh_alerts/
│   └── wazuh_sample.json
├── ai_alert_scoring.py
├── contract_audit/
│   ├── MyContract.sol
│   └── slither_report.txt
└── README.md
```

---

## Key Features

- Detect ping scans and file tampering
- Score and prioritize alerts from both Snort and Wazuh
- Track IP frequency across all Snort alerts and flag suspicious repeat offenders
- Audit Solidity smart contracts with static analysis patterns

---

## Sample Output

```
============================================================
  Snort Alert Analysis
============================================================
  [06/08-12:30:23.456789] Score:  40  192.168.1.10 -> 192.168.1.100  |  ICMP Ping Detected <<< REPEATED IP
  [06/08-12:31:15.123456] Score:  40  192.168.1.10 -> 192.168.1.101  |  ICMP Ping Detected <<< REPEATED IP
  [06/08-12:32:05.789012] Score:  50  192.168.1.10 -> 192.168.1.100  |  Port Scan Detected <<< REPEATED IP
  [06/08-12:33:45.678901] Score:  40  10.0.0.5 -> 192.168.1.100      |  ICMP Ping Detected
  [06/08-12:34:22.345678] Score:  50  192.168.1.10 -> 192.168.1.102  |  Port Scan Detected <<< REPEATED IP
  [06/08-12:35:10.987654] Score:  40  10.0.0.5 -> 192.168.1.101      |  ICMP Ping Detected

  --- IP Alert Frequency (threshold: 3) ---
    192.168.1.10: 4 alerts [FLAGGED]
    10.0.0.5: 2 alerts [OK]

============================================================
  Wazuh Alert Analysis
============================================================
  Score: 70
  Rule:  File modified on /etc/hosts (ID: 554, Level: 7)
  Agent: local-agent (ID: 001)
  File:  /etc/hosts
  Source IP: 192.168.1.10

  --- Summary ---
  >>> 192.168.1.10 triggered 4 alerts — flagged for investigation
```

---

## Learning Outcome

- Learned how AI enhances traditional SIEM/IDS
- Explored real-time network + host alert systems
- Applied static analysis to blockchain smart contracts
- Built a scalable template for enterprise & research use

---

## Contact
🙌 Contributors & Community
### UMBA YANGA IVON EXAUCE  
**Deep-Tech Systems Architect & Innovation Strategist**  
Founder & CEO UMBA Consulting Engineers  

🎓 AI • Blockchain Security • Computational Nanoscience • Smart Enterprise Systems  
🌐 umbaconsulting.com  
📧 umbayanga6bio@gmail.com  
