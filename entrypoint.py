from scrapy.cmdline import execute
execute(['scrapy', 'crawl', 'amazon','-a','keyword=小米','--nolog'])