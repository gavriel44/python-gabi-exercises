import shutil

from requests import get
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime


def create_base_dir(base_name: str) -> str:
    try:
        time = str(datetime.now().strftime("%H-%M-%S"))
        target_directory_name = f"{base_name}/{time}"
        Path(target_directory_name).mkdir(parents=True, exist_ok=True)
        return target_directory_name
    except Exception as e:
        print(e)
        raise e


def filter_images_tags(soup: BeautifulSoup) -> list:
    final_image_elements = []

    for image_element in soup.find_all("img", {"alt": True, "src": True}):
        if image_element["src"].endswith(".jpg"):
            final_image_elements.append(image_element)

    return final_image_elements


def scrape_wikipedia_images(article_name: str):
    article_response = get(f'https://en.wikipedia.org/wiki/{article_name}')
    soup = BeautifulSoup(article_response.content, "html.parser")

    # Creates the needed directory by specifications and return the target directory name
    target_directory_name = create_base_dir(article_name)

    image_elements = filter_images_tags(soup)

    for image_element in image_elements:
        try:
            response = get("https:" +
                           image_element["src"],
                           stream=True)
            if response.status_code == 200:
                print("success")
                with open(target_directory_name + (f"/{image_element['alt']}" if image_element['alt'].endswith(
                        '.jpg') else f"/{image_element['alt']}.jpg"), "wb") as file:
                    print("test")
                    response.raw.decode_content = True
                    shutil.copyfileobj(response.raw, file)

        except Exception as e:
            print(e)
            print(f"pic alt: {image_element['alt']} failed to download. moving on to next pic...")


if __name__ == '__main__':
    article = input("enter article name: ")
    scrape_wikipedia_images(article)
