from TestManager import responses_log
from OpenaiHandling import create_report

def getresults():

    prompt = "Given the quiz data for a student, analyze the following aspects and generate a comprehensive report: 1. Calculate the total number of questions attempted and the percentage of correct answers. 2. Analyze performance trends by question difficulty, summarizing how the student's correctness rate changes with increasing difficulty levels. 3. Identify key strengths and weaknesses: Determine which difficulty levels and question topics the student handles well and which they struggle with. 4. Provide recommendations for topics the student should focus on improving based on the quiz results. 5. Optionally, include a simple textual visualization (like a bar chart made from text characters) showing the distribution of correct and incorrect answers across different difficulty levels. The data for analysis is structured as list of lists with each sublist being a question answered in the form [question, is_correct, difficulty]"

    result = str(responses_log)

    print(result)

    report = create_report(prompt, result)

    return report
