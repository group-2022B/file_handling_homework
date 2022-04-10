def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    ans = []
    temp = data.split('\n')
    for i in temp:
        for j in i:
            if not j.isdigit():
                ans += j
    return ans

    
# Read data from file
with open('txt_file/data04.txt', 'r') as f:
    data = f.read()
    print(main(data))