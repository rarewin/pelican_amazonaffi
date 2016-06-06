from pelican import signals

import re
import logging

logging.Logger(__name__)

def content_object_init(instance):

    settings = instance.settings

    if instance._content is not None:

        content = instance._content

        # [amazonaffi:affiliate-id|link-name]
        instance._content = re.sub(r'\[amazonaffi:(.+)\|(.+?)\]',
                                   r'<a href="http://www.amazon.co.jp/dp/\1/?tag=%s">\2</a>' % (settings.get("AMAZON_AFFILIATE_ID")),
                                   content)

        # [amazonaffi:affiliate-id]


        return instance

def register():
    signals.content_object_init.connect(content_object_init)
