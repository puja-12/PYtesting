def day_of_the_week(y, m, d):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

    if m < 3:
        y = y - 1

    return (y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7


# Driver Code
day = 13
month = 7
year = 2017

print(day_of_the_week(year, month, day))

