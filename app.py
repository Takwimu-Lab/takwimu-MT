from core import translate, load_model
from pprint import pprint
MODEL_DIR = '.'

def loading():
    global confo
    confo = load_model("models/fr_ewe_bpe4000_transformer")
#     pprint(confo)


def traduis(message):
   
    answer = translate(message, **confo)
    return answer
    
loading()
# print(traduis("Wàhálà mélòó ni mo lè là kọjá láti"))
