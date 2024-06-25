def main():
    names = []
    # Store names
    while True:
        name = input("Enter a name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        names.append(name)
    
    # Greet people
    for name in names:
        print(f"Hello, {name}!")

if __name__ == "__main__":
    main()