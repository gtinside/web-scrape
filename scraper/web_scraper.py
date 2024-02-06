import re
import logging
import requests
import xml.etree.ElementTree as ET
from enum import Enum

from log_util import logging_config
from logging.config import dictConfig
dictConfig(logging_config)

logger = logging.getLogger(__name__)

class ScrapeType(Enum):
    EVENTS = "EVENTS"
    PRESENTATIONS = "PRESENTATIONS"

class Scraper:
    def __init__(self, url, type:ScrapeType):
        self.type = type
        self.url = url

    def get_data(self):       
        # Set headers for the request, this is required or the request will be denied
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        
        # Scrape the events from the url
        response = requests.get(self.url, headers=headers)
        
        # Just in case if the request gets denied, raise an error
        response.raise_for_status()
        xmlRoot = ET.fromstring(response.content)
        channel = xmlRoot.find('channel')
        events = []
        
        # Parse the XML, logic for getting the data and title is different for events and presentations
        try:
            for item in channel.findall('item'):
                date, title = None, None
                if self.type == ScrapeType.EVENTS:
                    date, title = item.find('title').text.split(" : ")
                else:
                    date = item.find('pubDate').text
                    title = item.find('title').text
                link = item.find('link').text
                description = None
                url_match = re.search(r'href="(.*?)"', item.find('description').text)
                if url_match:
                    description = url_match.group(1)
                events.append({
                    'date': date,
                    'title': title,
                    'link': link,
                    'description': description
                })
            
            return events
        except Exception as e:
            logger.error(f"Error while parsing the XML: {e} for: {self.type.value}")
            raise e
