# Ethical Web Scraping: DBpedia Standards

When interacting with DBpedia and Linked Open Data resources, we adhere to these professional standards:

### 1. Identifying the Agent
We use custom `User-Agent` headers in our scripts so web administrators know who is accessing their site.

### 2. Honoring the Commons
DBpedia is a community resource. We avoid aggressive scraping that could drain their resources, ensuring the site remains responsive for all users worldwide.

### 3. Request Throttling
A mandatory 2-second delay is built into our scripts. This prevents "scraping bursts" that can trigger firewall blocks or server strain.

### 4. Data Usage
The scraped content is intended for internal business intelligence research and trend analysis, respecting all creative commons and open-source licenses provided by DBpedia.
