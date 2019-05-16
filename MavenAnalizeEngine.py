# coding: utf-8
# maven 的pom分析器，读取xml，解读当前的artificial group和dependency
import csv
import logging
import traceback
import xml.etree.ElementTree as ET

# try:
#     import xml.etree.cElementTree as ET
#     from xml.etree.cElementTree import XMLParser
# except ImportError:
#     import xml.etree.ElementTree as ET
#     from xml.etree.ElementTree import XMLParser

logging.basicConfig()
logger = logging.getLogger("MavenAnalizeEngine")
logger.setLevel(logging.WARNING)
ns = {'m': 'http://maven.apache.org/POM/4.0.0'}
# parser = XMLParser()
# parser.parser.UseForeignDTD(True)


ET.register_namespace('', 'http://maven.apache.org/POM/4.0.0')


class PomSchema():
    artifactId = ''
    groupId = ''
    parent_artifactId = ''
    parent_groupId = ''
    packaging = ''
    dependencies = None
    complete = False

    def __init__(self):
        artifactId = ''
        groupId = ''
        parent_artifactId = ''
        parent_groupId = ''
        packaging = ''
        dependencies = None
        complete = False


class MavenAnalizeEngine():
    def __init__(self):
        pass

    # 读取pom文件
    # path:文件地址
    # return PomSchema
    def __read_pom_content(self, path):
        schema = None
        try:
            parser = ET.XMLParser(encoding="utf-8")
            tree = ET.ElementTree()
            tree.parse(path, parser=parser)
            # tree.parse(path)

            artifactId = tree.find('.//m:artifactId', ns)
            groupId = tree.find(".//m:groupId", ns)
            parent_groupId = tree.find('.//m:parent/m:groupId', ns)

            packaging = tree.find('.//m:packaging', ns)

            dependencies = tree.findall('*//m:dependency', ns)
            if artifactId is None:
                # 判断如果没有namespace
                artifactId = tree.find('.//artifactId')
                groupId = tree.find(".//groupId")
                parent_groupId = tree.find('.//parent/groupId')

                packaging = tree.find('.//packaging')

                dependencies = tree.findall('*//dependency')

            schema = PomSchema()
            schema.artifactId = artifactId.text
            if groupId is not None:
                schema.groupId = groupId.text
            elif parent_groupId is not None:
                schema.groupId = parent_groupId.text
            else:
                raise Exception('error groupId')
            tmpdependencies = []
            for dep in dependencies:
                dep_artifactId = dep.find('m:artifactId', ns)
                dep_groupId = dep.find('m:groupId', ns)
                if dep_artifactId is None:
                    dep_artifactId = dep.find('artifactId')
                    dep_groupId = dep.find('groupId')
                tmpdependencies.append({'groupId': dep_groupId.text, 'artifactId': dep_artifactId.text})
            schema.dependencies = [dict(t) for t in set([tuple(d.items()) for d in tmpdependencies])]
            # 这里要去重
            schema.complete = True
        except Exception as ex:
            traceback.print_exc()
            logger.error('error in {}'.format(path))
            # logger.error('error message : {} \n traceback.format_exc():\n{}'.format(ex.message, traceback.format_exc()))
        finally:
            return schema

    # 将PomSchema 转换为pajek格式
    # schema PomSchema
    # return pajek map
    def __transSchema2Pajek(self, schema):
        map = []
        if schema.dependencies is None or len(schema.dependencies) <= 0:
            item = {'from_group': '' + schema.groupId, 'from_arti': '' + schema.artifactId}
            map.append(item)
        for key in schema.dependencies:
            item = {'from_group': '' + schema.groupId, 'from_arti': '' + schema.artifactId,
                    'to_group': '' + key['groupId'],
                    'to_arti': '' + key['artifactId']}
            map.append(item)
        return map

    # 将pajek 的map保存到filePath文件中
    # pajekMap 文本键值对
    # filePath 要保存的文件
    # 使用批量方式
    def __savePajek2File(self, pajekMap, filePath):
        logger.info(filePath)
        with open(filePath, "a+", newline='') as f:
            writer = csv.writer(f, dialect='excel')
            for item in pajekMap:
                if 'to_group' in item.keys():
                    writer.writerow([item['from_group'], item['from_arti'], item['to_group'], item['to_arti']])
                else:
                    writer.writerow([item['from_group'], item['from_arti'], '', ''])

    # 转换
    def transform(self, pomfile, pajek_path):
        pomschema = self.__read_pom_content(pomfile)
        if pomschema is not None and pomschema.complete:
            logger.info("pomschema=========>{}".format(pomschema.__dict__))
            pajekpairs = self.__transSchema2Pajek(pomschema)
            if pajekpairs is not None:
                for pair in pajekpairs:
                    logger.info("pair==========>{}".format(pair.__str__()))
                self.__savePajek2File(pajekpairs, pajek_path)
