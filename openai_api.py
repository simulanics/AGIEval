# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import json
import openai
from multiprocessing.pool import ThreadPool
import threading
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

credential = DefaultAzureCredential()

token_provider = get_bearer_token_provider(
    credential,
    "https://cognitiveservices.azure.com/.default")

deployment_name = 'gpt-35-turbo'

if deployment_name == 'gpt-4o':
    azure_endpoint = ""
    api_version = ""

if deployment_name == 'gpt-35-turbo':
    azure_endpoint = ""
    api_version = ""

client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    azure_ad_token_provider=token_provider,
    api_version=api_version,
    max_retries=5,
)

class Timer(object):
    def __init__(self):
        self.__start = time.time()

    def start(self):
        self.__start = time.time()

    def get_time(self, restart=True, format=False):
        end = time.time()
        span = end - self.__start
        if restart:
            self.__start = end
        if format:
            return self.format(span)
        else:
            return span

    def format(self, seconds):
        return datetime.timedelta(seconds=int(seconds))

    def print(self, name):
        print(name, self.get_time())


# # fill in your OpenAI API key in the {} below, format: "custum_api_name": "your_api_key"
API_dic = {"": ""}
#
API_name_key_list = list(API_dic.items())
default_engine = None


def multi_threading_running(func, queries, n=20):
    def wrapped_function(query, max_try=20):
        result = func(query)
        return result
    pool = ThreadPool(n)
    replies = pool.map(wrapped_function, queries)
    return replies


cache = {}
def query_azure_openai_chat(query, engine="gpt-35-turbo"):
    global client
    query_string = json.dumps(query)
    if query_string in cache:
        return cache[query_string]
    if engine == "chatgpt":
        engine = "gpt-35-turbo"
    try:
        messages = [
            {"role": "system", "content": "You are a helpful AI assistant."},
        ]
        if isinstance(query, str):
            messages.append(
                {"role": "user", "content": query},
            )
        elif isinstance(query, list):
            messages += query
        else:
            raise ValueError("Unsupported query: {0}".format(query))
        response = client.chat.completions.create(
            model=engine,
            messages=messages,
            temperature=0,
            stop=["<|im_end|>"]
        )
        print("response:", response)
    except TypeError as e:
        print("type error:", e)
        return {'choices': [{'message': {'content': ""}}]}
    except Exception as e:
        print("Unexpected error occurred:", e)
        return {'choices': [{'message': {'content': ""}}]}
    return response

def query_azure_openai_complete(query, engine="gpt-35-turbo"):
    global client
    if engine == 'chatgpt':
        engine = "gpt-35-turbo"
    try:
        response = client.completions.create(
            model=engine,
            prompt=query,
            max_tokens=2000,
            temperature=0,
            stop=["<END>"])
    except TypeError as e:
        print(e)
        return {"choices": [{"text": ""}]}
    return response
    # return response["choices"][0]["text"]


import time
import datetime

class Timer(object):

    def __init__(self):
        self.__start = time.time()

    def start(self):
        self.__start = time.time()

    def get_time(self, restart=True, format=False):
        end = time.time()
        span = end - self.__start
        if restart:
            self.__start = end
        if format:
            return self.format(span)
        else:
            return span * 1000

    def format(self, seconds):
        return datetime.timedelta(seconds=int(seconds))

    def print(self, name):
        print(name, self.get_time())

if __name__ == "__main__":
    API_ID=0
    print(query_azure_openai_chat("1+1", engine='gpt-35-turbo'))
    # test_speed_2()

