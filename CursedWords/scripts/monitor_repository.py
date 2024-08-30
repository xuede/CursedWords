import os
import requests
import json

MULTION_API_KEY = os.environ.get('MULTION_API_KEY')
MULTION_API_URL = 'https://api.multion.ai/v1/web/browse'
REPO_URL = 'https://github.com/xuede/CursedWords'  # Updated with your username

def monitor_repository():
    payload = {
        "cmd": f"Check the repository at {REPO_URL} for any signs of defacement or inappropriate content. Review recent commits and pull requests.",
        "url": REPO_URL,
        "local": False
    }
    headers = {
        "X_MULTION_API_KEY": MULTION_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(MULTION_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        return result['message']
    else:
        raise Exception(f"Error monitoring repository: {response.status_code}")

def main():
    try:
        report = monitor_repository()
        issues_detected = "defacement" in report.lower() or "inappropriate" in report.lower()

        # Use a relative path for the monitoring report
        report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'monitoring_report.md')
        
        with open(report_path, 'w') as f:
            f.write("# Repository Monitoring Report\n\n")
            f.write(report + "\n\n")
            if issues_detected:
                f.write("⚠️ Potential issues detected. Please review the report and take necessary actions.\n")
            else:
                f.write("✅ No issues detected.\n")

        if issues_detected:
            exit(1)  # Non-zero exit to trigger issue creation
        else:
            print("Monitoring completed successfully. No issues detected.")
    except Exception as e:
        print(f"An error occurred during monitoring: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()