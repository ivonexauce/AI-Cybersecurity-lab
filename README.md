# 🔒 AI-Powered Cybersecurity Lab – Ivon Exauce Umba
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


Welcome to my mini cybersecurity lab that brings together AI and security tools for both enterprise networks and blockchain applications.

---

## 🧠 What’s Inside

| Layer       | Tool     | Purpose |
|-------------|----------|---------|
| Network IDS | Snort    | Detect network-level threats (e.g., port scans) |
| Host SIEM   | Wazuh    | Detect file tampering, unauthorized access |
| AI Analysis | Python   | Score and filter Snort/Wazuh alerts using simple logic |
| Blockchain  | Slither  | Static analysis of smart contracts |

---

## 🧪 Lab Architecture

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

## 📂 Folder Structure

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

## 🔧 Key Features

- ✅ Detect ping scans and host changes
- ✅ Use Python to score & prioritize alerts
- ✅ Audit Solidity smart contracts with open-source tools

---

## 📸 Sample Output

- `Snort` detected suspicious ICMP from `192.168.1.100`
- `Wazuh` reported file tampering at `/etc/hosts`
- `Python script` flagged repeated IPs with 90+ alerts
- `Slither` flagged 2 critical vulnerabilities in `MyContract.sol`

---

## 📘 Learning Outcome

- Learned how AI enhances traditional SIEM/IDS
- Explored real-time network + host alert systems
- Applied static analysis to blockchain smart contracts
- Built a scalable template for enterprise & research use

---

## 🚀 Contact

**Ivon Exauce Umba**  
PhD Scholar in AI & Blockchain Security  
📫 [umbayanga6bio@gmail.com](mailto:umbayanga6bio@gmail.com)  
🌐 www.umbaconsulting.com
