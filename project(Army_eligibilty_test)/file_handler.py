def save_to_file(candidates):
    with open("data.txt", "w") as f:
        for c in candidates:
            f.write(str(c) + "\n")

    print("Data saved successfully!")