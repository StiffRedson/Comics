import os
import sys
from random import randint
import requests
from dotenv import load_dotenv

GROUP_ID = 186864937


def download_comic():
    comic_number = randint(0, 2010)
    filename = "comics_python.png"
    url = f"https://xkcd.com/{comic_number}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()

    description_comic = response.json()['alt']
    url_image = response.json()['img']
    answer = requests.get(url_image)

    with open(filename, "wb") as file:
        file.write(answer.content)

    return description_comic


def get_server_address(vk_authorization):
    url = "https://api.vk.com/method/photos.getWallUploadServer"
    params = {
        "access_token": vk_authorization,
        "group_id": GROUP_ID,
        "v": 5.101
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    upload_url = response.json()["response"]['upload_url']
    return upload_url


def upload_photo_to_server(upload_url):
    with open('comics_python.png', 'rb') as file:
        files = {
            'file1': file,
        }
        response = requests.post(upload_url, files=files)
        response.raise_for_status()
        image_form_data = response.json()["photo"]
        server_id = response.json()["server"]
        hash_id = response.json()["hash"]
    return image_form_data, server_id, hash_id


def save_photo_to_album(vk_authorization, image, server, hash):
    url = "https://api.vk.com/method/photos.saveWallPhoto"
    params = {
        "access_token": vk_authorization,
        "group_id": GROUP_ID,
        "server": server,
        "hash": hash,
        "photo": image,
        "v": 5.101
    }

    response = requests.post(url, params=params)
    response.raise_for_status()
    received_from_server = response.json()["response"]
    for data_picture in received_from_server:
        owner = data_picture["owner_id"]
        media = data_picture["id"]
    return owner, media


def post_photo_on_wall(vk_authorization, owner_id, media_id, description_comic):
    url = "https://api.vk.com/method/wall.post"
    params = {
        "access_token": vk_authorization,
        "owner_id": f"-{GROUP_ID}",
        "from_group": 1,
        "attachments": f"photo{owner_id}_{media_id}",
        "message": description_comic,
        "v": 5.101
    }

    response = requests.post(url, params=params)
    response.raise_for_status()


def main():
    load_dotenv()
    vk_authorization = os.getenv("VK_ACCESS_TOKEN")

    if vk_authorization is None:
        sys.exit("[*] Vk token not found")

    try:
        comment = download_comic()

        url = get_server_address(vk_authorization)
        response_server = upload_photo_to_server(url)

        photo = response_server[0]
        server_id = response_server[1]
        hash = response_server[2]

        information_from_server = save_photo_to_album(vk_authorization, photo, server_id, hash)

        owner = information_from_server[0]
        media = information_from_server[1]

        post_photo_on_wall(vk_authorization, owner, media, comment)

    except requests.exceptions.HTTPError as http_err:
        print(f'[*] Check that the VK token is correct\n {http_err}')
    except requests.exceptions.ConnectionError as connect_err:
        exit(f'[*] Check Your network connection\n {connect_err}')
    except requests.exceptions.RequestException as err:
        print(f'[*] Something went wrong\n {err}')

    try:
        os.remove("comics_python.png")
    except OSError as os_err:
        print(f"[*] Could not close file..{os_err}")


if __name__ == "__main__":
    main()
