"""
Developer{
FileName : [AIDB]
Author:    [JUNWEN XIE]
Date:      [2017-12-21]
Version:   [v1.0]
}


说明：该项目目的用于预测和寻找大数据数据库中具有潜在关联性的数据表

设立此项目具有以下假设：

H0 ： 假设数据表具有可能关联性
H1 ： 假设数据表没有外键相互关联
H2 ： 假设数据内容具有脏数和干扰性数据


遗留问题：
还不能对一个表单所有row遍历计算相关性，只能人工选取对比
关于除数和被除数为0的问题，那就是词典里完全没有一个与内容有关的分词
所以会出现 radical is 0 的提示，说明词典应该更新优化

词典越大，那么计算会越复杂慎重啊！！

----------------------------------------------
               Table of Content
----------------------------------------------
                Function Name

1. cleanDict(self)   小工具用来清理词典文件

2. loadFile(self)    加载远程数据库的表单

3. mergeCont(self)   结构化表单转换成非结构化文本

4. estimateContent(self,dict,num_rows) 文本分词提取词向量

5. cosineRule(self)  余弦相似度计算

6. extractItem(self,dictionary) 需要一个能把词典内容提取成数组的小工具



PS: All coding style must follow the rules below
*********************************************
            Naming  Conventions
*********************************************
--------------------------------------------
Code Element 	    |       Style           |
--------------------------------------------
Namespace 	        |      under_scored     |
--------------------------------------------
Class name 	        |      CamelCase        |
--------------------------------------------
Function name 	    |      camelCase        |
--------------------------------------------
Parameters/Locals 	|      under_scored     |
--------------------------------------------
Member variables 	|    under_scored_with_ |
--------------------------------------------
Enums and its members 	|   CamelCase       |
--------------------------------------------
Globals 	        |      g_under_scored   |
--------------------------------------------
Constants 	        |      UPPER_CASE       |
--------------------------------------------
File names 	        |   Match case Of Class |
--------------------------------------------

"""

import psycopg2
import configparser
import os
import jieba
import numpy as  np
from numpy import *

class DataProcess:

    def __init__(self):

       return None
    # 用来清洗字典的临时工具，字典去重，清除空行
    def cleanDict(self):
        file_object = open("dict_cn.txt", "r" ,encoding="UTF-8")
        write_object = open("dict.txt", "w" , encoding="UTF-8")
        text_array = []
        new_text_array = []
        try:
            read_line = file_object.readline()
            for read_line in file_object:
                 if read_line != "":
                     text_array.append(read_line)


            for i in text_array:
                if i not in new_text_array:
                    new_text_array.append(i)

            write_object.writelines(new_text_array)

        finally:
            file_object.close()
            write_object.close()

    # 从数据库加载表，配置在conn.conf中更改

    def loadFile(self):

        # loading config
        conf = configparser.ConfigParser()
        conf.read("conn.conf")
        db_name = conf.get("db", "db_name")
        db_usr = conf.get("db", "db_usr")
        db_password = conf.get("db", "db_password")
        db_host = conf.get("db", "db_host")
        db_port = conf.get("db", "db_port")
        sqlcom = conf.get("conf", "conf_command")
        # set up connection to database
        connectdb = psycopg2.connect(database=db_name, user=db_usr, password=db_password, host=db_host, port=db_port)
        cur = connectdb.cursor()
        cur.execute(sqlcom)
        rows = cur.fetchall()
        connectdb.commit()
        cur.close()
        connectdb.close()
        #return a list of touple
        return rows

    def mergeCont(self):

        # read data get the length of the row.
        data = DataProcess.loadFile(self)
        row_len = len(data[0])
        # initial the key of dict according to the rows
        memory = {}
        for i in range(0,row_len):
            memory[i]=""
        # merge content together
        for n in range(0,row_len):
            for i in data:
                memory[n] = memory[n] + str(i[n])
        return memory

    """
    测试结巴分词-》分割数据词向量-》提取特征向量-》余弦定理
    向量计算
    """
    def estimateContent(self,dict,num_rows):
        dic = dict
        array_dic=[]
        new_array_dic = []
        """
        这里需要修改一下，要读需所有row 才行哦 或者控制
        """
        # 目前这里我只取了一个row用来做测试
        seg_ = jieba.cut(dic[num_rows],cut_all=True)
        for i in seg_:
            array_dic.append(i)
        for id in array_dic:
            if id != "":
                # 去除空位数据
                new_array_dic.append(id)

        # new_array_dic is the data of content
        # let's process the consine low to compare with exist dict
        # import the dict

        dict_object = open("dict.txt", "r", encoding="UTF-8")
        text_dic = {}
        for read_line in dict_object:
                text_dic[read_line.strip()] = 0

        # 字典计算内容分词后出现的分词次数
        # print(text_dic)
        # print(new_array_dic)

        for key in new_array_dic:
            if key in text_dic.keys():
                text_dic[key] = text_dic[key] + 1

        # 现在生成了一组key值数据
        return text_dic


    def cosineRule(self):

        # 这里我们会得到两组数据 分别来自两个假设潜在关联性数据表的内容
        # 我们得到词向量字典，我们需要把字典数据数组化
        # 计算余弦相似度

        classFun = DataProcess()
        dic = classFun.mergeCont()

        analysis_c1 = classFun.estimateContent(dic, 0)
        analysis_c2 = classFun.estimateContent(dic, 1)

        analysis_c1_array = classFun.extractItem(analysis_c1)
        analysis_c2_array = classFun.extractItem(analysis_c2)
        length = len(analysis_c1_array)
        plus = 0
        c1 = 0
        c2 = 0

        print(length)

        # 这里经过处理之后的数据长度不存在不一致问题
        # 计算向量乘积
        for i in range(0,length):
            x = analysis_c1_array[i] * analysis_c2_array[i]
            plus = plus + x
            x = 0

        # 计算C1 C2平方和
        for i in range(0,length):
            c1 = c1 + analysis_c1_array[i] * analysis_c1_array[i]
            c2 = c2 + analysis_c2_array[i] * analysis_c2_array[i]


        radical = sqrt(c1) * sqrt(c2)
        if radical == 0:
            print("radical is 0")
            return radical


        cosTheta = plus / radical


        return cosTheta


    # 需要一个函数进来一个字典数据输字典值的数组

    def extractItem(self,dictionary):

        array_list = []
        for i in dictionary:
           array_list.append(dictionary[i])
        return array_list



s = DataProcess()

f = s.cosineRule()

print(f)
