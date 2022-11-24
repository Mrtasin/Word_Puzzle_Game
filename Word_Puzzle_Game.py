import random

def main():
    score = 0
    world = ['FATHER','BREAK','MOTHER']
    world = random.sample(world, k = len(world))
    for world1 in world:
        score = World_Puzzle(world1, score)
    print(score)


def World_Puzzle(world1,score):
    temp = world1
    world1 = random.sample(world1, k = len(world1))
    world1 = ''.join(world1)
    Word = input(f"Arrange the letters to form a valid word : \n{world1}").upper()
    if temp == Word:
        print("\nCorrect")
        return score+1
    else:
        print("\nWrong")
        return score-1

main()