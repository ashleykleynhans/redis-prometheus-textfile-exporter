#!/usr/bin/env python3
import os
import sys
import redis
import yaml
from typing import Dict

KEYS_TO_SKIP = [
    'redis_version',
    'redis_ssl_current_certificate_not_before_date',
    'redis_ssl_current_certificate_not_after_date',
    'redis_ssl_current_certificate_serial',
    'redis_errorstat_LOADING'
]


def load_config(script_path):
    try:
        config_file = f'{script_path}/config.yml'

        with open(config_file, 'r') as stream:
            return yaml.safe_load(stream)
    except FileNotFoundError:
        print(f'ERROR: Config file {config_file} not found!')
        sys.exit()


def get_redis_client(config, decode_responses=False):
    return redis.Redis(
        host=config['redis']['host'],
        port=config['redis']['port'],
        decode_responses=decode_responses
    )


def fetch_data(config):
    redis_client = get_redis_client(config, True)
    data = redis_client.info()
    return data


def write_data(data):
    filename = 'redis.prom'
    output_file = os.path.join(config['textfile_path'], filename)
    tmp_output_file = f'{output_file}.$$'

    f = open(tmp_output_file, 'a')
    for key, value in data.items():
        if isinstance(value, Dict) or key in KEYS_TO_SKIP:
            continue

        if not key.startswith('redis_'):
            key = f'redis_{key}'

        # print(key, value)
        f.write(f'{key} {value}\n')
    f.close()

    os.rename(tmp_output_file, output_file)


if __name__ == '__main__':
    script_path = os.path.dirname(__file__)
    config = load_config(script_path)
    data = fetch_data(config)
    write_data(data)
