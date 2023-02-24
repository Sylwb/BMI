from operations import CalculatorBMI
from tqdm import tqdm
import time

print("*** Welcome the the BMI Calculator by Sylwester Bogusz ***\n")

weight = int(input("Please enter your weight in kg: "))
height = input("Please enter your height in meters: ")
height = height.replace(",", ".")

try:
    height = float(height)
except ValueError:
    print("Wrong datatype entered.")
    exit()

print("\nLoading...\n")
for i in tqdm(range(100), bar_format="{desc}{percentage:3.0f}%|{bar}| \033[34m{elapsed}\033[0m"):
    time.sleep(0.01)
print("")

diagnosis = CalculatorBMI.calculate(weight, height)

if diagnosis < 18.5:
    print(f"Your BMI is equal to {diagnosis}. You are underweight. Please take care of yourself.")
elif 18.5 <= diagnosis <= 24.9:
    print(f"Your BMI is equal to {diagnosis}. You are in good shape.")
elif diagnosis > 24.9:
    print(f"Your BMI is equal to {diagnosis}. You are overweight. Please take care of yourself.")
else:
    raise ValueError("The program encountered problem with data. Please try again.")

