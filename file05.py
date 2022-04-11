def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    ans = []
    for i in data:
        ans.append(len(i))
    return ans
    
# Read data from file
with open('txt_file/data04.txt', 'r') as f:
    data = f.readlines()
    print(main(data))