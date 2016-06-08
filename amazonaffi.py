from pelican import signals

import re

regexs = [re.compile(x, re.I | re.S) for x in [r'(<pre>.*?</pre>)', r'(<code>.*?</code>)']]

def data_splitter(reg, s_list):

    ret = []

    for s in s_list:
        ret += reg.split(s)

    return ret

def parser_for_amazonaffi(article_generator):

    for a in article_generator.articles:

        settings = article_generator.settings
        c_list = [a._content]

        for r in regexs:
            c_list = data_splitter(r, c_list)

        for i, c in enumerate(c_list):
            for r in regexs:
                if r.search(c):
                    break
                else:
                    c_list[i] = re.sub(r'\[amazonaffi:(.+)\|(.+?)\]',
                                       r'<a href="http://www.amazon.co.jp/dp/\1/?tag=%s">\2</a>' % (settings.get("AMAZON_AFFILIATE_ID")),
                                       c)
        # [amazonaffi:affiliate-id|link-name]
        a._content = "".join(c_list)

def register():
    signals.article_generator_finalized.connect(parser_for_amazonaffi)
