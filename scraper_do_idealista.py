import json
# import multiprocessing
import re
import time
import uuid

import pymysql
import requests
from bs4 import BeautifulSoup
from lxml import etree, html

import post_api


# from multiprocessing import freeze_support


def normalize_whitespace(string):
    return re.sub(r'(\s)\1{1,}', r'\1', string)


def replace_normalize(name):
    return normalize_whitespace(str(name).replace('\r', ' ')
                                .replace('\n', ' ').replace('\t', ' ').replace('"', '\\"').replace("'", "\\'").strip())


db_host = "localhost"
db_user = "root"
db_password = "1313"
db_name = "idealista"
db_table_name = "idealista_pending_urls"
# db_table_name = "idealista_new_home_url"

connection = pymysql.connect(host=db_host,
                             user=db_user,
                             password=db_password,
                             charset='utf8mb4')
cursor = connection.cursor()


def creat_database():
    try:
        sql = f"create database if not exists {str(db_name)} default charset utf8mb4 collate utf8mb4_general_ci;"
        cursor.execute(sql)
        cursor.execute(f"use {db_name}")
        connection.commit()
    except Exception as e:
        print(e)


def create_table():
    try:
        sql = f"""create table if not exists {str(db_table_name)} (URL varchar(533)Unique, Status VARCHAR(533)) DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;"""
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        print("error in table: ", e)


