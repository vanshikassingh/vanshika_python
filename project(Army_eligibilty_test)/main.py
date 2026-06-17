from candidate import add_candidate, view_candidates, search_candidate
from eligibility import check_eligibility
from file_handler import save_to_file
from statistics import show_statistics

candidates = []

while True:
    print("\n===== ARMY ELIGIBILITY SYSTEM =====")
    print("1. Add Candidate")
    print("2. View Candidates")
    print("3. Search Candidate")
    print("4. Check Eligibility")
    print("5. Statistics")
    print("6. Save to File")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_candidate(candidates)

    elif choice == 2:
        view_candidates(candidates)

    elif choice == 3:
        search_candidate(candidates)

    elif choice == 4:
        check_eligibility(candidates)

    elif choice == 5:
        show_statistics(candidates)

    elif choice == 6:
        save_to_file(candidates)

    elif choice == 7:
        print("Exiting system...")
        break

    else:
        print("Invalid choice!")