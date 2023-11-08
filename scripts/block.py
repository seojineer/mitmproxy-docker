import logging
from typing import List
import os

from mitmproxy import command
from mitmproxy import flow
from mitmproxy import http

pwd = os.path.dirname(os.path.realpath(__file__))

def get_ro_list() -> List:
    with open(f'{pwd}/read-only-list', 'r') as f:
        return [_ for _ in f.read().split('\n') if _]

def requestheaders(flow: http.HTTPFlow) -> None:
    logging.info(f"flow: {flow}")
    logging.info(f"flow.request: {flow.request}")
    logging.info(f"flow.request.host: {flow.request.host}")
    logging.info(f"flow.request.path: {flow.request.path}")

    logging.info(f'read-only domain: {get_ro_list()}')
    if flow.request.host in get_ro_list() and "service=git-receive-pack" in flow.request.path:
        logging.info("push event!")
        flow.response = http.Response.make(403, b"Permission denied.")
