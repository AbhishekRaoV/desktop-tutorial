import requests

# The code snippet you provided is setting up the necessary parameters and API endpoint to make a
# request to a chatbot model deployed on Google Cloud's AI Platform.
ACCESS_TOKEN = "<ACCESS TOKEN>"
MODEL_ID = "chat-bison"
PROJECT_ID = "arena-challenge"
API_ENDPOINT = f"https://us-central1-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/us-central1/publishers/google/models/{MODEL_ID}:predict"

# The `headers` variable is a dictionary that contains the headers to be included in the API request.
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}

# Initialize conversation with a system message
conversation = [
    {"role": "system", "content": "First say hi, then user replies, next ask the user for employee id then user enters employee id then ask user name then user enters name, next act as an interviewer that ask the user which technology stack he knows and then ask questions on that stack but dont give answers to user"},
]

while True:
    # Prepare data for the API request
    data = {
        "instances": [
            {
                "messages": conversation,
            }
        ],
        "parameters": {
            "temperature": 0.3,
            "maxOutputTokens": 200,
            "topP": 0.8,
            "topK": 40,
        },
    }

    # Make API request
    response = requests.post(API_ENDPOINT, json=data, headers=headers)

    if response.status_code == 200:
        # Extract and print the model's reply
        predictions = response.json().get("predictions", [])
        if predictions:
            candidates = predictions[0].get("candidates", [])
            if candidates:
                model_reply = candidates[0].get("content", "No content found")
                print("Bot:", model_reply)

                # Update the conversation with the model's reply
                conversation.append({"role": "assistant", "content": model_reply})
            else:
                print("No candidates found in the response.")
        else:
            print("No predictions found in the response.")
    else:
        print("Error:")
        print(response.status_code, response.text)

    # Prompt user for input
    user_input = input("You: ")

    # Add user's question to the conversation
    conversation.append({"role": "user", "content": user_input})

    # Write the entire conversation to the file
    with open("user_input.txt", "w") as file:
        for message in conversation:
            file.write(f"{message['role']}: {message['content']}\n")


