#!/usr/bin/env python3
import requests
import sys
import getopt
import json


def main(argv):

    server_address = ""
    server_address_required = True
    task_id = 0

    try:
        opts, args = getopt.getopt(
            argv, "h", ["server_address=", "task-create=", "task-list", "task-search", "task-delete", "task-update=", "task-id="])
    except getopt.GetoptError:
        print(
            'test.py --server_address <server-address> --task-id <task-id> (if required) --<task-option> <arguments>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--server_address':
            server_address = arg
        elif opt == '--task-id':
            task_id = arg
        elif opt == '-h':
            print(
                'test.py --server_address <server-address> --task-id <task-id> (if required) --<task-option> <arguments>')
            sys.exit()
            server_address_required = False
        elif opt == '--task-create':
            with open(arg) as json_file:
                arguments = json.load(json_file)
            print(arguments)
            r = requests.post(server_address + "/task",
                              data=json.dumps(arguments))
            print(r.url)
            print(r.text)
        elif opt == '--task-list':
            r = requests.get(server_address + "/task")
            print(r.url)
            print(r.text)
        elif opt == '--task-search':
            r = requests.get(server_address + "/task" + "/" + task_id)
            print(r.url)
            print(r.text)
        elif opt == '--task-delete':
            id_task = arg
            r = requests.delete(server_address + "/task" + "/" + arg)
            print(r.url)
            print(r.text)
        elif opt == '--task-update':
            with open(arg) as json_file:
                arguments = json.load(json_file)
            r = requests.put(server_address + "/task" + "/" + task_id,
                             data=json.dumps(arguments))
            print(r.url)
            print(r.text)

    if (server_address == "" and server_address_required):
        print("--server_address argument is required")
        sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
