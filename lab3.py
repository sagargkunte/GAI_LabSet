from gensim.models import Word2Vec 

def createWordVecModel(text):
    model = Word2Vec(
        sentences = text,
        vector_size=50,
        window=5,
        min_count=1,
        workers=4,
        epochs=10
    )
    return model

def analyze(model,word):
    similarWord = model.wv.most_similar(word,topn=5)
    for word_,similarity in similarWord:
        print(word_,similarity)
        
        
text = [
    "The doctor saved the patient life".split(),
    "The mechanic is responsible for the bike reparing".split()
]
model = createWordVecModel(text)
analyze(model,"patient")