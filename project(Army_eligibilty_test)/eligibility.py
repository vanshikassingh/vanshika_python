def check_eligibility(candidates):
    name = input("Enter candidate name: ")

    for c in candidates:
        if c["name"].lower() == name.lower():

            age = c["age"]
            gender = c["gender"].lower()
            qualification = c["qualification"].lower()

            print("\nEligible Entries:")

            found = False

            if 16 <= age <= 19:
                print("- NDA")
                found = True

            if age >= 19 and ("graduate" in qualification or "b.tech" in qualification):
                print("- CDS")
                found = True

            if gender == "female" and "b.tech" in qualification:
                print("- SSC Tech Women")
                found = True

            if gender == "male" and "b.tech" in qualification:
                print("- SSC Tech Men")
                found = True

            if not found:
                print("No eligible entries")

            return

    print("Candidate not found")