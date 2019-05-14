# coding: utf-8
# maven 的pom分析器，读取xml，解读当前的artificial group和dependency


class PomSchema():
    artifactId = ''
    groupId = ''
    dependencies = []

    def __init__(self):
        pass


class MavenAnalizeEngine():
    def __init__(self):
        pass

    # 读取pom文件
    # path:文件地址
    # return PomSchema
    def __read_pom_content(self, path):
        schema = PomSchema()
        return schema

    # 将PomSchema 转换为pajek格式
    # schema PomSchema
    # return pajek map
    def __transSchema2Pajek(self, schema):
        pass

    # 将pajek 的map保存到filePath文件中
    # pajekMap 文本键值对
    # filePath 要保存的文件
    # 使用批量方式
    def __savePajek2File(self, pajekMap, filePath):
        pass

    def transform(self, pomfile, pajek_path):
        pomschema = self.__read_pom_content(pomfile)
        print(pomschema)
