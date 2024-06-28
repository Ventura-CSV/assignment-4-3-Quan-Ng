def main():
    number = int(input('Enter your input: '))
    result = []
    """
    ########################################
    Code Your Program here
    ########################################
    """

    while x >= 2:
        remainder = x % 2
        result.append(remainder)
        x = x // 2
        
        result.append(x)
        
        
    
    print(*result)
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
