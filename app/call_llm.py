import requests
import json

from typing import Union

# from fastapi import FastAPI

# app = FastAPI()

# @app.post("/api/chat")
# async def chat_endpoint(chat: Chat):
#     api_url = "http://localhost:11434/api/chat"
#     response = make_chat_api_call(url=api_url, model=chat.model, message=chat.message)
#     return response

def make_chat_api_call(url, model, message):
    headers = {'Content-Type': 'application/json'}
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ],
        "stream": False
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print("Server response:", response.text)  # Print the server's response
    try:
        return response.json()
    except json.JSONDecodeError:
        print("Failed to parse server's response as JSON.")
        raise

def check_server_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Server is running")
        else:
            print("Server is not running")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

api_headers = {
    "Content-Type": "application/json"
}
api_data = {
    "model": "mistral",  # Update the model
    "messages": [
        {"role": "user", "content": "what's up amigo"}
    ]
}


if __name__ == "__main__":
    api_url = "http://localhost:11434/api/chat"
    make_chat_api_call(url=api_url, model='mistral', message='which is the better programming language' )
