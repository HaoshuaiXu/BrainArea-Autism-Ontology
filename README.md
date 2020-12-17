# Autism-Brain-Ontology-Extract
This project codes follows [Guillaume Genthial](https://github.com/guillaumegenthial/tf_ner).
## Install
This project depends on **python3**
You need to install **tensorflow 1.15.0**.
## Data Format
1. For name in {train, testa, testb}, create files {name}.words.txt and {name}.tags.txt that contain one sentence per line, each word / tag separated by space. I recommend using the IOBES tagging scheme.
2. Create files vocab.words.txt, vocab.tags.txt and vocab.chars.txt that contain one token per line.
3. Create a glove.npz file containing one array embeddings of shape (size_vocab_words, 300) using GloVe 840B vectors and np.savez_compressed.