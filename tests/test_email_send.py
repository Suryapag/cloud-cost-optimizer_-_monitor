import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared.notifier import send_error_email

# Test email content
subject = "✅ Test Email from Cloud Cost Optimizer"
body = "This is a test to confirm that your email setup is working."

send_error_email(subject, body)
