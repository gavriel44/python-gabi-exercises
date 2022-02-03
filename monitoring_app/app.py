import os
import psutil

from flask import Flask
from services import help, writer_service
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return dict(psutil.virtual_memory()._asdict())


@app.route("/stats")
def get_my_stats():
    stats = {"computerName": os.environ["COMPUTERNAME"], **dict(psutil.virtual_memory()._asdict()), }

    list_of_process_name = help.get_process_list()

    stats["process_list"] = list_of_process_name
    print(stats.keys())
    writer_service.write_dict_to_csv("test.csv", stats)

    return stats
