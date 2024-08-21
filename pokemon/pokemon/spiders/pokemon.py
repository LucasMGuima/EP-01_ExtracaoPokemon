import scrapy

class PokemonScrapper(scrapy.Spider):
    name = "drilbur"
    domain = "https://pokemondb.net"

    def start_requests(self):
        url = "https://pokemondb.net/pokedex/all"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pokemons = response.css('#pokedex > tbody > tr')
        for pokemon in pokemons:
        #pokemon = pokemons[0]
            link = pokemon.css("td.cell-name > a::attr(href)").extract_first()
            yield response.follow(self.domain + link, self.get_data)

    def get_data(self, response):
        yield {
            'pokemon_id': response.css('.vitals-table > tbody > tr:nth-child(1) > td > strong::text').get(),
            'url_page': response.url,
            'pokemon_name': response.css('#main > h1::text').get(),
            'peso': response.css('.vitals-table > tbody > tr:nth-child(5) > td::text').get(),
            'altura': response.css('.vitals-table > tbody > tr:nth-child(4) > td::text').get(),
            'tipo 1': response.css('.vitals-table > tbody > tr:nth-child(2) > td > a:nth-child(1)::text').get(),
            'tipo 2': response.css('.vitals-table > tbody > tr:nth-child(2) > td > a:nth-child(2)::text').get(),
            'abilities': self.get_abilities(response.css('.vitals-table > tbody > tr:nth-child(6)')),
        }

    def get_abilities(self, response) -> str:
        abiliities = response.css('td > .text-muted')
        resp = ""
        for abilitie in abiliities:
            name = abilitie.css('a::text').get()
            resp = resp + name + "|"
        return resp