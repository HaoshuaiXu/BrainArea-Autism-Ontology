from read_sentence import get_sentence_data
from read_symptom_data import get_symptom_data


sentence_list = get_sentence_data("/Users/xuhaoshuai/PycharmProjects/AutismCorpusForBiLSTM/data/segement.txt")
symptom_list = get_symptom_data("/Users/xuhaoshuai/PycharmProjects/AutismCorpusForBiLSTM/data/ASD_symptom.txt")

for symptom in symptom_list:
    for sentence in sentence_list:
        if sentence.find(symptom) == -1:
            pass
        else:
            with open("/Users/xuhaoshuai/PycharmProjects/AutismCorpusForBiLSTM/data/match.txt", 'a',
                      encoding='utf-8') as f:
                f.write(sentence + '\n')

for symptom in symptom_list:
    for sentence in sentence_list:
        symptom = symptom.lower()
        if sentence.find(symptom) == -1:
            pass
        else:
            with open("/Users/xuhaoshuai/PycharmProjects/AutismCorpusForBiLSTM/data/match.txt", 'a',
                      encoding='utf-8') as f:
                f.write(sentence + '\n')


