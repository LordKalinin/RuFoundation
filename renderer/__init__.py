from .parser import Parser
from .tokenizer import StaticTokenizer
import time
import json
import logging


def single_pass_render(source, context=None):
    t = time.time()
    p = Parser(StaticTokenizer(source))
    result = p.parse()
    debug = False
    parsing_time = time.time()-t
    t = time.time()
    s = result.root.render(context)
    rendering_time = time.time()-t
    if context is not None and context.source_article == context.article:
        logging.info('parsing took %.3fs, rendering took %.3fs (%s)' % (parsing_time, rendering_time, context.source_article.full_name if hasattr(context.source_article, "full_name") else ""))
        if debug:
            logging.info('rendering tree\n%s' % json.dumps(result.root.to_json()))

    return s
