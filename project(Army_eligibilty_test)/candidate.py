def add_candidate(candidates):
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    qualification = input("Enter Qualification: ")
    marital_status = input("Enter Marital Status: ")

    candidate = {
        "name": name,
        "age": age,
        "gender": gender,
        "qualification": qualification,
        "marital_status": marital_status
    }

    candidates.append(candidate)
    print("Candidate added successfully!")


def view_candidates(candidates):
    if not candidates:
        print("No candidates found.")
        return

    for c in candidates:
        print(c)


def search_candidate(candidates):
    name = input("Enter name to search: ")

    for c in candidates:
        if c["name"].lower() == name.lower():
            print(c)
            return

    print("Candidate not found.")