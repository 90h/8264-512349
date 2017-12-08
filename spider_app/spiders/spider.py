from scrapy import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from spider_app.items import PostItem


class TheSpider(Spider):
    name = 'spider'

    start_urls = [
        'http://bbs.8264.com/thread-512349-1-1.html'
    ]

    def start_requests(self):
        for url in self.start_urls:
            self.logger.warning(u'\n\n' + u'Start >>> :' + url + u'\n')
            yield Request(url=url, callback=self.parse, headers={'Referer': url})

    def parse(self, response):
        selector = Selector(response)

        items = selector.xpath('body/div[@id="wp"]/div[@id="postlist"]/div[@class="lxch_new clboth"]')
        for item in items:
            post = PostItem()

            space_url = item.xpath('div/div[@class="lxch_l"]/a/@href').extract_first()
            screen_name = item.xpath('div/div[@class="lxch_l"]/a/text()').extract_first()
            avatar = item.xpath('div/div[@class="lxch_l"]/div[@class="t_img_new"]/a/img/@src').extract_first()

            reply_view_url = item.xpath('div/div[@class="lxch_l"]/a[@class="info_new alink"]/@href').extract_first()
            reply_count = item.xpath('div/div[@class="lxch_l"]/'
                                     'a[@class="info_new alink"]/text()').extract_first().split(' ')[0][3:]
            online_count = item.xpath('div/div[@class="lxch_l"]/span[@class="info_new"]/text()')[0].extract()[3:]
            registered_at = item.xpath('div/div[@class="lxch_l"]/span[@class="info_new"]/text()')[1].extract()[3:]

            created_at = item.xpath('div/div[@class="lxch_r"]/div[@class="lc_bs_new clboth"]/'
                                    'span[@class="fby"]/text()').extract()[1].split('\n')[2]
            floor = item.xpath('div/div[@class="lxch_r"]/div[@class="lc_bs_new clboth"]/'
                               'a[@class="lc_bs_no"]/em/text()').extract_first()
            content = item.xpath('div/div[@class="lxch_r"]/div[@class="bjcon_new"]/'
                                 'div[@class="t_fsz_new "]/table').extract_first()

            post['floor'] = int(floor)
            post['content'] = content
            post['created_at'] = created_at + ':00'

            post['screen_name'] = screen_name
            post['avatar'] = avatar
            post['space'] = space_url
            post['reply_view'] = reply_view_url
            post['reply_count'] = int(reply_count)
            post['online_count'] = online_count
            post['registered_at'] = registered_at

            yield post

        next_page = selector.xpath(
            'body/div[@id="wp"]/div[@class="layout fenyebbscon"]'
            '/div[@class="pg"]/a[@class="nxt"]/@href'
        ).extract_first()
        if next_page:
            self.logger.warning(u'\n\n' + u'Start >>> :' + next_page + u'\n')
            yield Request(url=next_page, callback=self.parse, headers={'Referer': response.url})
        else:
            self.logger.warning(u'\n\n' + u'Done' + u'\n')
