import requests
from typing import List, Dict

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

def fetch_papers(query: str, max_results: int = 10) -> List[Dict]:
    """Fetches research papers from PubMed based on a query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json",
    }
    response = requests.get(PUBMED_API_URL, params=params)
    response.raise_for_status()
    
    data = response.json()
    paper_ids = data.get("esearchresult", {}).get("idlist", [])
    
    return [{"PubmedID": pid} for pid in paper_ids]
