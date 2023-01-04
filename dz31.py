import codecs


def delete_html_tags(html_file, result='cleaned.txt'):
    lst_1 = []

    html = codecs.open(html_file, 'r', 'utf-8').read()

    for i in html:
        lst_1.append(i)

    while lst_1.count('<'):
        if '<' or '>' in lst_1:
            a = lst_1.index('<')
            b = lst_1.index('>')
            del lst_1[a:b + 1]

    html = codecs.open('cleaned.txt', 'w', 'utf-8')

    for x in lst_1:
        html.write(x)

    html.close()
    return result


delete_html_tags("draft.html")
