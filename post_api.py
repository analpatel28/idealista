import json
import re
import uuid

import requests


def property_type(property_type, title):

    if 'apartment' in property_type.lower():
        Property_Type = 'Apartment'
    elif 'appartment' in property_type.lower():
        Property_Type = 'Apartment'
    elif 'apartament' in property_type.lower():
        Property_Type = 'Apartment'
    elif 'commercial' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'villa' in property_type.lower():
        Property_Type = 'House'
    elif 'moradia' in property_type.lower():
        Property_Type = 'House'
    elif 'warehouse' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'palace' in property_type.lower():
        Property_Type = 'House'
    elif 'flat' in property_type.lower():
        Property_Type = 'Apartment'
    elif 'farm' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'house' in property_type.lower():
        Property_Type = 'House'
    elif 'home' in property_type.lower():
        Property_Type = 'House'
    elif 'duplex' in property_type.lower():
        Property_Type = 'House'

    elif 'land' in property_type.lower():
        Property_Type = 'Land'
    elif 'terrain' in property_type.lower():
        Property_Type = 'Land'
    elif "plot" in property_type.lower():
        Property_Type = 'Land'
    elif "ground" in property_type.lower():
        Property_Type = "Land"
    elif 'terreno' in property_type.lower():
        Property_Type = "Land"

    elif "building" in property_type.lower():
        Property_Type = "Commercial"

    elif 'hotel' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'shop' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'storage' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'industrial' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'restaurant' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'office' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'store' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'business' in property_type.lower():
        Property_Type = 'Commercial'
    else:
        Property_Type = "Other"

    if 'villa' in title.lower():
        if re.match('.*(villa,)', title) or re.match('.*(villa )', title) or re.match('.*(villa\.)', title):
            Property_Type = 'House'
        elif "village" in title.lower():
            if "apartment" in title.lower():
                Property_Type = 'Apartment'
            elif 'apartament' in title.lower():
                Property_Type = 'Aparment'
            elif 'appartment' in title.lower():
                Property_Type = 'Apartment'
            elif 'commercial' in title.lower():
                Property_Type = 'Commercial'
            elif 'warehouse' in title.lower():
                Property_Type = 'Commercial'
            elif 'palace' in title.lower():
                Property_Type = 'House'
            elif 'farm' in title.lower():
                Property_Type = 'Commercial'
            elif 'house' in title.lower():
                Property_Type = 'House'
            elif 'home' in title.lower():
                Property_Type = 'House'
            elif 'duplex' in title.lower():
                Property_Type = 'House'
            elif 'flat' in title.lower():
                Property_Type = 'Apartment'

            elif 'land' in title.lower():
                Property_Type = 'Land'
            elif 'terrain' in title.lower():
                Property_Type = 'Land'
            elif "plot" in title.lower():
                Property_Type = 'Land'
            elif "ground" in title.lower():
                Property_Type = "Land"
            elif 'terreno' in title.lower():
                Property_Type = "Land"

            elif "building" in title.lower():
                Property_Type = "Commercial"

            elif 'hotel' in title.lower():
                Property_Type = 'Commercial'
            elif 'shop' in title.lower():
                Property_Type = 'Commercial'
            elif 'storage' in title.lower():
                Property_Type = 'Commercial'
            elif 'industrial' in title.lower():
                Property_Type = 'Commercial'
            elif 'restaurant' in title.lower():
                Property_Type = 'Commercial'
            elif 'office' in title.lower():
                Property_Type = 'Commercial'
            elif 'store' in title.lower():
                Property_Type = 'Commercial'
            elif 'business' in title.lower():
                Property_Type = 'Commercial'
            else:
                Property_Type = Property_Type
        else:
            Property_Type = "House"
    elif 'moradia' in title.lower():
        Property_Type = 'House'
    elif "apartment" in title.lower():
        Property_Type = 'Apartment'
    elif "appartment" in title.lower():
        Property_Type = 'Apartment'
    elif "apartament" in title.lower():
        Property_Type = 'Apartment'
    elif 'commercial' in title.lower():
        Property_Type = 'Commercial'
    elif 'warehouse' in title.lower():
        Property_Type = 'Commercial'
    elif 'palace' in title.lower():
        Property_Type = 'House'
    elif 'flat' in title.lower():
        Property_Type = 'Apartment'
    elif 'farm' in title.lower():
        Property_Type = 'Commercial'
    elif 'land' in title.lower():
        Property_Type = 'Land'
    elif "plot" in title.lower():
        Property_Type = 'Land'
    elif 'house' in title.lower():
        Property_Type = 'House'
    elif 'home' in title.lower():
        Property_Type = 'House'
    elif 'duplex' in title.lower():
        Property_Type = 'House'


    elif 'terrain' in title.lower():
        Property_Type = 'Land'

    elif "ground" in title.lower():
        Property_Type = "Land"
    elif 'terreno' in title.lower():
        Property_Type = "Land"

    elif "building" in title.lower():
        Property_Type = "Commercial"

    elif 'Negócio' in title.lower():
        Property_Type = "Commercial"
    elif 'hotel' in title.lower():
        Property_Type = 'Commercial'
    elif 'shop' in title.lower():
        Property_Type = 'Commercial'
    elif 'storage' in title.lower():
        Property_Type = 'Commercial'
    elif 'industrial' in title.lower():
        Property_Type = 'Commercial'
    elif 'restaurant' in title.lower():
        Property_Type = 'Commercial'
    elif 'office' in title.lower():
        Property_Type = 'Commercial'
    elif 'store' in title.lower():
        Property_Type = 'Commercial'
    elif 'business' in title.lower():
        Property_Type = 'Commercial'
    else:
        Property_Type = Property_Type
    return Property_Type


