# -*- utf-8 -*-

from newspaper import Article
url = 'http://vnexpress.net/tin-tuc/thoi-su/ham-luong-sat-hai-bai-tam-o-ha-tinh-vuot-nguong-3401128.html'

a = Article(url, language='vi') # Vietnamese

a.download()
a.parse()
with open('classification_data/vnexpress.txt', 'w', encoding='utf-8') as f:
    print(a.text, file=f)

with open('data/vnexpress.html', 'w', encoding='utf-8') as f:
    print(a.article_html, file=f)

import xml.etree.ElementTree as ET
with open('data/vnexpress.xml', 'w', encoding='utf-8') as f:
    print(ET.tostring(a.clean_top_node), file=f)

import ntpath
head, tail = ntpath.split(url)
file_name=tail or ntpath.basename(head)

from xml.dom import minidom as MD
with open('wp_data/' + file_name, 'w', encoding='utf-8') as f:
    rough_string = ET.tostring(a.clean_top_node, 'utf-8')
    reparsed = MD.parseString(rough_string)
    lines = reparsed.toprettyxml(indent="\t").split('\n')
    if len(lines) > 1:
        f.write(a.title + '\n')
        f.write(a.top_img + '\n')
        f.write('<div><p>' + '\n')
        f.write(a.meta_description + '\n')        
        f.write('</p></div>' + '\n')
        f.write('<!--more-->' + '\n')
        #f.write('<html><head><meta charset="utf-8"/></head><body>\n')
        f.write('\n'.join([line for line in lines[1:] if line.strip()]))
        #f.write('</body></html>')

with open('data/vnexpress_clean_top_node.xml', 'w', encoding='utf-8') as f:
    rough_string = ET.tostring(a.clean_top_node, 'utf-8')
    reparsed = MD.parseString(rough_string)
    #print(rough_string.decode('utf-8'))
    f.write(reparsed.toprettyxml(indent="\t"))

with open('data/vnexpress_top_node.xml', 'w', encoding='utf-8') as f:
    rough_string = ET.tostring(a.top_node, 'utf-8')
    reparsed = MD.parseString(rough_string)
    f.write(reparsed.toprettyxml(indent="\t"))
'''
from lxml import etree
with open('data/vnexpress_clean_doc.xml', 'w', encoding='utf-8') as f:
    result = etree.tostring(a.clean_doc, pretty_print=True, method="html")
    print(result, file=f)

with open('data/vnexpress_doc.xml', 'w', encoding='utf-8') as f:
    result = etree.tostring(a.doc, pretty_print=True, method="html")
    print(result, file=f)
'''