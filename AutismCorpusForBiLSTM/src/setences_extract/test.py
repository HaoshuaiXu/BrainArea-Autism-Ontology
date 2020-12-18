from read_symptom_data import get_symptom_data


symptom_list = get_symptom_data("/Users/xuhaoshuai/PycharmProjects/AutismCorpusForBiLSTM/data/ASD_symptom.txt")
for s in symptom_list:
    print(s.lower())