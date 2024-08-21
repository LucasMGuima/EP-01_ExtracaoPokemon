import scrapy

class PokemonScrapper(scrapy.Spider):
    name = "drilbur"
    domain = "https://pokemondb.net"

    def start_requests(self):
        url = "https://pokemondb.net/pokedex/all"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pokemons = response.css('#pokedex > tbody > tr')
        pokemon = pokemons[0]
        link = pokemon.css("td.cell-name > a::attr(href)").extract_first()
        yield response.follow(self.domain + link, self.get_data)

    def get_data(self, response):
        yield {
            'pokemon_id': response.css('.vitals-table > tbody > tr:nth-child(1) > td > strong::text').get(),
            'url_page': response.url,
            'pokemon_name': response.css('#main > h1::text').get(),
            'next_evolution': response.css('#main > div.infocard-list-evo > div:nth-child(3) > span.infocard-lg-data.text-muted > a::text').get(),
            'peso': response.css('.vitals-table > tbody > tr:nth-child(5) > td::text').get(),
            'altura': response.css('.vitals-table > tbody > tr:nth-child(4) > td::text').get(),
            'tipo 1': response.css('.vitals-table > tbody > tr:nth-child(2) > td > a:nth-child(1)::text').get(),
            'tipo 2': response.css('.vitals-table > tbody > tr:nth-child(2) > td > a:nth-child(2)::text').get(),
        }