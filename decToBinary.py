def ToBinaryConversion(n):
    if n == 0:
        return 0
    else:
        return (n % 2 + 10 *
                ToBinaryConversion(int(n // 2)))


# Driver Code
if __name__ == "__main__":

    decimal_number = 10
    print(ToBinaryConversion(decimal_number))