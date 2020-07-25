import random
import sys
import threading
import queue
import time
import argparse
import requests
import logging

hac_cam_URL = "http://localhost:8888/"

def worker(cam_position):
    r = requests.get(f'"{hac_cam_URL}{cam_position}?getimage"')
    logging.info(f'"POSITION : #{cam_position}" resp {r}')

def main():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    threads = []

    print("-- test ids [CAM THREADS] --")

    # define args parser - simple
    parser = argparse.ArgumentParser()
    parser.add_argument("--positions_max", help="array contains every cameras position (refers to config.ini)")

    args = parser.parse_args()
    cam_positions_max = int(args.positions_max)


    for i in range(1, int(cam_positions_max) + 1):
        cam_position = i
        th = threading.Thread(target=worker, args=(cam_position,), daemon=True)
        threads.append(th)

    for i in threads:
        i.start()

    for x in threads:
        x.join()

if __name__ == "__main__":
    # execute only if run as a script
    main()