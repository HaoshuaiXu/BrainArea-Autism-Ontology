import os


def get_txt_filepath_list(folder_path):
    result = []
    for maindir, subdir, file_name_list in os.walk(folder_path):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            result.append(apath)
    return result


def delete_newline_character(input_filepath, output_filepath):
    with open(input_filepath, 'r', encoding='utf-8') as f:
        input_content = f.readlines()
    already_deleted_content = [t.strip('\n') + ' ' for t in input_content]
    with open(output_filepath, 'a', encoding='utf-8') as f:
        for content in already_deleted_content:
            f.write(content)


if __name__ == '__main__':
    # 两个文件夹地址
    txt_folder_path_1 = "/Users/xuhaoshuai/Downloads/文献集/未命名txt"
    txt_folder_path_2 = "/Users/xuhaoshuai/Downloads/文献集/已命名txt"

    # 将两个文件夹地址存储到列表里
    txt_folder_path_list = get_txt_filepath_list(txt_folder_path_1)
    txt_folder_path_list.extend(get_txt_filepath_list(txt_folder_path_2))

    # 执行去除换行符的功能
    i = 0
    for tfp in txt_folder_path_list:
        delete_newline_character(tfp, '/Users/xuhaoshuai/PycharmProjects/AutismCorpusForBiLSTM/data/proceed.txt')
        i = i + 1
        print(str(i) + "/" + str(len(txt_folder_path_list)) + " Processed: " + tfp)
