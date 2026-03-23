# DBpedia Data Scraping Project - Viva Preparation Guide

This document will help you explain each slide during your presentation and prepare you for any counter-questions (cross-questions) the evaluator might ask.

---

## 🟢 Slide 1: Title Slide
**What to say:** 
"Good morning/afternoon. Today I'll be presenting my project on extracting organizational intelligence from DBpedia using automated, ethical web scraping."

**Counter-Questions:**
> **Q:** What exactly is DBpedia?
> **A:** DBpedia is a community-driven project that extracts structured data from Wikipedia and makes it available on the web. It's basically the database version of Wikipedia.

---

## 🟢 Slide 2: Project Objectives
**What to say:**
"Our main goal was to gather actionable business intelligence from DBpedia. Specifically, we focused on two areas: 
1. The **latest knowledge updates** published on their blog.
2. The **complete list of organizations** that make up the DBpedia Association.
We needed to extract this data cleanly into a CSV format without capturing any URLs, making it 100% text-based."

**Counter-Questions:**
> **Q:** Why did you choose only the Blog and Members sections?
> **A:** I chose these two sections because they answer the "what" and "who" questions of business intelligence. The blog shows *what* DBpedia is actively researching, and the members section shows *who* is supporting them. Other sections of the site represent technical tools rather than informational content.

---

## 🟢 Slide 3: Web Scraping Architecture
**What to say:**
"To achieve this, I built a custom Python scraper using `requests` for fetching web pages and `BeautifulSoup` for parsing the HTML. The architecture involved a two-phase crawl for the members section—first gathering all the profile links from the overview page, and then systematically visiting each individual profile to extract the organization's name and mission details."

**Counter-Questions:**
> **Q:** Did you consider using Scrapy or Selenium instead of BeautifulSoup?
> **A:** Yes, but DBpedia's pages are static HTML. BeautifulSoup with `requests` is much faster and simpler for static content. Selenium wasn't needed because there was no JavaScript rendering required, and Scrapy would have been over-engineering for a focused, two-section scrape.

> **Q:** How did you make sure the output was 100% link-free?
> **A:** I wrote a custom Python function (`clean_text_only`) that uses regular expressions (regex). Before saving any text to the CSV, the regex scans the string, finds any URLs starting with http or https, and physically replaces them with the text `[Source Website]`.

---

## 🟢 Slide 4: Ethical & Responsible Scraping
**What to say:**
"A major focus of this project was adhering to ethical web scraping standards. DBpedia is a shared community resource, so it was important not to abuse their servers. I implemented a mandatory 1-second delay between all requests, identified my traffic using a proper 'User-Agent' header, and strictly limited the scraping to publicly available pages for internal research purposes."

**Counter-Questions:**
> **Q:** You mentioned a delay. What happens if you don't put `time.sleep` in your code?
> **A:** Without a delay, a Python script can send hundreds of requests per second. This is known as a Denial of Service (DoS) attack. It overloads the server, slows the website down for real users, and often results in our IP address getting permanently blocked or blacklisted by the server's firewall.

> **Q:** Does the `robots.txt` file matter here?
> **A:** Yes, `robots.txt` matters. DBpedia allows ethical scraping of these public informational directories as long as crawlers don't behave aggressively, which is exactly why the rate-limiting (delays) and User-Agent headers were implemented.

---

## 🟢 Slide 5: Uncovering Organizational Assets
**What to say:**
"Here is a snapshot of the final output. The scraper successfully crawled 25 member profiles. The script intelligently filtered out navigation noise and only captured the core organizational mission. You can see how raw web pages were transformed into an organized, structured CSV report, ready for analysis."

**Counter-Questions:**
> **Q:** Why does the CSV only have 25 rows? Did your scraper fail to get the rest?
> **A:** No, the scraper did not fail. It successfully crawled 100% of the member profiles listed on the DBpedia members overview page. There are exactly 25 organizations in the DBpedia Association directory at this time.

> **Q:** Why are some descriptions cut off with "..."?
> **A:** I deliberately capped the mission descriptions at 400 characters inside the Python code. This was to keep the CSV clean, concise, and easy to read in a spreadsheet, preventing giant blocks of text from breaking the formatting.

---

## 🟢 Slide 6: Summary & Impact
**What to say:**
"In conclusion, this project demonstrated how web scraping can efficiently bridge the gap between unstructured web data and structured business intelligence. By adhering to link-free sanitization and ethical crawling practices, we created a repeatable asset that tracks DBpedia's organizational growth and community updates without any manual data entry."

**Counter-Questions:**
> **Q:** If the website structure changes tomorrow, will your script still work?
> **A:** If DBpedia completely redesigns their HTML class names (like changing `uk-card-title`), the script will break and return empty data. That is the nature of web scraping—it relies on the current DOM structure. To fix it, we would just inspect the new website and update the CSS selectors in the Python code.

---

## 🟢 Slide 7: Thank You
**What to say:**
"Thank you for your time. I am now open to any questions."

---

## 💡 Quick Tips for the Viva:
1. **Be Honest:** If they point out a flaw, say "That's a great point, in a production environment we would definitely implement that."
2. **Know Your Tech Stack:** `Python`, `requests` (for fetching), `BeautifulSoup` (for parsing HTML), `csv` (for saving), `re` (Regex, for removing links), `time` (for ethical delays).
3. **Stand By Your Design:** Data capping (400 chars) and targeted scraping (2 sections) were intentional design choices for quality, not limitations of your coding ability.

Good luck! You've got this.
