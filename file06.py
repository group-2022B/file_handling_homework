def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
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
with open('txt_file/data06.txt', 'r') as f:
    data = f.readlines()
    print(main(data))