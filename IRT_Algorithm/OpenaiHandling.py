import openai

openai.api_key = 'sk-proj-AZDwdcpcwJcmvJv69X1zT3BlbkFJfuJ2AXsxLQfyiTzmOAbY'

 
prompt = "You are an AI assistant tasked with marking student answers and can only respond in 'Yes' or 'No'. You will be provided with the correct answer and the student's answer. You should evaluate the student's answer and respond only and only with a simple 'Yes' if it's correct or 'No' if it's incorrect. The assistant should only output 'Yes' or 'No' without any additional information or explanations."


def evaluate_answer(student_answer, correct_answer):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",  
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"This is the student's answer: {student_answer} and this is the correct answer {correct_answer}"}
        ]
    )
    return response.choices[0].message.content


