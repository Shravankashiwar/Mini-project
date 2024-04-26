class VotingSystem:
    def _init_(self, candidates):
        self.candidates = candidates
        self.votes = {candidate: 0 for candidate in candidates}

    def vote(self, candidate):
        if candidate in self.candidates:
            self.votes[candidate] += 1
            print(f"Voted for {candidate} successfully!")
        else:
            print("Invalid candidate.")

    def get_results(self):
        print("Voting Results:")
        for candidate, votes in self.votes.items():
            print(f"{candidate}: {votes} votes")

def main():
    candidates = ["Candidate A", "Candidate B", "Candidate C"]
    voting_system = VotingSystem(candidates)

    while True:
        print("\nWelcome to the Voting System!")
        print("1. Vote")
        print("2. View Results")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            candidate = input("Enter the name of the candidate you want to vote for: ")
            voting_system.vote(candidate)
        elif choice == '2':
            voting_system.get_results()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if _name_ == "_main_":
    main()