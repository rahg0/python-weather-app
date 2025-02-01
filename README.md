# python-weather-app

## Installation
1. Clone the repo:
```sh
$ git clone https://github.com/rahg0/python-weather-app.git
```

2. Install all the packages as per requirements.txt:
```sh
$ pip install -r requirements.txt
```

3. Create an [OpenWeather](https://openweathermap.org/) account and generate an API Key.

4. Assign the API Key for **api_key** in app.py file. 

5. Run the application:
```sh
$ python app.py
Enter the city name: bengaluru
Weather in Bengaluru:
Temperature: 30.6°C
Condition: Broken clouds
```

## Scan for Security Issues
```sh
$ orca-cli fs scan ./
  ____   ___   _____ ___      ____ ____ _____ __  __ ___   ____ ________  __
 / __ \ / _ \ / ___// _ |    / __// __// ___// / / // _ \ /  _//_  __/\ \/ /
/ /_/ // , _// /__ / __ |   _\ \ / _/ / /__ / /_/ // , _/_/ /   / /    \  /
\____//_/|_| \___//_/ |_|  /___//___/ \___/ \____//_/|_|/___/  /_/     /_/
✓ Performing file system scanning for security risks
✓ Performing results analysis and policy decision (via Orca Cloud)

========================================================================
VULNERABILITIES
pip (./requirements.txt)
[TOTAL: 8 | CRITICAL: 2 | HIGH: 3 | MEDIUM: 3 | LOW: 0 | UNKNOWN: 0]
╭──────────┬──────────────────┬───────────────────┬───────────────┬──────────┬───────┬───────┬────────╮
│ PACKAGE  │ VULNERABILITY ID │ INSTALLED VERSION │ FIXED VERSION │ SEVERITY │ CVSS2 │ CVSS3 │ STATUS │
├──────────┼──────────────────┼───────────────────┼───────────────┼──────────┼───────┼───────┼────────┤
│ agpt     │ CVE-2024-6091    │ 0.2.2             │               │ CRITICAL │       │ 9.8   │ FAILED │
├──────────┼──────────────────┼───────────────────┼───────────────┼──────────┼───────┼───────┼────────┤
│ gradio   │ CVE-2025-23042   │ 5.10.0            │ 5.11.0        │ CRITICAL │       │       │ FAILED │
├──────────┼──────────────────┼───────────────────┼───────────────┼──────────┼───────┼───────┼────────┤
│ flask    │ CVE-2023-30861   │ 1.0.2             │ 2.3.2, 2.2.5  │ HIGH     │       │ 7.5   │ FAILED │
├──────────┼──────────────────┼───────────────────┼───────────────┼──────────┼───────┼───────┼────────┤
│ waitress │ CVE-2022-24761   │ 2.0.0             │ 2.1.1         │ HIGH     │ 5     │ 7.5   │ FAILED │
├──────────┼──────────────────┼───────────────────┼───────────────┼──────────┼───────┼───────┼────────┤
│ waitress │ CVE-2024-49769   │ 2.0.0             │ 3.0.1         │ HIGH     │       │ 7.5   │ FAILED │
├──────────┼──────────────────┼───────────────────┼───────────────┼──────────┼───────┼───────┼────────┤
│ requests │ CVE-2023-32681   │ 2.26.0            │ 2.31.0        │ MEDIUM   │       │ 6.1   │ FAILED │
├──────────┼──────────────────┼───────────────────┼───────────────┼──────────┼───────┼───────┼────────┤
│ requests │ CVE-2024-35195   │ 2.26.0            │ 2.32.0        │ MEDIUM   │       │ 5.6   │ FAILED │
├──────────┼──────────────────┼───────────────────┼───────────────┼──────────┼───────┼───────┼────────┤
│ waitress │ CVE-2024-49768   │ 2.0.0             │ 3.0.1         │ MEDIUM   │       │ 4.8   │ FAILED │
╰──────────┴──────────────────┴───────────────────┴───────────────┴──────────┴───────┴───────┴────────╯
```
