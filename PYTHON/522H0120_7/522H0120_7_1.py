import random

def dice_experiment_probability(n):
    total_experiments = n
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_e = 0
    count_f = 0
    count_g = 0

    for _ in range(total_experiments):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        if dice1 == dice2:
            count_a += 1
        else:
            count_b += 1

        if (dice1 % 2 == 0) and (dice2 % 2 == 0):
            count_c += 1

        if (dice1 % 2 != 0) and (dice2 % 2 != 0):
            count_d += 1

        if (dice1 % 2 == 0) and (dice2 % 2 != 0):
            count_e += 1
        elif (dice1 % 2 != 0) and (dice2 % 2 == 0):
            count_e += 1

        if (dice1 == 6) and (dice2 == 6):
            count_f += 1

        if (dice1 + dice2) > 10:
            count_g += 1

    probability_a = count_a / total_experiments
    probability_b = count_b / total_experiments
    probability_c = count_c / total_experiments
    probability_d = count_d / total_experiments
    probability_e = count_e / total_experiments
    probability_f = count_f / total_experiments
    probability_g = count_g / total_experiments

    print("Xác suất thực nghiệm sau", total_experiments, "lần gieo:")
    print("a) Hai viên giống nhau:", probability_a)
    print("b) Hai viên khác nhau:", probability_b)
    print("c) Hai viên cùng chẵn:", probability_c)
    print("d) Hai viên cùng lẻ:", probability_d)
    print("e) Một viên chẵn và một viên lẻ:", probability_e)
    print("f) Hai viên cùng ra 6:", probability_f)
    print("g) Hai viên có tổng số nút lớn hơn 10:", probability_g)

dice_experiment_probability(1000)