import argparse
from papers_fetcher.fetch_papers import fetch_papers
from papers_fetcher.filter_authors import filter_non_academic_authors
from papers_fetcher.save_results import save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename", default=None)
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    if args.debug:
        print(f"Fetching papers for query: {args.query}")

    papers = fetch_papers(args.query)
    papers = filter_non_academic_authors(papers)

    if args.file:
        save_to_csv(papers, args.file)
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()
