from TestManager import responses_log
from OpenaiHandling import create_report
import requests
import json


def getresults():

    prompt = "respond in one sentence. Given the quiz data for a student, analyze the following aspects and generate a comprehensive report: 1. Calculate the total number of questions attempted and the percentage of correct answers. 2. Analyze performance trends by question difficulty, summarizing how the student's correctness rate changes with increasing difficulty levels. 3. Identify key strengths and weaknesses: Determine which difficulty levels and question topics the student handles well and which they struggle with. 4. Provide recommendations for topics the student should focus on improving based on the quiz results. 5. Optionally, include a simple textual visualization (like a bar chart made from text characters) showing the distribution of correct and incorrect answers across different difficulty levels. The data for analysis is structured as list of lists with each sublist being a question answered in the form [question, is_correct, difficulty]"

    result = str(responses_log)

    report = create_report(prompt, result)

    return report


def send_teams_message():
    results = getresults()

    title = "Title"
    with open("./IRT_Algorithm/teamscard.json", 'r') as file:
        card_json = json.load(file)

    with open("./IRT_Algorithm/studymaterials.json", 'r') as file:
        study_materials = json.load(file)

    preference = "websites"

    selected_links = study_materials["Ecology_and_the_Environment"].get(preference, [])
    urls = [link["url"] for link in selected_links[:3]]  # Get the first 3 URLs
    titles = [link["title"] for link in selected_links[:3]]  # Get the first 3 titles

    while len(urls) < 3:
        urls.append("")
        titles.append("")

    def update_json(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, str):
                    obj[k] = v.replace("${title}", title).replace("${results}", results)\
                              .replace("${Url1}", urls[0]).replace("${urlTitle1}", titles[0])\
                              .replace("${Url2}", urls[1]).replace("${urlTitle2}", titles[1])\
                              .replace("${Url3}", urls[2]).replace("${urlTitle3}", titles[2])
                else:
                    update_json(v)
        elif isinstance(obj, list):
            for item in obj:
                update_json(item)
    
    update_json(card_json)

    print(card_json)

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

    data = {
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": card_json
            }
        ]
    }
    
    response = requests.post(base_url, params=params, json=data, headers=headers)
    
    if response.status_code in [200, 202]:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.status_code} - {response.text}")
