import scrapy
from scrapy import signals
import subprocess, os, random
from loguru import logger

class ApodbotSpider(scrapy.Spider):
    name = 'apodBot'
    allowed_domains = ['apod.nasa.gov']
    start_urls = ['https://apod.nasa.gov/apod/astropix.html']
    base_url_img = 'https://'+ allowed_domains[0] + '/apod/'
    img_path = '/home/thiago/Projetos/apod/apodScrapy/apodProject/img/'

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(ApodbotSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        self.set_image_background()

    def parse(self, response):
        link_image = response.css('a ::attr(href)').getall()[1]
        self.base_url_img += link_image
        yield scrapy.Request(
            url= self.base_url_img,
            callback=self.parse_image
            )

    def parse_image(self, response):
        subprocess.call(f'wget -P {self.img_path} {response.url}', shell=True)

    def set_image_background(self):
        img = self.select_image_background()
        logger.debug(img)
        subprocess.call(f'gsettings set org.gnome.desktop.background picture-uri file:///{self.img_path}{img}', shell=True)

    def select_image_background(self):
        img_list =  os.listdir(f'{self.img_path}')
        return random.choice(img_list)