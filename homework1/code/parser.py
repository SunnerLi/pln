import random
from providedcode import dataset
from providedcode.transitionparser import TransitionParser
from providedcode.evaluate import DependencyEvaluator
from featureextractor import FeatureExtractor
from transition import Transition
from providedcode.dependencygraph import DependencyGraph 

if __name__ == '__main__':
    data = dataset.get_english_train_corpus().parsed_sents()
    random.seed(1234)
    subdata = random.sample(data, 200)    

    # parsing arbitrary sentences (english):
    sentence = DependencyGraph.from_sentence('Hi, this is a test')

    tp = TransitionParser.load('english.model')
    parsed = tp.parse([sentence])
    print parsed[0].to_conll(10).encode('utf-8')