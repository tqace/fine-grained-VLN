from pycocoevalcap.tokenizer.ptbtokenizer import PTBTokenizer
from pycocoevalcap.bleu.bleu import Bleu
from pycocoevalcap.meteor.meteor import Meteor
from pycocoevalcap.rouge.rouge import Rouge
from pycocoevalcap.cider.cider import Cider

import jieba
#使用jieba进行分词


def fun(c,r):
    c_ = {1:[c.split(' ')]}
    r_ = {1:[r.split(' ')]}
    c_ = {1:[c]}
    r_ = {1:[r]}
    #score = sentence_bleu(r_, c_,smoothing_function=smoothie)
    #score = Rouge_1(c, r)
    scorers = [
            #(Bleu(4), ["Bleu_1", "Bleu_2", "Bleu_3", "Bleu_4"]),
            #(Meteor(),"METEOR")
            (Rouge(), "ROUGE_L")
            #(Cider(), "CIDEr")
        ]

    for scorer, method in scorers:
            print('computing %s score...'%(scorer.method()))
            score, scores = scorer.compute_score(r_,c_)
            if type(method) == list:
                for sc, scs, m in zip(score, scores, method):
                    print("%s: %0.3f"%(m, sc))
            else:
                print("%s: %0.3f"%(method, score))




def main():
    #fun('leave the bathroom and turn right walk straight until you enter the kitchen area .','exit the bathroom and turn right walk into the kitchen and turn right .')
    fun('turn right pass the stair and pass the couch enter the dining room continue down the hall and stop in the kitchen.','walk past the pool and turn right .')
    fun('turn right pass the stair and pass the couch enter the dining room continue down the hall and stop in the kitchen.','walk past the stair and turn right walk past the dining room table and chair .')
    fun('turn right pass the stair and pass the couch enter the dining room continue down the hall and stop in the kitchen.','walk past the stair and turn right walk past the dining room table and chair and turn right walk past the table and chair .')
    fun('turn right pass the stair and pass the couch enter the dining room continue down the hall and stop in the kitchen.','walk past the stair and turn right walk past the dining room table and chair and turn right walk past the table and chair and stop in front of the kitchen .')
if __name__ == '__main__':
    main()
