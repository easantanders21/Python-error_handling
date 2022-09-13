def run():
    squares = []
    for i in range(1, 101):
        if i % 3 != 0:
            squares.append(i**2)

    print(squares)
    
    squeares_c = [i**2 for i in range(1, 101) if i %3 != 0]
    
    print(squeares_c)


if __name__ == '__main__':
    run()
