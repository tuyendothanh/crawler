# -*- utf-8 -*- 

from newspaper import Article
url = 'http://vnexpress.net/tin-tuc/thoi-su/ham-luong-sat-hai-bai-tam-o-ha-tinh-vuot-nguong-3401128.html'

a = Article(url, language='vi') # Vietnamese

a.download()
a.parse()
with open('vnexpress.txt', 'w', encoding='utf-8') as f:
    print(a.text, file=f)
	
with open('vnexpress.html', 'w', encoding='utf-8') as f:
    print(a.article_html, file=f)
	
import xml.etree.ElementTree as ET
with open('vnexpress.xml', 'w', encoding='utf-8') as f:
    print(ET.tostring(a.clean_top_node), file=f)
	
from xml.dom import minidom as MD
with open('vnexpress_clean_top_node.xml', 'w', encoding='utf-8') as f:
    rough_string = ET.tostring(a.clean_top_node, 'utf-8')
    reparsed = MD.parseString(rough_string)
    f.write(reparsed.toprettyxml(indent="\t")) 

with open('vnexpress_top_node.xml', 'w', encoding='utf-8') as f:
    rough_string = ET.tostring(a.top_node, 'utf-8')
    reparsed = MD.parseString(rough_string)
    f.write(reparsed.toprettyxml(indent="\t")) 

from lxml import etree	
with open('vnexpress_clean_doc.xml', 'w', encoding='utf-8') as f:
    result = etree.tostring(a.clean_doc, pretty_print=True, method="html")
    print(result, file=f)
	
with open('vnexpress_doc.xml', 'w', encoding='utf-8') as f:
    result = etree.tostring(a.doc, pretty_print=True, method="html")
    print(result, file=f)
