from bs4 import BeautifulSoup
# from threading import Thread
import urllib.request

# Get url and list view of land parcels
coop_proj_url = "https://policesacco.com/available-projects/"
coop_proj_html = urllib.request.urlopen(coop_proj_url).read()
proj_html_el = BeautifulSoup(coop_proj_html, "lxml")
lands_section = proj_html_el.select(".button.btn-secondary.caps_small.btn_exstra_small")

# Create list containing all the lands detail page
land_urls = []
for url in range(len(lands_section)):
    land_urls.append(lands_section[url]["href"])


# base data structure
# data = {
#     "cooperative": "kenya police sacco",
#     "parcel_1" : {
#         "title" : "",
#         "cost" : ""
#     }
#
# }

# Scrap data from details pages
def scrape(land_url):
    """
    :param land_url:
    :return:
    """
    html = urllib.request.urlopen(land_url).read()
    soup = BeautifulSoup(html, "html.parser")

    title = soup.select(".post-title")
    overview = soup.select(".normal")
    cost = soup.select('.table.table-striped')
    if len(cost) == 0:
        print("TITLE:", title[0].get_text())
        print("COST: ", soup.tbody.find_all('tr')[2].contents[3].get_text())
        pass
    if len(cost) == 1:
        cost = soup.select('.table.table-stripped')
        print("TITLE:", title[0].get_text())
        print(soup.tbody.find_all('tr')[2].contents[3].get_text())


for url in land_urls:
    scrape(url)
