from gensim.downloader import load 

print("Loading pretrained model!")
model = load("glove-wiki-gigaword-50")

def main():
    res = model.most_similar(positive=["king","women"],negative=["man"],topn=1)
    print("First response is ",res)

main()