import requests
import json

def emotion_detector(text_to_analyze):
    # URL for the Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Define headers for the request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Define input JSON for the request
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        # Make a POST request to the Emotion Detection service
        response = requests.post(url, headers=headers, json=input_json)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON and extract emotion scores
            response_json = response.json()
            emotions = response_json.get('emotions', {})
            
            # Extract required emotions and their scores
            anger_score = emotions.get('anger', 0.0)
            disgust_score = emotions.get('disgust', 0.0)
            fear_score = emotions.get('fear', 0.0)
            joy_score = emotions.get('joy', 0.0)
            sadness_score = emotions.get('sadness', 0.0)
            
            # Find the dominant emotion
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
            }
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            
            # Construct the formatted output dictionary
            output = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
            
            return output
        else:
            print(f"Error: Emotion Detection request failed with status code {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: An exception occurred - {e}")
        return None

# Example usage
text_to_analyze = "I am so happy I am doing this."
result = emotion_detector(text_to_analyze)
print(json.dumps(result, indent=4))  # Print formatted JSON output
