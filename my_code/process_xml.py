from xml.etree import ElementTree
import collections
import os

Course = collections.namedtuple('Course', 'title room building')


def main():
    folder = os.path.dirname(__file__)
    file = os.path.join(folder, 'xml_data', 'reed.xml')

    with open(file) as fin:
        xml_text = fin.read()

    dom = ElementTree.fromstring(xml_text)

    course_nodes = dom.findall('course')

    courses =[]
    for n in course_nodes:
        c = Course(
            n.find('title').text,
            n.find('place/room').text,
            n.find('place/building').text

        )
        courses.append(c)

    print(courses)

if __name__ == '__main__':
    main()
