#General API tests for any of the included frameworks egt. Qiskit, OpenAI or TogetherAI

import os
from dotenv import load_dotenv
load_dotenv()

class APITest:
    def __init__(self, api, api_key):
        self.base_url="127.0.0.1:8000"
        self.headers = "" #default_headers""
        