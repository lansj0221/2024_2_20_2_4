import random
import pyinputplus as pyip
from pprint import pprint

def generate_data_structure(nums: int) -> list[dict]:
    data_structure = []
    for _ in range(nums):
        person = {}
        person["name"] = "xxx"  # 假設所有人的名字都是 "xxx"
        person["height"] = random.randint(150, 220)
        person["weight"] = random.randint(40, 90)
        data_structure.append(person)
    return data_structure

def main():
    nums = pyip.inputInt("請輸入人數(1~50): ", min=1, max=50)
    data_structure = generate_data_structure(nums)
    pprint(data_structure)

if __name__ == "__main__":
    main()
