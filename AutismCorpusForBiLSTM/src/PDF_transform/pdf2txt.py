import time
import os
import re


from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument, PDFTextExtractionNotAllowed
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfpage import PDFPage


def pdf_to_txt(pdf_file_path, txt_file_path):
    try:
        # 获取pdf文档
        fp = open(pdf_file_path, 'rb')
        parser = PDFParser(fp)
        # pdf文档的对象，与解释器连接起来
        doc = PDFDocument(parser=parser)
        parser.set_document(doc=doc)
        # 如果是加密pdf，则输入密码
        # doc._initialize_password()
        # 检测文档是否提供txt转换，不提供就忽略
        if not doc.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            # 创建pdf资源管理器
            resource = PDFResourceManager()
            # 参数分析器
            laparam = LAParams()
            # 创建一个聚合器
            device = PDFPageAggregator(resource, laparams=laparam)
            # 创建pdf页面解释器
            interpreter = PDFPageInterpreter(resource, device)
            # 获取页面的集合
            for page in PDFPage.get_pages(fp):
                # 使用页面解释器来读取
                interpreter.process_page(page)
                # 使用聚合器来获取内容
                layout = device.get_result()
                for out in layout:
                    if hasattr(out, 'get_text'):
                        # print(out.get_text())
                        # 写入txt文件
                        fw = open(txt_file_path, 'a')
                        fw.write(out.get_text())
                        fw.close()
        fp.close()
    except Exception as e:
        print(e)


def batch_pdf_to_txt(dir_path):
    files = os.listdir(dir_path)
    tar_dir = dir_path + 'txt'
    if not os.path.exists(tar_dir):
        os.mkdir(tar_dir)
    replace = re.compile(r'\.pdf', re.I)
    file_number = 0  # 标记一个变量用于计数
    for file in files:
        file_number = file_number + 1
        start_time = time.time()
        pdf_path = dir_path + '/' + file
        txt_path = tar_dir + '/' + re.sub(replace, '', file) + '.txt'
        pdf_to_txt(pdf_path, txt_path)
        end_time = time.time()
        print(str(file_number) + '/' + str(len(files)) + ', time cost: ' + str(
            end_time - start_time) + ' s, ' + "saved in " + txt_path + ' ')

