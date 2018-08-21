# Install
Please follow the Rasa nlu document step by step
http://www.rasa.com/docs/nlu/installation/

# Training
To train a model, start the rasa_nlu.train command, and tell it where to find your configuration and your training data
```
python -m rasa_nlu.train -c nlu_config.yml --data nlu_zh.md -o models --fixed_model_name nlu --project current --verbose
```

# Example use
Use your model from python directly. After loading the model, type your messages or send 'stop' 
```
python nlu_demo.py
```
# Result example
```
Input: 冰島今天天氣
Answer:
{
  "intent": {
    "name": "weather",
    "confidence": 0.97412109375
  },
  "entities": [
    {
      "start": 2,
      "end": 4,
      "value": "今天",
      "entity": "date",
      "confidence": 0.8579809800967223,
      "extractor": "ner_crf"
    }
  ],
  "intent_ranking": [
    {
      "name": "weather",
      "confidence": 0.97412109375
    },
    {
      "name": "greet",
      "confidence": 0.0
    }
  ],
  "text": "冰島今天天氣"
}
```
