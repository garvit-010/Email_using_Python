# Email Python Script

## Overview

This script allows you to send emails using the `yagmail` library in Python. It supports sending emails with attachments, CC, BCC, and HTML formatting. The script securely retrieves email credentials from a `.env` file.

## Prerequisites

Before using the script, ensure the following are installed:
- **Python** on your system.
- **yagmail** and **python-dotenv** libraries, which can be installed using pip.

## Setting Up Environment Variables

The script uses environment variables to store sensitive information such as email credentials. Create a `.env` file in the root directory of your project, which should contain your email credentials.

### Example `.env` File:
- `USER_EMAIL`: Your email address.
- `USER_PASSWORD`: Your email account password (preferably, use an app-specific password for better security).

## Features

1. **Email Sending**: The script allows you to send emails to one or more recipients.
2. **Attachments**: You can attach files to your email by specifying their file paths.
3. **CC and BCC**: The script supports CC (carbon copy) and BCC (blind carbon copy) recipients.
4. **HTML Support**: You can send emails with HTML formatting for rich content.
5. **Secure Credentials**: Email credentials are stored in a `.env` file, keeping them out of the source code.

## Usage Instructions

1. **Environment Variables**: Ensure you have added your email and password in the `.env` file.
2. **Running the Script**: Update the email details (recipient, subject, message, attachments) in the script and run it. The email will be sent using your specified settings.
3. **Attachments**: Attach files by specifying their paths in the script.
4. **Message Format**: You can choose to send the message in plain text or HTML format.

## Notes:

- Ensure your email provider allows SMTP access (some providers might block or limit outgoing emails).
- You may need to enable "less secure app access" or generate an app-specific password for email accounts with stricter security settings (e.g., Gmail).
- Be cautious about sharing or storing `.env` files with sensitive information.

## Recommendations:

- **Security**: Avoid hardcoding email credentials in your scripts. Instead, use environment variables as shown here.
- **Environment**: Ensure the `.env` file is in the same directory as your script, or specify the path if it's located elsewhere.
- **Email Limits**: Be aware of any sending limits set by your email provider (especially if you're sending bulk emails).


