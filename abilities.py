import os

os.chdir("./pokemon")
os.system("scrapy crawl diglet -o ../dados/abilities.csv -t csv")