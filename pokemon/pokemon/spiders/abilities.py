import scrapy

class HabilitScrapper(scrapy.Spider):
    name = "diglet"
    domain = "https://pokemondb.net"

    def start_requests(self):
        url = "https://pokemondb.net/ability"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        abilities = response.css('#main > div.grid-row > div:nth-child(2) > div.resp-scroll > table > tbody > tr')
        for abiliti in abilities:
        #abiliti = abilities[0]
            yield {
                'url': self.domain + abiliti.css('td > a::attr(href)').extract_first(),
                'nome': abiliti.css('td > a::text').get(),
                'descricao': abiliti.css('td:nth-child(3)::text').get(),
            }