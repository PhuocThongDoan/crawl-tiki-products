# from bs4 import BeautifulSoup
# import requests
# import json
# import csv

# laptop_page_url = 'https://tiki.vn/bach-hoa-online/c4384?page=2&amp'
# product_url = "https://tiki.vn/api/v2/products/{}"

# product_id_file = "./data/product-id.txt"
# product_data_file = "./data/product.txt"
# product_file = "./data/product.csv"

# def get_data_id(string_product_item):  
#   word = str(string_product_item)
#   result = word.find(".html?") 
#   data_id = ''
#   i = 1
#   while(1):
#     if (word[result-i]) != 'p':
#       data_id = data_id + word[result-i]
#       i += 1
#     else:
#       data_id = data_id[::-1]
#       break
#   return data_id

# def crawl_product_id():
#     product_list = []
#     i = 2
#     while (i==2):
#         print("Crawl page: ", i)
#         headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.344"}
#         response = requests.get(laptop_page_url, headers = headers)
#         parser = BeautifulSoup(response.text, 'html.parser')

#         product_box = parser.findAll(class_="product-item")

#         if (len(product_box) == 0):
#             break

#         for product in product_box:
#             product_list.append(get_data_id(product))

#         i += 1

#     return product_list, i

# def save_product_id(product_list=[]):
#     file = open(product_id_file, "w+")
#     str = "\n".join(product_list)
#     file.write(str)
#     file.close()
#     print("Save file: ", product_id_file)

# def crawl_product(product_list=[]):
#     product_detail_list = []
#     for product_id in product_list:
#         response = requests.get(product_url.format(product_id))
#         if (response.status_code == 200):
#             product_detail_list.append(response.text)
#             print("Crawl product: ", product_id, ": ", response.status_code)
#     return product_detail_list

# flatten_field = [ "badges", "inventory", "categories", "rating_summary", 
#                       "brand", "seller_specifications", "current_seller", "other_sellers", 
#                       "configurable_options",  "configurable_products", "specifications", "product_links",
#                       "services_and_promotions", "promotions", "stock_item", "installment_info" ]

# def adjust_product(product):
#     e = json.loads(product)
#     if not e.get("id", False):
#         return None

#     for field in flatten_field:
#         if field in e:
#             e[field] = json.dumps(e[field], ensure_ascii=False)

#     return e

# def save_raw_product(product_detail_list=[]):
#     file = open(product_data_file, "w+")
#     str = "\n".join(product_detail_list)
#     file.write(str)
#     file.close()
#     print("Save file: ", product_data_file)

# def load_raw_product():
#     file = open(product_data_file, "r")
#     return file.readlines()

# def save_product_list(product_json_list):
#     file = open(product_file, "w")
#     csv_writer = csv.writer(file)

#     count = 0
#     for p in product_json_list:
#         if p is not None:
#             if count == 0:
#                 header = p.keys() 
#                 csv_writer.writerow(header) 
#                 count += 1
#             csv_writer.writerow(p.values())
#     file.close()
#     print("Save file: ", product_file)


# # crawl product id
# product_list, page = crawl_product_id()

# print("No. Page: ", page)
# print("No. Product ID: ", len(product_list))

# # save product id for backup
# # save_product_id(product_list)

# # # crawl detail for each product id
# # product_list = crawl_product(product_list)

# # # save product detail for backup
# # save_raw_product(product_list)

# # # product_list = load_raw_product()
# # # flatten detail before converting to csv
# # product_json_list = [adjust_product(p) for p in product_list]
# # # save product to csv
# # save_product_list(product_json_list)

from bs4 import BeautifulSoup
import requests
import json
import csv

laptop_page_url = "https://tiki.vn/laptop/c8095?src=c.8095.hamburger_menu_fly_out_banner&_lc=&page={}"
product_url = "https://tiki.vn/api/v2/products/{}"

product_id_file = "./data/product-id.txt"
product_data_file = "./data/product.txt"
product_file = "./data/product.csv"

def get_data_id(string_product_item):  
  word = str(string_product_item)
  result = word.find(".html?") 
  data_id = ''
  i = 1
  while(1):
    if (word[result-i]) != 'p':
      data_id = data_id + word[result-i]
      i += 1
    else:
      data_id = data_id[::-1]
      break
  return data_id


def crawl_product_id():
    product_list = []
    i = 1
    while (True):
        print("Crawl page: ", i)
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.344"}
        response = requests.get(laptop_page_url.format(i), headers=headers)
        parser = BeautifulSoup(response.text, 'html.parser')

        product_box = parser.findAll(class_="product-item")

        if (len(product_box) == 0):
            break

        for product in product_box:
            product_list.append(get_data_id(product))

        i += 1

    return product_list, i

def save_product_id(product_list=[]):
    file = open(product_id_file, "w+")
    str = "\n".join(product_list)
    file.write(str)
    file.close()
    print("Save file: ", product_id_file)

def crawl_product(product_list=[]):
    product_detail_list = []
    for product_id in product_list:
        response = requests.get(product_url.format(product_id))
        if (response.status_code == 200):
            product_detail_list.append(response.text)
            print("Crawl product: ", product_id, ": ", response.status_code)
    return product_detail_list

flatten_field = [ "badges", "inventory", "categories", "rating_summary", 
                      "brand", "seller_specifications", "current_seller", "other_sellers", 
                      "configurable_options",  "configurable_products", "specifications", "product_links",
                      "services_and_promotions", "promotions", "stock_item", "installment_info" ]

def adjust_product(product):
    e = json.loads(product)
    if not e.get("id", False):
        return None

    for field in flatten_field:
        if field in e:
            e[field] = json.dumps(e[field], ensure_ascii=False)

    return e

def save_raw_product(product_detail_list=[]):
    file = open(product_data_file, "w+")
    str = "\n".join(product_detail_list)
    file.write(str)
    file.close()
    print("Save file: ", product_data_file)

def load_raw_product():
    file = open(product_data_file, "r")
    return file.readlines()

def save_product_list(product_json_list):
    file = open(product_file, "w")
    csv_writer = csv.writer(file)

    count = 0
    for p in product_json_list:
        if p is not None:
            if count == 0:
                header = p.keys() 
                csv_writer.writerow(header) 
                count += 1
            csv_writer.writerow(p.values())
    file.close()
    print("Save file: ", product_file)


# crawl product id
product_list, page = crawl_product_id()

print("No. Page: ", page)
print("No. Product ID: ", len(product_list))

# save product id for backup
save_product_id(product_list)

# crawl detail for each product id
product_list = crawl_product(product_list)

# save product detail for backup
save_raw_product(product_list)

# product_list = load_raw_product()
# flatten detail before converting to csv
product_json_list = [adjust_product(p) for p in product_list]
# save product to csv
save_product_list(product_json_list)











    

