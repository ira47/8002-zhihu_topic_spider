# -*- coding: UTF-8 -*-

import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')


class Wd():
    def __init__(self, temporaryDataFileName, DataFileName):
        self.tdfn = temporaryDataFileName
        self.dfn = DataFileName
    # 记录临时数据

    def wd_temporaryData(self, jsonData):
        # pass
        file_object = open('temp.csv', 'a')
        for d in jsonData['msg'][1]:
            file_object.write(json.dumps(
                d[0][1], ensure_ascii=False, encoding="utf-8"))
            file_object.write(',')
            file_object.write(json.dumps(
                d[0][2], ensure_ascii=False, encoding="utf-8"))
            file_object.write('\n')
        file_object.close()
    # 记录话题数据

    def wd_Data(self, title, id, focus, parentsname, parentsid):
        file_object = open('data.csv', 'a')
        file_object.write('\n'+str(title)+','+str(id)+',' +
                          str(focus)+','+str(parentsname)+','+str(parentsid))
        file_object.close()
