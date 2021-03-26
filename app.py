from core import translate, load_model
from pprint import pprint
MODEL_DIR = '.'

def loading(model_dir):
    confo = load_model(model_dir)
    return confo


def traduis(message, confo):
   
    answer = translate(message, **confo)
    return answer
    

