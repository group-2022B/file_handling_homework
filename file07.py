def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    ans = []

    for i in data:
        for j in i:
            if j.isdigit():
                ans.append(int(j))
    return sum(ans)
    
# Read data from file
with open('txt_file/data07.txt', 'r') as f:
    data = f.readlines()
    print(main(data))
    