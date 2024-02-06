import logging
from web_scraper import Scraper, ScrapeType
from log_util import logging_config
from logging.config import dictConfig
dictConfig(logging_config)

logger = logging.getLogger(__name__)

# get the events from the url
events = Scraper('https://investor.nvidia.com/rss/event.aspx', ScrapeType.EVENTS).get_data()
logger.info("--------NVIDIA UPCOMING EVENTS----------------")
for event in events:
    logger.info(f"Event Title: {event['title']}")
    logger.info(f"Event Description: {event['description']}")
    logger.info(f"Event Date: {event['date']}")
    logger.info(f"Event Link: {event['link']}")
    logger.info("------------------------")

# get the presentations from the url
presentations = Scraper('https://investor.nvidia.com/rss/presentation.aspx', ScrapeType.PRESENTATIONS).get_data()
logger.info("--------NVIDIA UPCOMING PRESENTATIONS----------------")
for presentation in presentations:
    logger.info(f"Presentation Title: {presentation['title']}")
    logger.info(f"Presentation Description: {presentation['description']}")
    logger.info(f"Presentation Date: {presentation['date']}")
    logger.info(f"Presentation Link: {presentation['link']}")
    logger.info("------------------------")