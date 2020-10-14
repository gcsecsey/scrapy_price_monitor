from .base_spider import BaseSpider


class CandleShackSpider(BaseSpider):
    name = "candleshack.com"

    def parse(self, response):
        item = response.meta.get('item', {})
        item['url'] = response.url
        item['title'] = response.css("product-title::text").extract_first("").strip()
        item['price'] = float(
            response.css("div.product-meta > table > tbody > tr > td:nth-child(2) > span").re_first("\$(.*)") or 0
        )
        yield item