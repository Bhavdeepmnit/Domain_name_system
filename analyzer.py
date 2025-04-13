import whois
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pandas as pd
from datetime import datetime

class DomainAnalyzer:
    def __init__(self, domain):
        self.domain = domain
        self.results = {
            'domain': domain,
            'is_available': None,
            'age_years': None,
            'keywords': [],
            'similar_domains': [],
            'page_title': None
        }
    
    def check_availability(self):
        try:
            w = whois.whois(self.domain)
            self.results['is_available'] = False
            if isinstance(w.creation_date, list):
                creation_date = w.creation_date[0]
            else:
                creation_date = w.creation_date
            self.results['age_years'] = (datetime.now() - creation_date).days // 365
        except:
            self.results['is_available'] = True
    
    def extract_keywords(self):
        # Simple keyword extraction from domain name
        keywords = self.domain.split('.')[0].replace('-', ' ').split()
        self.results['keywords'] = keywords
    
    def find_similar_domains(self):
        # This would be more robust in a real implementation
        base = self.domain.split('.')[0]
        self.results['similar_domains'] = [
            f"{base}app.com",
            f"{base}tech.com",
            f"{base}online.com"
        ]
    
    def get_page_title(self):
        try:
            url = f"http://{self.domain}"
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            self.results['page_title'] = soup.title.string if soup.title else None
        except:
            self.results['page_title'] = None
    
    def analyze(self):
        self.check_availability()
        if not self.results['is_available']:
            self.extract_keywords()
            self.find_similar_domains()
            self.get_page_title()
        return self.results

def save_to_csv(results, filename):
    df = pd.DataFrame([results])
    df.to_csv(filename, index=False)