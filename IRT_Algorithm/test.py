import requests
import json



def send_teams_message():

    with open("./IRT_Algorithm/teamscard.json", 'r') as file:
        card_json = json.load(file)

    title = "Title"
    results = "results"
    view_url = "https://chatgpt.com/c/8921ed03-ab66-4c3e-876b-111cf528b5dd"

    card_json_str = json.dumps(card_json)
    card_json_str = card_json_str.replace("${title}", title)
    card_json_str = card_json_str.replace("${results}", results)
    card_json_str = card_json_str.replace("${viewUrl}", view_url)
    card_json = json.loads(card_json_str)

    print(type(card_json))

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
                "content": card_json
                                    }
                                ]
                            }
    
    response = requests.post(base_url, params=params, json=data, headers=headers)
    
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.status_code} - {response.text}")
# Example usage:
send_teams_message()



