def segment_txt(txt_path, output_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(output_path, 'a', encoding='utf-8') as f:
        for c in content.split('.'):
            f.writelines(c + '\n')
