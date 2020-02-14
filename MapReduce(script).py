import sys
import csv

def tokenize(mensaje):
    #mensaje = mensaje.lower()
    palabras = mensaje.split()
    return palabras

def cuenta_palabras_secuencial(documents):
    wordcount = {}
    
    # Crea un loop que recorra los documentos.
    for doc in documents:
        # tokeniza el documento
        doc_words = tokenize(doc)
        #crea un loop que recorra las palabras del documento
        for word in doc_words:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    return wordcount  
    
def main():
    local_paths = ['/Users/home/Desktop/MapReduce/shakespeare.txt']

    docs = []
    for path in local_paths:
        with open(path, 'r') as f:
            docs.append(f.read())

    words = cuenta_palabras_secuencial(docs)
    sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
    #print(sorted_words)
    header = []
    with open('/Users/home/Desktop/MapReduce/output.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(sorted_words)

if __name__ == "__main__":
    main()
    




