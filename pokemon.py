import os

os.chdir("./pokemon")
os.system("scrapy crawl drilbur -o ../dados/pokemons.csv -t csv")