import os

os.chdir("./pokemon")
os.system("scrapy crawl drilbur -o ../dados/file.csv -t csv")