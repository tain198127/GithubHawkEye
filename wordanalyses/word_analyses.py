# -*- coding:utf-8 -*-
import jieba
import jieba.posseg as pseg
import xlrd


class word_analyses:
    #  词频
    wordscount = {}
    # 词性
    wordstype = {}

    # 初始化
    def __init__(self):
        jieba.load_userdict("./dict/dict.txt")

    # 判断是否是中文
    def isAllZh(self, s):
        """
        :param s:字符串
        :return: 是否包含中文
        """
        for c in s:
            if not ('\u4e00' <= c <= '\u9fa5'):
                return False
        return True

    # 计算词频词性
    def calWordsFreq(self, str):
        """
        :param str: 字符串
        :return: 词频和词性统计数据
        """
        seg_list = pseg.cut(str)
        for seg, flag in seg_list:
            if self.isAllZh(seg):
                if self.wordscount.get(seg) is None:
                    self.wordscount[seg] = 1
                    self.wordstype[seg] = flag
                else:
                    self.wordscount[seg] = self.wordscount[seg] + 1
        return self.wordscount, self.wordstype

    # 读取excel
    def readExcel(self, path, sheetIdx, beginIdx, endIdx):
        """
        :param path: 文件路径
        :param sheetIdx: sheet表的index
        :param beginIdx: 开始的列，从0开始
        :param endIdx: 结束的列，最小要比beginIdx大1
        :return:
        """
        # 文件路径
        filepath = path
        # '/Users/tain/Documents/我的坚果云/nutscloud/金蛋理财/清结算平台/工作周报统计.xlsx'
        # 打开excel
        data = xlrd.open_workbook(filepath)

        # 拿第二页
        for idx in range(beginIdx, endIdx):
            sheet = data.sheets()[sheetIdx]
            # 拿第二列数据
            columnValues = sheet.col_values(idx)

            for str in columnValues:
                if str.strip() != '':
                    # print(str)
                    self.calWordsFreq(str)


wa = word_analyses()
wa.readExcel('/Users/tain/Documents/我的坚果云/nutscloud/paper/毕业论文数据/周报统计/原始数据.xlsx', 0, 0, 1)
# readExcel('/Users/tain/Desktop/副本竞品调研内容-张宇翔20180911.xlsx',1,2,4)
# readExcel('/Users/tain/Desktop/生产环境bugs.xlsx',0,0,1)
print("key, count, type")
for key in wa.wordscount.keys():
    print("{},{},{}".format(key, wa.wordscount.get(key), wa.wordstype.get(key)))
