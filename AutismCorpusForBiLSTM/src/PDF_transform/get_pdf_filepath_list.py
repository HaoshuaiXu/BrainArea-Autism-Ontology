import os


def get_pdf_filepath_list(filepath):
    result = []
    for maindir, subdir, file_name_list in os.walk(filepath):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            result.append(apath)
    return result
