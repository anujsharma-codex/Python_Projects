for filename in ["cats.txt", "dogs.txt"]:
    try:
        with open(filename) as f:
            print(f"\nContents of {filename}:")
            for line in f:
                print(line.strip())
    except FileNotFoundError as e:
        pass