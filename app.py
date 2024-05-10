from cal_func import do_addition, do_subtraction
from multiply import do_multiplication
def main():
    print("welcome to calculator app")
    print("""
          \nSelect the funciton from the given options
          1. Add
          2. Subtract
          3. Multiplication
          """)
    user_input = input("select the function")

    a = int(input("value of A "))
    b = int(input("value of B "))

    if user_input == "1":
        result = do_addition(a,b)
    elif user_input == "2":
        result = do_subtraction(a,b)
    elif user_input =="3":
        result = do_multiplication(a,b)
    
    print("Result : ", result)

if __name__ == "__main__":
    main()
