def calculate(math_expression: str) -> float:
    """示例工具：计算数学表达式"""
    try:
        return eval(math_expression)  # 注意：实际项目中避免直接eval！
    except:
        return None

def get_weather(city: str) -> str:
    """模拟天气查询工具"""
    return f"Weather in {city}: Sunny, 25°C"