def portu_property_type(property_type, title):
    if 'apartamento' in property_type.lower():
        Property_Type = 'Apartment'
    elif 'appartment' in title.lower():
        Property_Type = 'Apartment'
    elif 'apartament' in property_type.lower():
        Property_Type = 'Apartment'
    elif 'Comercial' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'predio' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'moradia' in property_type.lower():
        Property_Type = 'House'
    elif 'terreno' in title.lower() or "terra" in title.lower():
        Property_Type = 'Land'
    elif 'loja' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'Negócio' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'armazem' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'Armazém' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'estacionamento' in title.lower():
        Property_Type = 'Commercial'
    elif 'trespasse' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'terra' in title.lower():
        Property_Type = 'Land'
    elif 'Negócio' in property_type.lower():
        Property_Type = "Commercial"
    elif 'quinta' in title.lower():
        Property_Type = 'Commercial'
    elif 'casa' in title.lower():
        Property_Type = 'House'
    elif 'quarto' in property_type.lower():
        Property_Type = 'Commercial'
    elif 'escritorio' in property_type:
        Property_Type = 'Commercial'
    else:
        Property_Type = 'Other'

    if 'apartament' in title.lower():
        Property_Type = 'Apartment'
    elif 'apartament' in title.lower():
        Property_Type = 'Aparment'
    elif 'appartment' in title.lower():
        Property_Type = 'Apartment'
    elif 'Comercial' in title.lower():
        Property_Type = 'Commercial'
    elif 'predio' in title.lower():
        Property_Type = 'Commercial'
    elif 'moradia' in title.lower():
        Property_Type = 'House'
    elif 'duplex' in title.lower():
        Property_Type = "House"
    elif 'terreno' in title.lower():
        Property_Type = 'Land'
    elif "terra" in title.lower():
        Property_Type = 'Land'
    elif 'loja' in title.lower():
        Property_Type = 'Commercial'
    elif 'armazem' in title.lower():
        Property_Type = 'Commercial'
    elif 'estacionament' in title.lower():
        Property_Type = 'Commercial'
    elif 'trespasse' in title.lower():
        Property_Type = 'Commercial'
    elif 'quinta' in title.lower():
        Property_Type = 'Commercial'
    elif 'casa' in title.lower():
        Property_Type = 'House'
    elif 'quarto' in title.lower():
        Property_Type = 'Commercial'
    elif 'escritorio' in title.lower():
        Property_Type = 'Commercial'
    else:
        Property_Type = Property_Type
    return Property_Type


"""
format for code
Property_Type = post_api.portu_property_type(property_type, title)"""


