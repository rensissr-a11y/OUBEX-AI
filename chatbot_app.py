import os
from flask import Flask, request, jsonify
from openai import OpenAI

# ඔයාගේ OpenAI API key එක මෙතන දාන්න
client = OpenAI(api_key="OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_chatbot():
    data = request.get_json()
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({'response': 'Please enter a message.'})

    try:
        # OpenAI API එකට ප්‍රශ්නය යැවීම
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # භාවිතා කරන AI model එක (මේක වෙනස් කරන්න පුළුවන්)
            messages=[
                {"role": "user", "content": user_message}
            ]
        )

        # උත්තරය ලබාගැනීම
        chatbot_response = response.choices[0].message.content.strip()

        return jsonify({'response': chatbot_response})

    except Exception as e:
        return jsonify({'response': f"An error occurred: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
