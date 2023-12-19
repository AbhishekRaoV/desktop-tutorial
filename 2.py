import streamlit as st
import requests

ACCESS_TOKEN = "<ACCESS TOKEN>"
MODEL_ID = "chat-bison"
PROJECT_ID = "arena-challenge"
API_ENDPOINT = f"https://us-central1-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/us-central1/publishers/google/models/{MODEL_ID}:predict"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}

st.title("Chatbot Application")

# Initialize conversation with a system message
conversation = [
    {"role": "system", "content": "First say hi, then user replies, next ask the user for employee id then user enters employee id then ask user name then user enters name, next act as an interviewer that asks the user which technology stack he knows and then ask questions on that stack but don't give answers to the user"},
]

# Function to make API request
def make_api_request(data):
    response = requests.post(API_ENDPOINT, json=data, headers=headers)
    return response

# Main Streamlit app
while True:
    # Display conversation
    st.text_area("Conversation", value="\n".join([f"{message['role']}: {message['content']}" for message in conversation]))

    # Prompt user for input
    user_input = st.text_input("You:")

    if st.button("Send"):
        # Add user's question to the conversation
        conversation.append({"role": "user", "content": user_input})

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
        response = make_api_request(data)

        if response.status_code == 200:
            # Extract and display the model's reply
            predictions = response.json().get("predictions", [])
            if predictions:
                candidates = predictions[0].get("candidates", [])
                if candidates:
                    model_reply = candidates[0].get("content", "No content found")
                    st.text_area("Bot:", value=model_reply)

                    # Update the conversation with the model's reply
                    conversation.append({"role": "assistant", "content": model_reply})
                else:
                    st.text("No candidates found in the response.")
            else:
                st.text("No predictions found in the response.")
        else:
            st.text(f"Error: {response.status_code}, {response.text}")
