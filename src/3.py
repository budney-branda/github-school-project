
import random

def get_random_python_code():
    """
    Generates a random Python code snippet
    """
    code = f"""
    {random.choice(["print", "return"])}({random.choice(["Hello, World!", "1 + 1"])})
    """
    return code