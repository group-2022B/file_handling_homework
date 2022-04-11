import re


def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    ans = []
    for line in data.split('\n'):
        ans.append(len(line))
    return ans
    
# Read data from file
with open('txt_file/data06.txt', 'r') as f:
    data = f.read()
    print(main(data))