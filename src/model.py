#! ./venv/bin/python3.10
import os
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
from torch.nn.functional import softmax

"""
  "id2label": {
    "0": "clean",
    "1": "mild gibberish",
    "2": "noise",
    "3": "word salad"
  }

"""
CACHE_DIR = "../model_weights"
CLASS_MAPPING = ["clean", "mild gibberish", "noise", "word salad"]

def getModel():
    return DistilBertForSequenceClassification.from_pretrained("madhurjindal/autonlp-Gibberish-Detector-492513457", cache_dir=CACHE_DIR)

def getTokenizer():
    return DistilBertTokenizer.from_pretrained("madhurjindal/autonlp-Gibberish-Detector-492513457", cache_dir=CACHE_DIR)


def predict(text: str, model:DistilBertForSequenceClassification, tokenizer:DistilBertTokenizer):
    tokenized_text = tokenizer(text, return_tensors='pt')
    logits = model(**tokenized_text)

    probabilites = softmax(logits.logits[0], dim=0)

    class_detected = probabilites.argmax(dim=0).item()

    return {"classPredicted": CLASS_MAPPING[class_detected], "confidence": probabilites[class_detected].item()}


def pipeline(inp):
    model = getModel()
    tokenizer = getTokenizer()
    res = predict(inp, model, tokenizer) # type: ignore

    return res


if __name__ == "__main__":
    inp = "This is something special"
    print(pipeline(inp))