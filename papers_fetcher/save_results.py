import csv
from typing import List, Dict

def save_to_csv(papers: List[Dict], filename: str):
    """Saves the research papers list to a CSV file."""
    fieldnames = ["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"]
    
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(papers)
    
    print(f"Saved results to {filename}")
