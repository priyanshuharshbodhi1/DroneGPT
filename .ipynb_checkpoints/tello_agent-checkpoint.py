# -*- coding: utf-8 -*-
# @Time    : 2025/07/10  23:12
# @Author  : mariswang@rflysim
# @File    : airsim_agent.py
# @Software: PyCharm
# @Describe:
# -*- encoding:utf-8 -*-
import os
from openai import OpenAI
import re
import tello_wrapper

BASE_URL = "https://api.intelligence.io.solutions/api/v1/"
ARK_API_KEY = "*****" # your api key，visit https://ai.io.net/ai/api-keys
MODEL = "deepseek-ai/DeepSeek-R1-0528" #model list：https://docs.io.net/reference/get-started-with-io-intelligence-api

#初始化无人机
aw = tello_wrapper.TelloWrapper()

class TelloAgent:
    def __init__(self, system_prompts="system_prompts/airsim_basic.txt", knowledge_prompt="prompts/airsim_basic.txt", chat_history=[]):
        #llm client
        self.client = OpenAI(
            base_url = BASE_URL,
            api_key = ARK_API_KEY,
        )

        # 先对话列表，全局变量
        self.chat_history = []

        # 系统提示词，读取并加入对话记录
        sys_prompt = open(system_prompts, "r", encoding="utf8").read()
        chat_history.append(
            {
                "role": "system",
                "content": sys_prompt,
            }
        )

        # 知识库，并加入对话记录，通过聊天函数，加入知识库
        kg_prompt = open(knowledge_prompt, "r", encoding="utf8").read()
        self.ask(kg_prompt)

    # 调用chat api，包含历史记录，多轮对话
    def ask(self, prompt):
        # 加入用户输入的prompt
        self.chat_history.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        completion = self.client.chat.completions.create(
            model=MODEL,
            messages=self.chat_history,  # chat_history[-10:0]
            temperature=0.1,
        )

        #h回复
        content = completion.choices[0].message.content

        # 加入机器人回复，相当于保存全部的历史记录，多轮对话
        self.chat_history.append(
            {
                "role": "assistant",
                "content": content,
            }
        )

        return content

    # 解析python代码
    def extract_python_code(self, content):
        """
        Extracts the python code from a response.
        :param content:
        :return:
        """
        code_block_regex = re.compile(r"```(.*?)```", re.DOTALL)
        code_blocks = code_block_regex.findall(content)
        if code_blocks:
            full_code = "\n".join(code_blocks)

            if full_code.startswith("python"):
                full_code = full_code[7:]

            return full_code
        else:
            return None

    def process(self, command,run_python_code=False):
        #step 1, ask ernie
        response = self.ask(command)

        #step 2, extract python code
        python_code = self.extract_python_code(response)

        #step 3, exec python code
        if run_python_code and python_code:
            exec(python_code)
        return python_code

if __name__=="__main__":
    airsim_agent = AirSimAgent(knowledge_prompt="prompts/aisim_lession23.txt")
    command = "起飞"
    python_code = airsim_agent.process(command)
    print("python_code:", python_code)
