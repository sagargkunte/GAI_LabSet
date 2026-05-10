import matplotlib.pyplot as plt
from gensim.downloader import load
from sklearn.decomposition import PCA


def reduce(embeddings):
    pca = PCA(n_components=2)
    response = pca.fit_transform(embeddings)
    return response

def visualize(words,embeddings):
    plt.figure(figsize=(10,6))
    for i,word in enumerate(words):
        x,y = embeddings[i]
        plt.scatter(x,y,marker="o",color="blue")
        plt.text(x + 0.02,y + 0.02,word,fontsize=12)
    plt.show()  

# def generateSimilarWords(word):
#     similarWords = model.most_similar(word)
#     for word_,pred in similarWords:
#         print(word_,pred)
    
print("Loading pretrained model!")
model = load("glove-wiki-gigaword-50")
words = ["volleyball","football","basketball","handball","soccer"]
# words = ['football', 'basketball', 'soccer', 'tennis', 'cricket']
embeddings = [model[word] for word in words]

reducedEmbeddings = reduce(embeddings)
visualize(words,reducedEmbeddings)  


