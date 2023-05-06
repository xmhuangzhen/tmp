import os
import json
import sys
import subprocess
import tempfile
from typing import List
import time
import datetime
import yaml
import socket
import pickle
import flbenchmark.datasets
import flbenchmark.logging

import colink as CL

from unifed.frameworks.test.util import store_error, store_return, GetTempFileName, get_local_ip

pop = CL.ProtocolOperator(__name__)
UNIFED_TASK_DIR = "unifed:task"


@pop.handle("unifed.test:server")
@store_error(UNIFED_TASK_DIR)
@store_return(UNIFED_TASK_DIR)
def run_server(cl: CL.CoLink, param: bytes, participants: List[CL.Participant]):

    # run external program
    participant_id = [i for i, p in enumerate(participants) if p.user_id == cl.get_user_id()][0]
    
    return json.dumps({
            "server_ip": "1",
            "stdout": "1",
            "stderr": "1",
            "returncode": "1",
    })


@pop.handle("unifed.test:client")
@store_error(UNIFED_TASK_DIR)
@store_return(UNIFED_TASK_DIR)
def run_client(cl: CL.CoLink, param: bytes, participants: List[CL.Participant]):
    # get the ip of the server
    server_in_list = [p for p in participants if p.role == "server"]
    assert len(server_in_list) == 1
    p_server = server_in_list[0]
    # run external program
    participant_id = [i for i, p in enumerate(participants) if p.user_id == cl.get_user_id()][0]
    

    return json.dumps({
            "server_ip": "1",
            "stdout": "1",
            "stderr": "1",
            "returncode": "1",
    })