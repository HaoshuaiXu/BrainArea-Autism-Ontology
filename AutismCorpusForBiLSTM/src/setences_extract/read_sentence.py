def get_sentence_data(txt_filepath):
    with open(txt_filepath, 'r', encoding='utf-8') as f:
        sentence = [s.strip('\n') for s in f.readlines()]
    return sentence

