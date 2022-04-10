def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    ans = []
    for line in data:
        for char in line:
            if char.isdigit():
                continue
            else:
                ans.append(char)
    return ans

    
# Read data from file
with open('txt_file/data04.txt', 'r') as f:
    data = f.readlines()
    print(main(data))