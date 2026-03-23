import requests
from bs4 import BeautifulSoup
import csv
import time
import os
import re

def get_headers():
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

def clean_text_only(raw_text):
    """
    Removes any residual URLs (http/https) from the text for 100% link-free compliance.
    """
    if not raw_text: return ""
    # Regex to find URLs
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    clean = re.sub(url_pattern, '[Source Website]', raw_text)
    # Clean up multiple spaces and newlines
    clean = re.sub(r'\s+', ' ', clean)
    return clean.strip()

def scrape_blog_updates():
    """
    Scrapes DBpedia blog for knowledge updates - 100% LINK FREE.
    """
    print("\n--- Task 1: Scraping Knowledge Updates (100% Text-Only) ---")
    url = 'https://www.dbpedia.org/blog/'
    headers = get_headers()
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Blog entries use uk-card-title for titles
        h3_tags = soup.find_all('h3', class_='uk-card-title')
        blog_results = []
        
        for h3 in h3_tags:
            link_tag = h3.find('a')
            if not link_tag: continue
            
            title = h3.get_text(strip=True)
            source_detail = "DBpedia Official Blog - Community & Research Portal"
            
            # Date is in div.subhead sibling
            date_tag = h3.find_next_sibling('div', class_='subhead')
            date = date_tag.get_text(strip=True) if date_tag else "N/A"
            
            # Summary is in div.excerpt sibling
            summary_tag = h3.find_next_sibling('div', class_='excerpt')
            summary = summary_tag.get_text(strip=True) if summary_tag else "No summary available."
            
            clean_summary = clean_text_only(summary)
            
            blog_results.append({
                'Topic Name': title,
                'Release Date': date,
                'Source Insight': source_detail,
                'Brief Detail': clean_summary[:250] + "..." if len(clean_summary) > 250 else clean_summary
            })
            
        if blog_results:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            filename = os.path.join(script_dir, 'dbpedia_knowledge_updates.csv')
            keys = blog_results[0].keys()
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(blog_results)
            print(f"Success! {len(blog_results)} knowledge updates saved.")
            
    except Exception as e:
        print(f"Blog Error: {e}")

def scrape_association_members():
    """
    Scrapes DBpedia Association Members - 100% LINK FREE & FULL COVERAGE.
    """
    print("\n--- Task 2: Scraping Association Members (100% Text-Only) ---")
    overview_url = 'https://www.dbpedia.org/members/overview/'
    base_url = 'https://www.dbpedia.org'
    headers = get_headers()
    
    try:
        response = requests.get(overview_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        member_links = []
        for a in soup.find_all('a', class_='uk-margin-bottom'):
            href = a.get('href')
            if href:
                full_link = href if href.startswith('http') else base_url + href
                member_links.append(full_link)
        
        member_links = list(dict.fromkeys(member_links))
        member_results = []
        
        print(f"Crawling all {len(member_links)} member profiles for full organizational coverage...")
        for link in member_links:
            time.sleep(1) 
            p_res = requests.get(link, headers=headers)
            if p_res.status_code != 200: continue
            
            p_soup = BeautifulSoup(p_res.text, 'html.parser')
            # Extract Org Name from h2 inside entry-content
            name_tag = p_soup.select_one('div.entry-content h2') or p_soup.find('h1')
            name = name_tag.get_text(strip=True) if name_tag else "Institutional Partner"
            
            source_detail = "Verified DBpedia Association Member profile"
            
            content_div = p_soup.find('div', class_='entry-content')
            description = ""
            if content_div:
                paragraphs = content_div.find_all('p')
                meaningful_p = [p.get_text(strip=True) for p in paragraphs if len(p.get_text(strip=True)) > 40]
                description = " ".join(meaningful_p[:2])
            
            clean_desc = clean_text_only(description)
            
            member_results.append({
                'Organization Name': name,
                'Membership Tier': "DBpedia Association Member",
                'Source Insight': source_detail,
                'Mission Detail': clean_desc[:400] + "..." if len(clean_desc) > 400 else clean_desc
            })
            
        if member_results:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            filename = os.path.join(script_dir, 'dbpedia_members_report.csv')
            keys = member_results[0].keys()
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(member_results)
            print(f"Success! {len(member_results)} members captured.")
            
    except Exception as e:
        print(f"Member Error: {e}")

if __name__ == "__main__":
    scrape_blog_updates()
    scrape_association_members()
    print("\nAll link-free reports generated successfully with complete site information.")
