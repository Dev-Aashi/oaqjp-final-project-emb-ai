import requests
import json

def emotion_detector(text_analyzed):
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    INPUT_JSON = {'raw_document': {'text': text_analyzed}}
    response = requests.post(URL, headers=HEADERS, json=INPUT_JSON)
    status_code = response.status_code
    json_doc = json.loads(response.text)

    if status_code == 400:
        return {
            "anger":None,
            "disgust":None,
            "fear":None,
            "joy":None,
            "sadness":None,
            "dominant_emotion":None
        }
    else:
        #Extract score
        anger = json_doc['emotionPrediction'][0]["emotion"]['anger']
        disgust = json_doc['emotionPrediction'][0]["emotion"]['disgust']
        fear = json_doc['emotionPrediction'][0]["emotion"]['fear']
        joy = json_doc['emotionPrediction'][0]["emotion"]['joy']
        sadness = json_doc['emotionPrediction'][0]["emotion"]['sadness']

        max_score = 0
        emotion = ''

        for i in json_doc['emotionPrediction'][0]["emotion"].items():
            if i[1] > max_score:
                max_score = i[1]
                emotion = i[0]

        return {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
            "dominant_emotion": emotion
        }
