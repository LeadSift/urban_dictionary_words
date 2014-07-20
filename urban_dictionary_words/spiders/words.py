# -*- coding: utf-8 -*-
import re
import string
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import UrbanDictionaryWordsItem


class WordsSpider(scrapy.Spider):
    name = "words"
    allowed_domains = ["www.urbandictionary.com"]
    start_urls = [
        'http://www.urbandictionary.com/browse.php?word=%s%s' % (a, b)
        for a in string.ascii_lowercase
        for b in string.ascii_lowercase
    ]
    _link_extractor = LinkExtractor(allow=re.compile(r'\bterm='))

    def parse(self, response):
        for link in self._link_extractor.extract_links(response):
            yield UrbanDictionaryWordsItem(term=link.text, url=link.url)
