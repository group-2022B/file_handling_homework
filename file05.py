def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    digit = 0
    non_digit = 0
    for line in data:
        for char in line:
            if char.isdigit():
                digit += 1
            else:
                non_digit += 1
    return [digit, non_digit]
    
# Read data from file
with open('txt_file/data05.txt', 'r') as f:
    data = f.readlines()
    print(main(data))