import unittest
from web_scraper import Scraper, ScrapeType

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.event_scraper = Scraper("https://investor.nvidia.com/rss/event.aspx", ScrapeType.EVENTS)
        self.presentation_scraper = Scraper("https://investor.nvidia.com/rss/presentation.aspx", ScrapeType.PRESENTATIONS)
    
    def test_get_event_data(self):
        events = self.event_scraper.get_data()
        self.assertIsInstance(events, list)
        self.assertGreater(len(events), 0)
        for event in events:
            self.assertIn('date', event)
            self.assertIn('title', event)
            self.assertIn('link', event)
            self.assertIn('description', event)
    
    def test_get_presentation_data(self):
        presentations = self.presentation_scraper.get_data()
        self.assertIsInstance(presentations, list)
        self.assertGreater(len(presentations), 0)
        for presentation in presentations:
            self.assertIn('date', presentation)
            self.assertIn('title', presentation)
            self.assertIn('link', presentation)
            self.assertIn('description', presentation)

if __name__ == '__main__':
    unittest.main()