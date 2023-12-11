
outer_list = []
for _ in range(int(input())):
    inner_list = []
    name = input()
    score = float(input())
    inner_list = [name , score]
marks_list = [i[1] for i in outer_list ]
marks_2ndleast  = marks_list
for i in marks_list:
    if i > marks_list.min() :
        if i < marks_secondleast :
            marks_secondleast = i