def Energy_Rating(a):
    if a.lower() == "a_plus" or a.lower() == "a+" or a.lower() == "a +":
        energy_rating = "a+"
    elif a.lower() == "a_minus" or a.lower() == "a-" or a.lower() == "a -":
        energy_rating = "a-"
    elif a.lower() == "a":
        energy_rating = "a"

    elif a.lower() == "b_plus" or a.lower() == "b+" or a.lower() == "b +":
        energy_rating = "b+"
    elif a.lower() == "b_minus" or a.lower() == "b-" or a.lower() == "b -":
        energy_rating = "b-"
    elif a.lower() == "b":
        energy_rating = "b"

    elif a.lower() == "c_plus" or a.lower() == "c+" or a.lower() == "c +":
        energy_rating = "c+"
    elif a.lower() == "c_minus" or a.lower() == "c-" or a.lower() == "c -":
        energy_rating = "c-"
    elif a.lower() == "c":
        energy_rating = "c"

    elif a.lower() == "d_plus" or a.lower() == "d+" or a.lower() == "d +":
        energy_rating = "d+"
    elif a.lower() == "d_minus" or a.lower() == "d-" or a.lower() == "d -":
        energy_rating = "d-"
    elif a.lower() == "d":
        energy_rating = "d"

    elif a.lower() == "e_plus" or a.lower() == "e+" or a.lower() == "e +":
        energy_rating = "e+"
    elif a.lower() == "e_minus" or a.lower() == "e-" or a.lower() == "e -":
        energy_rating = "e-"
    elif a.lower() == "e":
        energy_rating = "e"

    elif a.lower() == "f_plus" or a.lower() == "f+" or a.lower() == "f+":
        energy_rating = "f+"
    elif a.lower() == "f_minus" or a.lower() == "f-" or a.lower() == "f-":
        energy_rating = "f-"
    elif a.lower() == "f":
        energy_rating = "f"

    elif a.lower() == "g_plus" or a.lower() == "g+" or a.lower() == "g +":
        energy_rating = "g+"
    elif a.lower() == "g_minus" or a.lower() == "g-" or a.lower() == "g +":
        energy_rating = "g-"
    elif a.lower() == "g":
        energy_rating = "g"
    else:
        energy_rating = ""

    return energy_rating


def bed_bath_availability(Property_Type, bed, bath):
    if "apartment" in Property_Type.lower() or "house" in Property_Type.lower():
        if str(bed) == "0" and str(bath) == "0":
            return False
    return True


def location(lat, long):
    try:
        a_url = f'http://178.170.40.190:8080/reverse?format=json&lat={lat}&lon={long}'
        resp = requests.get(a_url)
        data_json = json.loads(resp.text)
        loc_data = data_json["address"]

        try:
            village = ""

            for loc in loc_data:
                if loc == 'neighbourhood':
                    village = loc_data[f"{loc}"]
                    break

            if village == "":
                for loc in loc_data:
                    if loc == 'hamlet':
                        village = loc_data[f"{loc}"]
                        break
                    elif loc == 'village':
                        village = loc_data[f"{loc}"]


        except:
            village = ""

        try:
            Locality = ""
            for loc in loc_data:
                if loc == 'city':
                    Locality = loc_data[f"{loc}"]
                    break

            if Locality == "":
                for loc in loc_data:
                    if loc == 'suburb':
                        Locality = loc_data[f"{loc}"]
                        break
                    elif loc == 'town':
                        Locality = loc_data[f"{loc}"]
        except:
            Locality = ""

        try:
            Municipality = ""
            for loc in loc_data:
                if loc == 'municipality':
                    Municipality = loc_data[f"{loc}"]
                    break
                elif loc == 'city_district':
                    Municipality = loc_data[f"{loc}"]

        except:
            Municipality = ""

        try:
            District = ""
            for loc in loc_data:
                if loc == 'county':
                    District = loc_data[f"{loc}"]
                    break
            if District == "":
                for loc in loc_data:
                    if loc == 'archipelago':
                        District = loc_data[f"{loc}"]
                        break
        except:
            District = ""
        return {"village": village, "Locality": Locality, "Municipality": Municipality, "District": District}
    except:
        return False


