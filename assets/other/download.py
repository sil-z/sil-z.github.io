import os
import json
import requests
from urllib.parse import urlparse
from time import sleep
from PIL import Image

def download_1(filename: str):
    json_data = None
    with open(filename, "r", encoding="utf-8") as f:
        json_data = json.load(f)
    failed_collections = []
    for entry in json_data:
        collection_name = entry["collection"]
        items = entry["item"]
        folder_path = os.path.join(os.getcwd(), collection_name)
        os.makedirs(folder_path, exist_ok=True)

        print(f"processing collection: {collection_name}")
        failed_items = []

        for url in items:
            file_path = os.path.join(folder_path, f"{url.split('/')[-3]}.jpg")

            if os.path.exists(file_path):
                continue
            try:
                response = requests.get(url, stream=True, timeout=30)
                response.raise_for_status()
                with open(file_path, "wb") as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                with Image.open(file_path) as img:
                    img.verify()
                print(f"[OK] {file_path}")
            except Exception as e:
                print(f"[FAIL] {file_path}")
                failed_items.append(url)
            sleep(0.1)

        if failed_items:
            failed_collections.append({
                "collection": collection_name,
                "item": failed_items
            })
        
            # record files failed to download
            # can be used as input files for re-running the download program later
            with open("failed_downloads.json", 'w', encoding='utf-8') as f:
                json.dump(failed_collections, f, indent=4)
    
def download_2(filename: str):
    content = None
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    urls = content.splitlines()
    failed_urls = []
    for url in urls:
        file_path = os.path.join(os.getcwd(), f"{url.split('/')[-1]}")
        if os.path.exists(file_path):
            continue
        try:
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            
            with open(file_path, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"[OK] {file_path}")
        except Exception as e:
            print(f"[FAIL] {url}")
            failed_urls.append(url)
    # record files failed to download
    # can be used as input files for re-running the download program later
    with open("failed_urls.txt", "w", encoding='utf-8') as f:
        f.write(failed_urls)

if __name__ == "__main__":
    # download the files from the scranton website
    # need to read file informations from the json file
    download_1("scranton_json.txt")
    # download the files from the internet archive
    # with several direct file urls
    download_2("journalsfromarchive.txt")

# download_1 函数下载 Scranton 网站上的文件
# download_2 函数下载 Internet Archive 网站上的文件
# 脚本可以随时中断运行，每次运行都会从头开始检查未下载的文件
# 下载图片常常会失败，失败数据将输出到一个额外的文本文件中，不用管，重新运行脚本即可重头下载所有失败文件
# 重复运行脚本，直至脚本未输出任何下载失败信息