from typing import List, Dict

def filter_non_academic_authors(papers: List[Dict]) -> List[Dict]:
    """Dummy function to simulate filtering of non-academic authors."""
    for paper in papers:
        paper["Non-academic Author(s)"] = "John Doe"
        paper["Company Affiliation(s)"] = "Biotech Inc."
        paper["Corresponding Author Email"] = "john@biotech.com"
    return papers
