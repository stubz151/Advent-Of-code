from collections import defaultdict
from common_logic import CommonLogic

def day1_p1(fh):
    first_list = []
    second_list = []
    print("sorting")
    for line in fh:
        line_split = line.split(" ")
        first_list = CommonLogic.insert_sorted(first_list, int(line_split[0]))
        second_list = CommonLogic.insert_sorted(second_list, int(line_split[3]))
    total = 0
    for i in range(len(first_list)):
        total += abs(first_list[i] - second_list[i])
    
    print(total)
    
def day1_p2(fh):
    first_dict = defaultdict(int)
    second_dict = defaultdict(int)
    for line in fh:
        line_split = line.split(" ")
        first_dict[int(line_split[0])] +=1
        second_dict[int(line_split[3])] +=1
    
    total = 0  
    for key, num in first_dict.items():
        if key in second_dict:
            total += (key * num * second_dict[key])
    print(total)
        
if __name__ == "__main__":    
    with open('input.txt', 'r') as fh:
        day1_p1(fh)
        day1_p2(fh)