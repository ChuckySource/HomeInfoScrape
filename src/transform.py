import regex
from lxml import etree

def read_htmltable(s: str) -> list:
    table = etree.HTML(s).find("body/table")
    rows = iter(table)
    headers = [col.text for col in next(rows)]
    out = []
    for row in rows:
        values = [col.text for col in row]
        out.append(dict(zip(headers, values)))
    return out

def read_html(file: str) -> dict:
    with open(file, 'r') as f:
        raw_text = f.read()
    segments = raw_text.split("<h3>")
    out = {}
    for segment in segments:
        if not (name := regex.findall("(?<=<a name='f_..'>..</a> . ).+(?=</h3>)", segment)):
            continue
        table_list = regex.findall("<table.+?</table>", segment, flags=regex.DOTALL)
        out[name[0]] = read_htmltable(table_list[0]), read_htmltable(table_list[1])
    return out

if __name__ == "__main__":
    from pprint import pprint
    pprint(read_html("test/getdata.html"))
