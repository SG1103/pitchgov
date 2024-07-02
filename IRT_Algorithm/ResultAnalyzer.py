from TestManager import responses_log
from OpenaiHandling import create_report
import requests


def getresults():

    prompt = "Given the quiz data for a student, analyze the following aspects and generate a comprehensive report: 1. Calculate the total number of questions attempted and the percentage of correct answers. 2. Analyze performance trends by question difficulty, summarizing how the student's correctness rate changes with increasing difficulty levels. 3. Identify key strengths and weaknesses: Determine which difficulty levels and question topics the student handles well and which they struggle with. 4. Provide recommendations for topics the student should focus on improving based on the quiz results. 5. Optionally, include a simple textual visualization (like a bar chart made from text characters) showing the distribution of correct and incorrect answers across different difficulty levels. The data for analysis is structured as list of lists with each sublist being a question answered in the form [question, is_correct, difficulty]"

    result = str(responses_log)

    print(result)

    report = create_report(prompt, result)

    return report


def send_teams_message():

    text = getresults()

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
    # Define the attachments array with your required data structure
    data = {
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "type": "AdaptiveCard",
                    "body": [
                        {
                            "type": "TextBlock",
                            "text": text
                        }
                    ]
                }
            }
        ]
    }
    
    response = requests.post(base_url, params=params, json=data, headers=headers)
    
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.status_code} - {response.text}")