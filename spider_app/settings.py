BOT_NANE = ['spider_app']


SPIDER_MODULES = ['spider_app.spiders']
NEWSPIDER_MODULE = 'spider_app.spiders'

DOWNLOAD_DELAY = 2
LOG_LEVEL = 'WARNING'

ITEM_PIPELINES = {
    'spider_app.pipelines.MysqlPipeline': 300,
}
