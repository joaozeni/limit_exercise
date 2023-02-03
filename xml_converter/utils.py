def parse_element(element):
    result = []
    
    for sub_element in element:
        data = {}
        data[sub_element.tag] = sub_element.text
        if list(sub_element):
            data[sub_element.tag] = parse_element(sub_element)
        result.append(data)
    
    return result