class Idealista:

    def __init__(self):
        self.typo_to_type = {
            "1": "Home",
            "2": "Home",
            "3": "Home",
            "4": "Garage",
            "5": "Office",
            "6": "Commercial",
            "7": "Room",
            "8": "Land",
            "10": "New Home",
            "12": "Storage Room",
            "13": "Building",
        }
        self.base_url = 'https://www.idealista.pt/en/'
        self.site_name = "idealista.pt"

        self.headers_to_check = {
            'Authorization': 'Token f213715c14987364042a355d6ebebea97b7792f1',
            'Content-Type': 'application/json'
        }

        self.header = {
            "accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / avif, image / webp, "
                      "image / apng, * / *;q = 0.8, application / signed - exchange;v = b3;q = 0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/96.0.4664.110 Safari/537.36 "
        }

    def Update_sql(self, p_url, status='complete'):
        try:
            sql = f"UPDATE {db_name}.{db_table_name} SET Status = '{status}' WHERE URL = '{p_url}'"
            cursor.execute(sql)
            connection.commit()
            print("update property: ", p_url, "With status of: ", status)
        except Exception as e:
            print("sql update error: ", e)
        return True

    # def bulk_update(self, all_url, count):
    #     jobs = []
    #     for url in all_url:
    #         p_url = url[0]
    #         if "empreendimento" in p_url:
    #             continue
    #         sale_type = url[2]
    #         count = count + 1
    #         p = multiprocessing.Process(target=self.get_data,
    #                                     args=(p_url, sale_type, count))
    #         jobs.append(p)
    #         p.start()
    #     print("SLEEP ==================================-")
    #     # time.sleep(4)
    #
    #     # jobs_complete = 0
    #     # number_of_chrome_widows = len(jobs)
    #     # while jobs_complete != number_of_chrome_widows:
    #     #     jobs_alive = []
    #     #     for index, job in enumerate(jobs):
    #     #         if not (job.is_alive()):
    #     #             if (job.exitcode != 0):
    #     #                 number_of_chrome_widows = number_of_chrome_widows - 1
    #     #             else:
    #     #                 jobs_complete += 1
    #     #         else:
    #     #             jobs_alive.append(job)
    #     #     jobs = jobs_alive
    #     TIMEOUT = 50
    #     start = time.time()
    #     while time.time() - start <= TIMEOUT:
    #         if not any(p.is_alive() for p in jobs):
    #             # All the processes are done, break now.
    #             break
    #
    #         time.sleep(.1)  # Just to avoid hogging the CPU
    #     else:
    #         # We only enter this if we didn't 'break' above.
    #         print("timed out, killing all processes")
    #         for p in jobs:
    #             p.terminate()
    #             p.join()
    #
    #     return count

    def get_url(self):
        count = 0
        while True:
            try:
                limit = 10
                offset = 0
                # query = f"SELECT * FROM idealista.idealista_pending_urls where URL LIKE '%empreendimento%' and URL LIKE '%imovel%' and status='pending';"
                query = f"SELECT * FROM {db_name}.{db_table_name} WHERE status = 'pending'"
                cursor.execute(query)
                all_url = cursor.fetchall()
                print('total fetch url = ', len(all_url))
                self.get_data(all_url, count)
                # for url in all_url:
                #     p_url = url[0]
                #     sale_type = url[2]
                #     self.get_data(p_url, sale_type, count)

                # jobs = []
                # count = 0
                # while all_url:
                #     print("===  Enter ++++++++++++++++++++++")
                #     count = self.bulk_update(all_url, count)
                #     offset = offset + limit
                #     query = f"SELECT * FROM {db_name}.{db_table_name} WHERE status = 'pending' limit {limit} offset {offset}"
                #     cursor.execute(query)
                #     all_url = cursor.fetchall()
                #     print("Restart ===================================")
            except Exception as e:
                print("eroorroooroooooooooooooooooooo")
                print(e)
                pass

    def get_data(self, all_url, count):
        a = int(input("a: "))
        b = int(input("b: "))
        for url in all_url[a:b]:
            p_url = url[0]
            sale_type = url[2]
            try:
                if "https://www.idealista.pt" not in p_url:
                    property_url = f'https://www.idealista.pt{p_url}'
                else:
                    property_url = p_url

                # if "empreendimento" in property_url and "imovel" in property_url:
                    # continue
                # else:
                #     continue
                print(str(count) + "================" + property_url)

                api_url = f"http://178.170.40.190:4000/propertiescheck?url={property_url}&site={self.site_name}"
                response = requests.request("GET", api_url, headers=self.headers_to_check)

                if not response.json():
                    try:
                        p_req = requests.get(
                            f'http://api.scrape.do?token=c70858af0cc14fe18d60d8ac91453c7380303d31a13&url={property_url}',
                            headers=self.header)

                    except Exception as e:
                        print(e)
                        continue
                    if p_req.status_code == 404:
                        self.Update_sql(property_url, 'complete')
                        continue
                    retry = 0
                    while p_req.status_code == 500 or p_req.status_code == 403 or p_req.status_code == 429:
                        print("property_url status code: ", p_req.status_code)
                        if retry < 4:
                            time.sleep(20)
                            p_req = requests.get(
                                f'http://api.scrape.do?token=c70858af0cc14fe18d60d8ac91453c7380303d31a13&url={property_url}',
                                headers=self.header)
                            print("retry: ", retry)
                            retry += 1
                        else:
                            self.Update_sql(p_url, 'retried')
                            continue
                    if p_req.status_code == 200:
                        p_res = html.fromstring(p_req.text)
                        soup = BeautifulSoup(p_req.content, "html.parser")
                        print("property reponse: ", p_req.status_code)

                        property_json = re.findall("var utag_data = (.*);", p_req.text)[0]
                        p_js = json.loads(property_json)
                        prop_number = p_js['ad']['typology']
                        property_type = self.typo_to_type[f"{prop_number}"]

                        name = soup.select_one('span.main-info__title-main').text.strip()

                        Property_Type = post_api.property_type(property_type, name)
                        if Property_Type == "Other":
                            Property_Type = post_api.portu_property_type(property_type, name)

                        print(Property_Type)

                        address = soup.select_one('span.main-info__title-minor').text.strip()

                        try:
                            latitude = ''.join(re.findall("latitude: '([-+]?\d*\.\d+|\d+)',", p_req.text))
                            lat = float("{0:.5f}".format(float(latitude)))
                        except:
                            lat = 0
                            self.Update_sql(p_url, status='check')
                            continue

                        try:
                            longitude = ''.join(re.findall("longitude: '([-+]?\d*\.\d+|\d+)',", p_req.text))
                            long = float("{0:.5f}".format(float(longitude)))
                        except:
                            long = 0
                            self.Update_sql(p_url, status='check')
                            continue

                        try:
                            price = int(
                                "".join(p_res.xpath('//strong[@class="price"]/text()')).replace("€/month", "").replace(
                                    "€",
                                    "").replace(
                                    ",", ""))
                        except:
                            price = 0

                        try:
                            if not price:
                                price = int("".join(p_res.xpath(
                                    '//div[@class="info-data"]/span[contains(text(), "Price from")]/span/text()')).replace(
                                    "€", "").replace(",", "").replace("EUR ", "").replace("EUR", "").strip())
                        except:
                            price = 0
                        if not price:
                            self.Update_sql(p_url, status='check')
                            continue

                        price_check = post_api.price_check(price, Property_Type, sale_type)
                        if not price_check:
                            self.Update_sql(p_url, status='complete')
                            continue

                        try:
                            t_num = ",".join(
                                p_res.xpath(
                                    '//div[@class="info-features"]//span[contains(text(),"T")]/text()')).replace(
                                "T",
                                "").strip()
                            beds = int(t_num) if t_num != "" else 0
                        except:
                            beds = '0'

                        try:
                            bath_num = re.search(r'"bathNumber":"(\d+)"', p_req.text)
                            baths = int(bath_num.group(1)) if bath_num is not None else 0
                        except:
                            baths = '0'

                        bed_bath = post_api.bed_bath_availability(Property_Type, beds, baths)
                        if not bed_bath:
                            self.Update_sql(p_url, status='complete')
                            continue

                        try:
                            image = []
                            Image = re.findall(r'imageDataService:"([^,]*),', p_req.text)
                            for im in Image:
                                img = im.replace("WEB_DETAIL", "WEB_DETAIL_TOP-XL-L")
                                if img not in image:
                                    image.append(img)
                            images = image
                        except Exception as e:
                            print(f"error in image: {e}")
                            images = ["-"]
                            self.Update_sql(p_url, status='checked')
                            continue

                        if not images:
                            print(f" Images not found === {property_url}")
                            self.Update_sql(p_url, status='checked')
                            continue

                        number_elm = soup.select_one("p._browserPhone")
                        try:
                            contact = number_elm.text.strip() if number_elm is not None else ""
                        except:
                            contact = "-"

                        if not contact or contact == "-":
                            contact = "-"

                        try:
                            ref = soup.select_one("p.txt-ref").text.strip()
                        except:
                            ref = ""

                        original_reference = ref
                        if not ref or ref == self.site_name:
                            ref = uuid.uuid4().hex[:6]

                        try:
                            professional_elm = soup.select_one("div.professional-name > span")
                            professional = professional_elm.text.strip().encode('utf-8').decode(
                                'unicode-escape') if professional_elm is not None else ""
                        except:
                            professional = "-"

                        if not professional:
                            professional = "-"

                        try:
                            price_per_m_elm = soup.select_one("p.squaredmeterprice > span:nth-child(2)")
                            price_per_m = price_per_m_elm.text.strip() if price_per_m_elm is not None else ""
                            price_per_m = price_per_m.replace("€/m²", "").replace("€", "").replace(",","").strip() if price_per_m != "" else ""
                        except:
                            price_per_m = "0"

                        try:
                            description = etree.tostring(
                                p_res.xpath('//div[@class="adCommentsLanguage expandable is-expandable"]//p')[
                                    0]).decode(
                                "utf-8")
                        except:
                            description = "."

                        try:
                            city_elm = soup.select_one("#headerMap > ul > :last-child").get_text()
                            city = city_elm.strip() if city_elm is not None else ""
                        except:
                            city = address

                        if len(city) >= 64 or len(address) >= 64:
                            city = "-"
                        try:
                            features = []
                            for elm in soup.select('div.details-property-feature-one ul > li'):
                                features.append(elm.text.strip())


                        except:
                            features = ["-"]
                        try:
                            equp = []
                            for eq in soup.select('div.details-property-feature-two ul > li'):
                                equp.append(eq.text.strip())
                            equipments = ", ".join(equp)
                        except:
                            equipments = "-"

                        try:
                            size_built = float(
                                p_res.xpath('//div[@class="info-features"]/span/span/text()')[0].replace(",",
                                                                                                         "").strip())
                        except:
                            size_built = 0

                        try:
                            if not price_per_m:
                                if size_built:
                                    price_per_m = int(price) / float(size_built)

                                else:
                                    price_per_m = 0
                        except:
                            price_per_m = 0

                        price_per_m = float("{0:.2f}".format(float(price_per_m)))
                        try:
                            plot_area = int(
                                "".join(re.findall('Land plot of (.*) m²', " , ".join(features))).replace(",", ""))
                        except:
                            plot_area = '0'

                        try:
                            energy_rating = "".join(
                                p_res.xpath('//*[contains(text(),"Energy efficiency rating: ")]/span/@title'))
                        except:
                            energy_rating = ""

                        Energy_Rating = post_api.Energy_Rating(energy_rating)

                        pool = p_res.xpath(
                            '//div[@class="details-property_features"]/ul/li[contains(text(),"pool")]/text()')
                        if pool:
                            pool = True
                        else:
                            pool = False

                        try:
                            videos = p_res.xpath('//source[@type="video/mp4"][contains(@src, "hd_")]')
                        except:
                            videos = ["-"]

                        if not videos:
                            videos = ["-"]

                        try:
                            ruin = False
                            if "ruin" in description.lower() or "ruin" in " ".join(features):
                                ruin = True
                        except:
                            ruin = False

                        loc = post_api.location(lat, long)
                        if not loc:
                            self.Update_sql(p_url, status='checked')
                            continue

                        if "quinta do lago" in name.lower() or "quinta do lago" in address.lower():
                            loc["village"] = "Quinta do Lago"

                        if "empreendimento" in property_url:
                            new_development = True
                        else:
                            new_development = False

                        payload = {
                            "property_type": Property_Type,
                            "sale_or_rent": sale_type,
                            "url": property_url,
                            "title": name,
                            "address": replace_normalize(address),
                            "city": replace_normalize(city),
                            "lat": lat,
                            "lon": long,
                            "price": 0.0 if price == 'POA ' else float(price),
                            "bedrooms": str(beds),
                            "bathrooms": str(baths),
                            "size_built": float(size_built),
                            "plot_size": float(plot_area),
                            "pool": pool,
                            "new_development": new_development,
                            "site": self.site_name,
                            "energy_rating": Energy_Rating,
                            "parking": True,
                            "other_details": description,
                            "contact": contact,
                            "ref": ref,
                            "original_reference": original_reference,
                            "professional": professional,
                            "price_sqft": price_per_m,
                            "descriptions": description,
                            "equipment": equipments,
                            "specifications": features,
                            "ruin": ruin,
                            "videos": videos,
                            "village": loc['village'],
                            "localities": loc['Locality'],
                            "municipality": loc["Municipality"],
                            "district": loc['District'],
                            "images": images,
                            "compititor_site": []
                        }

                        if price:
                            post_api.duplicate_by_ref(payload)
                            self.Update_sql(p_url)
                            print("count: ", count)

                    # continue
                else:
                    self.Update_sql(p_url)
                    continue
            except Exception as e:
                print(e)
                pass


if __name__ == '__main__':
    # freeze_support()
    Idealista().get_url()
