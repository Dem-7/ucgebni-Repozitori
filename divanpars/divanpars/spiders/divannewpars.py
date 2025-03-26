import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/rostov-na-donu/category/svet"]

    def parse(self, response):
        svet = response.css("div.LlPhw")
        for a in svet:
            yield {"название": a.css("a.ui-GPFV8.qUioe.ProductName.ActiveProduct span::text").get(),
                   "цена": a.css("div.Dms7X.bluLL.Zpdfx span::text").get(),
                   "url": a.css("a").attrib["href"] }
