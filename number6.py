def create_multiplication_table():
    table = []
    for i in range(1, 11):
        row = [i * j for j in range(1, 11)]
        table.append(row)
    return table

def print_multiplication_table(table):
    for i, row in enumerate(table, start=1):
        print(f"Table {i}: {row}")

def main():
    multiplication_table = create_multiplication_table()
    print_multiplication_table(multiplication_table)

if __name__ == "__main__":
    main()