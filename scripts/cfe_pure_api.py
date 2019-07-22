import json
import argparse

import requests


BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updates/"


def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    print(r.status_code)
    return r.json()


def create_update():
    new_data = {
        'user': 1,
        "content": "another new cool update"
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.status_code)
    return r.json() if r.status_code == requests.codes.ok else r.text


def do_obj_update(update_id):
    new_data = {
        "content": "New obj data"
    }
    id = str(update_id) + "/"
    r = requests.put(BASE_URL + ENDPOINT + id, data=json.dumps(new_data))
    print(r.status_code)
    return r.json() if r.status_code == requests.codes.ok else r.text


def do_obj_delete(delete_id):
    new_data = {
        "content": "New obj data"
    }
    id = str(delete_id) + "/"
    r = requests.delete(BASE_URL + ENDPOINT + id)
    print(r.status_code)
    return r.json() if r.status_code == requests.codes.ok else r.text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("method", help="the methed you want to call: get, post, put, delete.", type=str)
    parser.add_argument("--id", help="the obj id you want to deal with put, delete.", type=int)
    args = parser.parse_args()
    result = None
    if args.method == 'get':
        result = get_list()
    elif args.method == 'post':
        result = create_update()
    elif args.method == 'put':
        id = args.id
        result = do_obj_update(id)
    elif args.method == 'delete':
        id = args.id
        result = do_obj_delete(id)

    print(result)


if __name__ == "__main__":
    main()


