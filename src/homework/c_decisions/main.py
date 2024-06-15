# Import the necessary module
import decisions

def main():
    # Prompt the user for options and convert the input to an integer
    options = int(input("Enter the number of options: "))

    # Prompt the user for total and convert the input to a float
    total = float(input("Enter the total: "))

    # Calculate the ratio using the decisions module's get_options_ratio function
    ratio = decisions.get_options_ratio(options, total)

    # Get the faculty rating using the calculated ratio
    faculty_rating = decisions.get_faculty_rating(ratio)

    # Display the faculty rating
    print(f"Faculty Rating: {faculty_rating}")

if __name__ == "__main__":
    main()

