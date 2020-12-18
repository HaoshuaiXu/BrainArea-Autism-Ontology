import time


from pdf2txt import batch_pdf_to_txt


if __name__ == '__main__':
    start_time = time.time()
    print('Project starts at' + str(start_time))
    batch_pdf_to_txt("/Users/xuhaoshuai/Downloads/文献集/已命名")
    end_time = time.time()
    print('Project ends at' + str(start_time) + ' and cost ' + str(end_time - start_time) + ' s')
