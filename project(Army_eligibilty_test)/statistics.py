def show_statistics(candidates):
    total = len(candidates)
    male = 0
    female = 0

    for c in candidates:
        if c["gender"].lower() == "male":
            male += 1
        elif c["gender"].lower() == "female":
            female += 1

    print("\n--- STATISTICS ---")
    print("Total Candidates:", total)
    print("Male:", male)
    print("Female:", female)