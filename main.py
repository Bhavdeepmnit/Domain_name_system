from analyzer import DomainAnalyzer, save_to_csv

def main():
    print("Domain Name Analysis Tool")
    domain = input("Enter a domain to analyze (e.g., example.com): ").strip()
    
    analyzer = DomainAnalyzer(domain)
    results = analyzer.analyze()
    
    print("\nAnalysis Results:")
    print(f"Domain: {results['domain']}")
    print(f"Available: {'Yes' if results['is_available'] else 'No'}")
    
    if not results['is_available']:
        print(f"Age: {results['age_years']} years")
        print(f"Keywords: {', '.join(results['keywords'])}")
        print(f"Page Title: {results['page_title']}")
        print(f"Similar Domains: {', '.join(results['similar_domains'])}")
    
    save_option = input("\nSave results to CSV? (y/n): ").lower()
    if save_option == 'y':
        filename = f"{domain.replace('.', '_')}_analysis.csv"
        save_to_csv(results, filename)
        print(f"Results saved to {filename}")

if __name__ == "__main__":
    main()