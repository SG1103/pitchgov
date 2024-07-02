import requests

def send_webhook_message(text, image_url):
    base_url = "https://prod-18.uksouth.logic.azure.com:443/workflows/d918d252dbbf4e818fbf7ddba27371a5/triggers/manual/paths/invoke"
    params = {
        "api-version": "2016-06-01",
        "sp": "/triggers/manual/run",
        "sv": "1.0",
        "sig": "AI6wGxIKMHmfqH79awSoGnB3SS8_BHqex2OG2dOje6E"
    }
    headers = {
        "Content-Type": "application/json"
    }
    # Adding an image along with text in the attachments array
    data = {
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "type": "AdaptiveCard",
                    "version": "1.2",
                    "body": [
                        {
                            "type": "TextBlock",
                            "text": text,
                            "wrap": True
                        },
                        {
                            "type": "Image",
                            "url": image_url,
                            "size": "medium"
                        }
                    ]
                }
            }
        ]
    }
    
    response = requests.post(base_url, params=params, json=data, headers=headers)
    
    if response.status_code == 200:
        print("Message with image sent successfully!")
    else:
        print(f"Failed to send message: {response.status_code} - {response.text}")

# Example usage:
send_webhook_message(
    "Hello from webhook with image!",
    "https://files.oaiusercontent.com/file-7g0jLDT1CiUtbRj4BbWlAaCf?se=2024-06-30T18%3A35%3A00Z&sp=r&sv=2023-11-03&sr=b&rscc=max-age%3D604800%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3D27eda0f4-6849-4bdc-984a-c22d23f5dbba.webp&sig=BfZkwC/ru5b3SeZZfvpspEVCRoA3fShfrbetdQfaTCU%3D"
)



