import yaml
from utils.notifier import send_alert

try:
    with open("config.yaml") as f:
        config = yaml.safe_load(f)

    provider = config.get('provider', 'demo')
    print(f"Checking email bounces for provider: {provider}")

    # Fake bounce check
    print("Simulating bounce check... No bounces found!")

except Exception as e:
    send_alert(f"Bounce Monitor Failed: {str(e)}")

