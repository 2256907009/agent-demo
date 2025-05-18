from AGENT_DEMO.agent import Agent
from tools import calculate, get_weather


def main():
    # 初始化Agent
    agent = Agent()

    # 注册工具
    agent.register_tool("calculate", calculate)
    agent.register_tool("get_weather", get_weather)

    # 交互循环
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        # 使用工具示例（简单演示）
        if user_input.startswith("calc "):
            expr = user_input[5:]
            result = agent.tools["calculate"](expr)
            print(f"Calculation result: {result}")
        elif user_input.startswith("weather "):
            city = user_input[8:]
            print(agent.tools["get_weather"](city))
        else:
            # 普通对话
            print(agent.respond(user_input))


if __name__ == "__main__":
    main()