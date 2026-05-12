import os
import time
import random
from typing import Dict, List

# 模拟 LLM 调用 (实际开发中请替换为 MiMo 或 DeepSeek API)
def call_llm(prompt: str) -> str:
    # 这里模拟了 Token 的消耗过程
    print(f"🤖 [System] 正在思考并消耗 Token...\n提示词: {prompt[:50]}...")
    time.sleep(1) 
    return "模拟的 AI 回复内容"

# 工具 1: 搜索机票/火车
def search_flights(origin: str, destination: str, date: str) -> str:
    print(f"🔧 [Tool] 调用搜索工具: 查询 {date} 从 {origin} 到 {destination} 的票务...")
    # 模拟 API 返回
    return f"查询结果: {date} {origin}飞往{destination} 的航班 CA1234 余票充足，价格 800元。"

# 工具 2: 搜索酒店
def search_hotels(city: str, date: str, budget: int) -> str:
    print(f"🔧 [Tool] 调用地图/酒店工具: 查询 {city} 预算 {budget} 以内的酒店...")
    # 模拟 API 返回
    return f"查询结果: {city} 市中心汉庭酒店，价格 {budget}元/晚，距离地铁站 200米。"

# 核心 Agent 类
class TravelAgent:
    def __init__(self):
        self.history = []

    def run(self, user_input: str):
        # 1. 简单的意图识别 (实际应使用 LLM 进行结构化输出)
        response = ""
        
        if "机票" in user_input or "航班" in user_input:
            # 模拟提取参数 (实际应使用 LLM 提取)
            tool_response = search_flights("北京", "上海", "下周二")
            response = call_llm(f"根据用户提问：{user_input} 和 搜索结果：{tool_response}，生成回复。")
            
        elif "酒店" in user_input:
            tool_response = search_hotels("上海", "下周二", 500)
            response = call_llm(f"根据用户提问：{user_input} 和 搜索结果：{tool_response}，生成回复。")
            
        else:
            response = call_llm(user_input)

        return response

# 主程序入口
if __name__ == "__main__":
    print("🚀 智能差旅助手已启动 (输入 'exit' 退出)")
    agent = TravelAgent()
    
    while True:
        query = input("\n👤 用户: ")
        if query.lower() == 'exit':
            break
        answer = agent.run(query)
        print(f"💡 助手: {answer}")