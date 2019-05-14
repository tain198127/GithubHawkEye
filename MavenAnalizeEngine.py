# coding: utf-8
# maven 的pom分析器，读取xml，解读当前的artificial group和dependency
import logging

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
logging.basicConfig()
logger = logging.getLogger("MavenAnalizeEngine")
ns = {'m': 'http://maven.apache.org/POM/4.0.0'}
ET.register_namespace('', 'http://maven.apache.org/POM/4.0.0')


class PomSchema():
    artifactId = ''
    groupId = ''
    parent_artifactId = ''
    parent_groupId = ''
    packaging = ''
    dependencies = []
    complete = False

    def __init__(self):
        pass


class MavenAnalizeEngine():
    def __init__(self):
        pass

    # 读取pom文件
    # path:文件地址
    # return PomSchema
    def __read_pom_content(self, path):
        schema = None
        try:
            tree = ET.ElementTree()
            tree.parse(path)
            artifactId = tree.find('.//m:artifactId', ns)
            groupId = tree.find(".//m:groupId", ns)
            parent_groupId = tree.find('.//m:parent/m:groupId', ns)

            packaging = tree.find('.//m:packaging', ns)

            dependencies = tree.findall('*//m:dependency', ns)

            schema = PomSchema()
            schema.artifactId = artifactId.text
            if groupId is not None:
                schema.groupId = groupId.text
            elif parent_groupId is not None:
                schema.groupId = parent_groupId.text
            else:
                raise Exception('error groupId')
            for dep in dependencies:
                dep_artifactId = dep.find('m:artifactId', ns).text
                dep_groupId = dep.find('m:groupId', ns).text
                schema.dependencies.append({'groupId': dep_groupId, 'artifactId': dep_artifactId})
            schema.complete = True
        except Exception as ex:
            logger.error(ex)
        finally:
            return schema

    # 将PomSchema 转换为pajek格式
    # schema PomSchema
    # return pajek map
    def __transSchema2Pajek(self, schema):
        data = {'key': '', 'value': ''}
        return data

    # 将pajek 的map保存到filePath文件中
    # pajekMap 文本键值对
    # filePath 要保存的文件
    # 使用批量方式
    def __savePajek2File(self, pajekMap, filePath):
        pass

    # 转换
    def transform(self, pomfile, pajek_path):
        pomschema = self.__read_pom_content(pomfile)
        if pomschema is not None and pomschema.complete:
            logger.info(pomschema)
            pajekpair = self.__transSchema2Pajek(pomschema)
            if pajekpair is not None:
                self.__savePajek2File(pajekpair, pajek_path)
