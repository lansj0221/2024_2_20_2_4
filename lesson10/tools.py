
import random

def get_names(nums:int = 5) -> list[str]:
    with open('names.txt',encoding='utf8') as file:
        content:str = file.read()
        names:list[str] = content.split(sep='\n')
        random_names:list[str] = random.choices(names,k=nums)
    return random_names

def get_scores(names:list[str]) -> list[dict]:
    stus:list[dict] = []
    for name in names:
        stu:dict[str:any] = {}
        stu["name"] = name
        stu["height"] = random.randint(150,220)
        stu["weight"] = random.randint(50,100)
        stu["math"] = random.randint(50,100)
        stus.append(stu)
    return stus