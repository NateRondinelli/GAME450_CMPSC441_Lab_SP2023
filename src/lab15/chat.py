import sys
from sentence_transformers import SentenceTransformer, util
from pathlib import Path
from math import sqrt
import nltk


sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))


def manhattan(a,b):
    return sum(abs(val1-val2)for val1,val2 in zip(a,b))

if __name__ == "__main__":

    # ChatGPT provided the following 2 text responses to the question: "what boss battle in the most difficult?"
    text1 = "It's difficult to determine which boss battle is the most difficult as it often depends on personal experience and skill level. However, there are some boss battles that are widely considered to be challenging by many players: Ornstein and Smough in Dark Souls, Ruby Weapon in Final Fantasy VII, Mike Tyson in Mike Tyson's Punch-Out, Sephiroth in Kingdom Hearts II, Sans in Undertale. These are just a few examples, and there are certainly many other difficult boss battles in various video games."
    text2 = "There are some boss battles that are widely considered to be extremely challenging by many players due to their complexity, high difficulty level, and the need for precise timing and strategy. Some examples of such boss battles include: The Nameless King in Dark Souls III, The Demon of Hatred in Sekiro: Shadows Die Twice, The Four Kings in Dark Souls, Omega Weapon in Final Fantasy VIII, The Final Boss in Cuphead. These are just a few examples, and there are certainly many other boss battles in various video games that are notoriously difficult."
    
    # then I used nltk to split the paragraphs into sentences
    sentences1 = nltk.sent_tokenize(text1)
    sentences2 = nltk.sent_tokenize(text2)
    
    # choose the model from huggingface.co 
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    # use the model to encode the sentences for easier comparison
    embedding_1 = model.encode(sentences1,convert_to_tensor=True)
    embedding_2 = model.encode(sentences2,convert_to_tensor=True)

    # print out the similarity rating of the sentence pairs
    print("Score using cosine similarity:\n")
    print(util.pytorch_cos_sim(embedding_1,embedding_2))
    print("\n For the above output, it is important to look at matrix positions [0][0], [1][1], [2][2] to examine the similarity of senetence 1,2,3 respectively.")

    # calculate manhattan distance for the sentences
    #print("Score using manhattan distance:\n")
    #print(embedding_1,embedding_2)

