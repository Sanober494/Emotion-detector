import requests

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
            # Parse the response JSON and extract the text attribute
            response_json = response.json()
            detected_text = response_json.get('text')

            return detected_text
        else:
            print(f"Error: Emotion Detection request failed with status code {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: An exception occurred - {e}")
        return None

# Example usage
text_to_analyze = "I feel so excited about my upcoming vacation!"
detected_text = emotion_detector(text_to_analyze)
print("Detected Emotion Text:", detected_text)
