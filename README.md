# Redis Prometheus Textfile Exporter

## Installing

### Clone the repo

```bash
git clone https://github.com/ashleykleynhans/redis-prometheus-textfile-exporter.git
cd redis-prometheus-textfile-exporter
```

### Create and activate a Python virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install the dependencies

```bash
pip3 install -r requirements.txt
```

### Create a config file

```bash
cp config.yml.example config.yml
```

### Add your RunPod API key and endpoints to the config file

1. Edit config.yml
2. Ensure that the redis `host` and `port` are congigured correctly.

### Run the script via a cron job to generate the files

Create a cron job that runs the script `redis_exporter_cron.sh.sh` at your preferred interval.

## Community and Contributing

Pull requests and issues on [GitHub](https://github.com/ashleykleynhans/redis-prometheus-textfile-exporter)
are welcome. Bug fixes and new features are encouraged.

## Appreciate my work?

<a href="https://www.buymeacoffee.com/ashleyk" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
