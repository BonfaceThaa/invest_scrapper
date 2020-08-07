from bs4 import BeautifulSoup
import urllib.request
import json

# Get url and list view of land parcels
coop = "Kenya Police sacco"
coop_proj_url = "https://policesacco.com/available-projects/"

coop_proj_html = urllib.request.urlopen(coop_proj_url).read()
proj_html_el = BeautifulSoup(coop_proj_html, "lxml")
lands_section = proj_html_el.select(".button.btn-secondary.caps_small.btn_exstra_small")

# Create list containing all the lands detail page
land_urls = []
for url in range(len(lands_section)):
    land_urls.append(lands_section[url]["href"])

# Data structure for all the scrapped data
data = {
    "cooperative": coop,
    "parcels": []
}

# Data structure for a particular parcel for the scrapped data
land_info = {}


# Scrap data from details pages
def scrape(land_url):
    """
    :param land_url:
    :return:
    """
    html = urllib.request.urlopen(land_url).read()
    soup = BeautifulSoup(html, "html.parser")

    title = soup.select(".post-title")
    cost = soup.select('.table.table-striped')

    def get_data():
        """
        function to add the title and price of a land parcel to the land_info data structure
        :return:
        """
        land_info["title"] = title[0].get_text()
        land_info["price"] = soup.tbody.find_all('tr')[2].contents[3].get_text()

    if len(cost) == 0:
        get_data()

    if len(cost) == 1:
        cost = soup.select('.table.table-stripped')
        get_data()

    return land_info


for url in land_urls:
    scrape(url)
    data["parcels"].append(dict(land_info))

with open("data/data.json", "w") as data_file:
    json.dump(data, data_file)
