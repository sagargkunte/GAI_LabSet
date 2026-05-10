from gensim.downloader import load

model = load("glove-wiki-gigaword-50")

def create_paragraph(inputWord,similarWords):
    paragraph = f"The Fasinating thing of the word {inputWord} is {', '.join(similarWords)}"
    print(paragraph)
    
inputWord = "hacking"
similarWord = [word for word,score in model.most_similar(inputWord,topn=5)]
create_paragraph(inputWord,similarWord)