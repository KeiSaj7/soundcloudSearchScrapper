import requests
from bs4 import BeautifulSoup

def fetch_soundcloud_links(search_url):
    try:
        response = requests.get(search_url)
        response.raise_for_status() 

        soup = BeautifulSoup(response.text, 'html.parser')

        links = []
        for h2_tag in soup.find_all('h2'):
            a_tag = h2_tag.find('a')
            if a_tag and 'href' in a_tag.attrs:
                links.append(f"https://soundcloud.com{a_tag['href']}")

        return links

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the links: {e}")
        return []

if __name__ == "__main__":
    query = input("Enter your search query: ").strip()
    search_url = f"https://soundcloud.com/search/sounds?q={query}"
    soundcloud_links = fetch_soundcloud_links(search_url)

    if soundcloud_links:
        print("Fetched SoundCloud links:")
        for link in soundcloud_links:
            print(link)
    else:
        print("No links found.")