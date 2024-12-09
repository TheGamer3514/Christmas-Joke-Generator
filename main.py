# Import required modules
import os
import requests
import json  # For better handling of JSON data

def install_requests():
    """
    Check if the 'requests' library is installed, and install it if not.
    """
    try:
        import requests
    except ImportError:
        print("Requests library not found...\nInstalling...")
        os.system("pip install requests")
        print("Requests installed successfully.")

def fetch_christmas_joke():
    """
    Fetch a Christmas joke from the API.
    
    Returns:
        tuple: A tuple containing the joke question and answer.
    """
    try:
        response = requests.get("https://christmascountdown.live/api/joke")
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data.get("question", "No question found."), data.get("answer", "No answer found.")
    except requests.exceptions.RequestException as e:
        return "Error fetching joke:", str(e)

def display_joke():
    """
    Fetch and display a Christmas joke.
    """
    print("Fetching a Christmas joke for you...\n")
    question, answer = fetch_christmas_joke()
    print(f"Q: {question}\nA: {answer}")

def main():
    """
    Main function to run the Christmas Joke Generator.
    """
    print("Welcome to the Christmas Joke Generator!")
    while True:
        print("\nMenu:")
        print("1. Get a Christmas joke")
        print("2. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                display_joke()
            elif choice == 2:
                print("Merry Christmas! Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a numeric choice.")

# Run the script
if __name__ == "__main__":
    install_requests()
    main()
