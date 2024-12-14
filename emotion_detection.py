import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=input_json, headers=header)
    print(response)
    formated_response = json.loads(response.text)
    emotion_prediction = formated_response['emotionPredictions'][0]['emotion']
    emotion_prediction['dominant_emotion'] = max(emotion_prediction, key=emotion_prediction.get)
    return emotion_prediction