headers_input = {
    'Authorization': 'Token f213715c14987364042a355d6ebebea97b7792f1',
    'Content-Type': 'application/json'
}


def post(payload):
    if payload['price']:
        if "/AL" in payload["descriptions"] or "/AL" in payload["specifications"]:
            return True
        check_url = f"http://178.170.40.190:4000/propertiescheck?bed={payload['bedrooms']}&bath={payload['bathrooms']}&price={payload['price']}&lat={payload['lat']}&long={payload['lon']}&check_all=True "
        comp_resp = requests.get(check_url, headers=headers_input)
        if comp_resp.json() != [] and payload['site'] != comp_resp.json()[0]['site']:
            # print("inside url: ", payload['url'])
            print("inside url: ", comp_resp.json()[0]['url'])
            competitor_site = comp_resp.json()[0]['competitor_site']
            print(competitor_site)
            if not competitor_site:
                competitor_site = []
            else:
                competitor_site = json.loads(competitor_site)
            check_com = True
            for com in competitor_site:
                if com != '-' or com != []:
                    com = com
                    if 'site' in com and com['site'] == payload['site']:
                        check_com = False
                        break
            if check_com:
                comp_dict = dict()
                comp_dict["url"] = payload['url']
                comp_dict["professional"] = payload['professional']
                comp_dict["contact"] = payload['contact']
                comp_dict["site"] = payload['site']
                comp_dict["price"] = payload['price']
                comp_dict["ref"] = payload['ref']
                competitor_site.append(comp_dict)
                payload_com = comp_resp.json()[0]
                payload_com['competitor_site'] = json.dumps(competitor_site)
                payload_com['is_deleted'] = False
                del payload_com['id']

                comp_append = requests.put(
                    f"http://178.170.40.190:4000/propertiescheck/{comp_resp.json()[0]['id']}/",
                    headers=headers_input, data=json.dumps(payload_com))
                print("comp_append", comp_append.status_code)

        else:
            url_post = "http://178.170.40.190:4000/properties/"

            response = requests.post(url_post, headers=headers_input, data=json.dumps(payload))

            print("property upload", response.status_code)
            if response.status_code != 201:
                print(payload["url"])
                print(response.text)
            if "Ensure this field has no more than 64 characters" in response.text:
                print("lenth of city: ", len(payload["city"]))


def duplicate_by_ref(payload):
    if payload['images'] == ["-"]:
        return False

    duplicate_check_api = f"http://178.170.40.190:4000/propertiescheck?ref={payload['ref']}&professional={payload['professional']}"
    response = requests.request("GET", duplicate_check_api, headers=headers_input)
    if response.json():
        data = response.json()[0]
        if data['bedrooms'] == payload['bedrooms'] and data["bathrooms"] == payload["bathrooms"] and data[
            "lat"] == payload['lat'] and data["lon"] == payload['long'] and data["price"] == payload['price']:
            return False
        else:
            payload["ref"] = uuid.uuid4().hex[:6]
            post(payload)
            return True
    else:
        if payload["price"]:
            post(payload)
            return True


def price_check(price, property_type, sale_type):
    if int(price) <= 5000 and sale_type.lower() == "sale" and (
            property_type == "House" or property_type == "Apartment" or property_type == "Houses" or property_type == "Apartments"):
        return False
    return True


def remove_property(data, headers_to_check):
    if data['sale_or_rent'] not in ['Rent', 'rent']:
        data['is_available'] = False
        if not data["videos"]:
            data["videos"] = ["-"]
        id = data['id']
        del data['id']
        comp_append = requests.put(
            f"http://178.170.40.190:4000/propertiescheck/{id}/",
            headers=headers_to_check, data=json.dumps(data))
        return comp_append.status_code
    else:
        data["is_available_rent"] = False
        if not data["videos"]:
            data["videos"] = ["-"]
        id = data['id']
        del data['id']
        comp_append = requests.put(
            f"http://178.170.40.190:4000/propertiescheck/{id}/",
            headers=headers_to_check, data=json.dumps(data))
        return ("is_avaialable_rent=", comp_append.status_code)
