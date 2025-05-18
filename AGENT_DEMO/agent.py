import os
from dotenv import load_dotenv
from typing import Dict, List
from .memory import Memory

load_dotenv()  # 加载环境变量


class Agent:
    def __init__(self):
        self.name = os.getenv("AGENT_NAME", "DefaultAgent")
        self.memory = Memory()
        self.tools = {}  # 可扩展的工具函数

    def respond(self, input_text: str) -> str:
        """处理输入并返回响应"""
        # 1. 记录到记忆
        self.memory.add(f"User: {input_text}")

        # 2. 生成响应（此处简化逻辑，实际可集成LLM API）
        response = f"{self.name}: I received your message - '{input_text}'. "
        response += f"(Memory size: {len(self.memory)})"

        # 3. 记录自身响应
        self.memory.add(response)
        return response

    def register_tool(self, name: str, tool_func: callable):
        """注册工具函数"""
        self.tools[name] = tool_func