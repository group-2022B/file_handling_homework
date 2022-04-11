def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
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
    return max(ans)

# Read data from file
with open('txt_file/data08.txt', 'r') as f:
    data = f.readlines()
    print(main(data))
    