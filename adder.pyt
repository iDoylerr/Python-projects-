# [Start] Start the program

class Adder:
    # Constructor method (initialize object attributes)
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # Method to add two numbers
    def add_numbers(self):
        return self.num1 + self.num2

while True:
    try:
        # [Input] Input the first number
        num1 = float(input("Enter the first number: "))
        
        # [Input] Input the second number
        num2 = float(input("Enter the second number: "))

        # [Create Instance] Create an instance of the Adder class
        adder_instance = Adder(num1, num2)

        # [Method Call] Call the add_numbers method
        result = adder_instance.add_numbers()

        # [Display Result] Display the result
        print("The sum of {} and {} is: {}".format(num1, num2, result))
        break  # Exit the loop if input and calculation are successful

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# [End] End of the program
