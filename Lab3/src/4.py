# The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters. Build and return a string that represents the corresponding XML element. Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ") returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"


def build_xml_element(tag, content, **kwargs):
    result = "<" + tag + " "
    for key in kwargs:
        result = result + key + '="' + kwargs[key] + '" '
    result = result + ">" + content + "</" + tag + ">"
    return result


if __name__ == '__main__':
    print(build_xml_element("a", "Hello there", href_=" http://python.org ", _class=" my-link "))
