def get_symptom_data(data_path) -> list:
    with open(data_path, 'r', encoding='utf-8') as f:
        symptom_list = [sl.replace('_', ' ').strip('\n') for sl in f.readlines()]
    return symptom_list

