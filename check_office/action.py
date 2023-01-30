import requests
from bs4 import BeautifulSoup

cookies = {
    "JSESSIONID": "98C694D773A986F0B0BE2E45D6ECF76B.accstorefront-86b9bdc79-vbnmf",
    "CSRFToken": "fc370f41-1c8c-4657-ba68-68ec89bcea31",
    "ROUTE": ".accstorefront-86b9bdc79-vbnmf",
    "bm_sz": "18B84339D3D788526BA3961099771D2F~YAAQP4fdWITVFv+FAQAAEbREDBIarJ3KTon9qgJVPf6OmmqcrvIzpO64SeAPv1ClhbNr9bZZ1TYs7b9BuwFYwayLlUvF6mvt0E856iEgiJrkm4lxxQ5Tnk41fWTQbUILOMVd6e7vIdsEgcleu3FyDooTWRFgiqvmLBH93ZCOVUqTAW5S9vk2F/CEIP7JCn3Bl4xJxa4PKSxp47NTgDBk92+CEjNDPPKBsMvTGs/WlmUbE338m1FrEg/jPaMx9oS3AV+96P71lqcYoeBfMmBCRGOrh+k72a5EwWyCgIvxxalrbj/Q3UTVxSnYP4KbYK6Qs1D61FT5IRKM2SIaTPB4TQKpncE+bqvyHUz1+T7k2qFCtf0PyydR6TYTpucmSb0vUTUt5BLBuJuZlQyfdIqx24R9xKo=~3294773~3162947",
    "FH_TEST_PATH": "992b8aff-ae48-4372-b380-270589bb6b30:2aaadc0c-0b9a-4899-b9dd-de8d2cf98d9a",
    "_gcl_au": "1.1.1169842668.1675243074",
    "gtm-session-start": "1675243073180",
    "_gid": "GA1.3.1284001665.1675243074",
    "selectedCurrency": "GBP",
    "_tt_enable_cookie": "1",
    "_ttp": "PqiYxkAdhGKtyZu--83qloKTQzS",
    "ak_bmsc": "8B34DF46886AB5D93833EB1558638E33~000000000000000000000000000000~YAAQP4fdWBDaFv+FAQAAMLpEDBK2w8I1C6zrmoTccQfsnkkdaNaeeny0FiJvkw37wNAbplMRbL9/Zysfh+Re988BepygNpdoqFNHo5SGZ+VcFZ4eXj4HIMXotzMVBl9G+P+9l2QSVAoJJqDSCNCX5NxJigQQ1EUtfNP9evbDgdMI4nYS2XpuySG6ptkL9aoWkKs8rRZ8q3qnUuOet7oV6a+OaPIfNk2NxjjJFlVtG8dy7VeJMORkS5F/51Sjdq61c873k6KlVO8On7jJLmajuvSPMNOTA++rMkEdNleo0LJNHBtQtgKO89QYFPNAtpYGLPocWDjH+i26cMHUshiragxivU9x02LIrlqLt7AhEeUkstBlTVpFGR1EYWMaTasL1A2b+woFKKqIgWCMOQ9QosaYYPaItuOTlBbziBvdygtVAKHg9SBPHR5Oiv+QeSFBIX1d0kuYiz4IrDC37DLMmEyG5te6Bx0RU10Z1cj+BDoqmQiavQR2a/1yXw==",
    "_gat": "1",
    "OptanonAlertBoxClosed": "2023-02-01T09:19:40.978Z",
    "FirstSession": "source%3Ddirect%26medium%3Dnone%26campaign%3Ddirect%26term%3D%26content%3D%26date%3D20230201",
    "OptanonActiveGroups": "%2CC0001%2CC0002%2CC0003%2CC0004%2C",
    "__utma": "128686803.78602084.1675243074.1675243181.1675243181.1",
    "__utmc": "128686803",
    "__utmz": "128686803.1675243181.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
    "__utmt": "1",
    "_cs_c": "0",
    "_dy_csc_ses": "t",
    "_dy_c_exps": "",
    "_fbp": "fb.2.1675243181487.590592300",
    "_dycnst": "dg",
    "_dyid": "-7498492433003827537",
    "_dyjsession": "04d796f2af7aab30656182667df1f850",
    "dy_fs_page": "www.office.co.uk%2Fview%2Fproduct%2Foffice_catalog%2F2%2C20%2F3278515772",
    "_dycst": "dk.l.c.ws.",
    "_dy_geo": "GB.EU.GB_ENG.GB_ENG_London",
    "_dy_df_geo": "United%20Kingdom..London",
    "_dy_toffset": "2",
    "_pin_unauth": "dWlkPU1USTFZMkkyWXpBdE5tVTBOaTAwTkRjM0xUaGhNVEF0T0RabU1qRmpZemMxWW1VeA",
    "_dyid_server": "-7498492433003827537",
    "firstVisitTS": "1675243073964",
    "_dy_c_att_exps": "",
    "__zlcmid": "1EDlZMIEqXK1CAE",
    "bm_sv": "E7D28C51152F2F3E3A4A5EF7D8644C7C~YAAQP4fdWHxMGP+FAQAAls5GDBKYlGVZNwXBgPny0nuzt0vLIhGixIv+bWsQwAaYztPaj5W12lVmRGOvOcyI4waAorCGM0UXjSCqYr1Hk9hTJEoJdxSxbABz/jvmD7XqN9RfThavc9Lu3VUvwVX1/lBBtqZIj1ZrhBUyhNDvUp1I6BQw6eGuz+YD5icVTmOazk6D1Wm+MLGwB232o7vOIEoJ8IpWc0sLiHgZtn9VW2yoreMBbTVav1cuxagEZDT+eyCn~1",
    "ReturningSession": "source%3Ddirect%26medium%3Dnone%26campaign%3Ddirect%26term%3D%26content%3D%26date%3D20230201",
    "BVImplmain_site": "14642",
    "OptanonConsent": "isGpcEnabled=0&datestamp=Wed+Feb+01+2023+09%3A20%3A11+GMT%2B0000+(Greenwich+Mean+Time)&version=6.19.0&isIABGlobal=false&hosts=&consentId=6f8be20c-6eb7-4f54-84e0-72583b171604&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=GB%3BENG&AwaitingReconsent=false",
    "_ga": "GA1.1.78602084.1675243074",
    "_ga_RX8QMPD6V5": "GS1.1.1675243181.1.1.1675243211.30.0.0",
    "_uetsid": "8eea90f0a21111ed97b151294ae30343",
    "_uetvid": "8eead600a21111edb5f6e5d73d976973",
    "_cs_id": "9b47d8e8-8c07-a66c-e781-c000d3d4e139.1675243181.1.1675243211.1675243181.1531393851.1709407181367",
    "_cs_s": "3.0.0.1675245011473",
    "_abck": "F51E5FEF14C9D095DF6ED86CC24F3C9C~-1~YAAQP4fdWLRPGP+FAQAAr9NGDAnBqRexoJG7Me9rz7GOOfK9YXMowDBHjmx0C+oTpcqwhwHEPQcP1Alw2UzQvHzGjTUraIdecHHhf2VBIzbiBIwAdihh6ZpPQOdEeVDaC6KsZflaQ1aJF6nU1PsqEE4mwHOSJQQIH4KU1Fc3WbVj6bjSwupN8DALkKu32GpKNAmX7m1OJyJfVX5gyahzEXXw31saIqxoDhZYBFPNXZNwTmpfmXYMM7b8Bqfjh3A2ugKt1GfnMeEMS59pUkS45wt3aXx6dGENqArOvctKUEs8unF+eG7EvvCzijI9x+NvWdTAPZtiWLC6CoQf8c+XGg7DHT5XDIMWeJfy3vrM+TND2xbRogsEmzxKV83d8F5stzWIBWAOGNXx5xApz6IiOJbiYyWst2iwnDWIahGXnxVJJuR12eLGEe89sOI6D1kJN9SOseCRUplJXU9QwWtA3D4/2vtM3UTPEmkanjPT0BvBbD7nt4y7OvFM~-1~-1~-1",
    "cto_bundle": "gk0ZE19HbkZWcE5haHBvMGNZRHh2amtjUGslMkJGMDJHdVBZTXdXUXlIeEVDTEgySk9JczBKSzBNdmE4bmxXNmJmcm9sNEtpWUZFYkVCOEtIbThZeXJTQUVtckRzTVpiJTJGSmJwcG5zU0lzY1JkJTJGV1ZaMkNYd1U1bzJtUUl1dHNHcmd4QnlZVVZmZEJPM1Jua3lmZjZrMiUyRmV0ZUNDdyUzRCUzRA",
    "BVBRANDID": "5341e9ec-291d-46bb-818b-83086d1b4ee3",
    "BVBRANDSID": "031404a8-6754-4020-9e91-3d26f28957a7",
    "__utmb": "128686803.4.9.1675243212315",
    "_dy_ses_load_seq": "4892%3A1675243212361",
    "_dy_soct": "1004494.1006427.1675243181*1004739.1006845.1675243181*1150352.1431416.1675243192*1000924.1001029.1675243212*1078733.1219716.1675243212",
    "_dyfs": "1675243212559",
    "_dy_lu_ses": "04d796f2af7aab30656182667df1f850%3A1675243212560",
}

headers = {
    "authority": "www.office.co.uk",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-GB,en;q=0.9",
    "cache-control": "max-age=0",
    "dnt": "1",
    "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}


def main():
    url = "https://www.office.co.uk/view/product/office_catalog/2,20/3278515772"
    response = requests.get(url, cookies=cookies, headers=headers)
    response.raise_for_status()
    if (
        '<p class="text-subheading">Something went wrong, please try again later.</p>'
        in response.text
    ):
        print("Blocked")
        return
    page = BeautifulSoup(response.text, "lxml")
    li_list = page.find_all(
        "li",
        class_="product__sizes-option",
        attrs={"data-value": "060", "data-name": "6"},
    )
    if len(li_list) != 1:
        print(response.text)
        assert False
    if li_list[0]["data-stock"] != "SOLD OUT!":
        print("Stock status change")
        print(url)
        assert False


if __name__ == "__main__":
    main()
