import random

def ball_experiment_probability(n):
    total_experiments = n
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_e = 0

    for _ in range(total_experiments):
        balls = ['X', 'X', 'R', 'R', 'R', 'W', 'W', 'W', 'W', 'W']

        drawn_balls = random.sample(balls, 3)

        if drawn_balls.count('X') == 3:
            count_a += 1

        if len(set(drawn_balls)) == 3:
            count_b += 1

        if drawn_balls.count('R') == 2 or drawn_balls.count('W') == 2:
            count_c += 1

        if drawn_balls.count('R') == 2 and drawn_balls.count('W') == 1:
            count_d += 1

        if drawn_balls.count('W') == 3:
            count_e += 1

    probability_a = count_a / total_experiments
    probability_b = count_b / total_experiments
    probability_c = count_c / total_experiments
    probability_d = count_d / total_experiments
    probability_e = count_e / total_experiments

    print("Xác suất thực nghiệm sau", total_experiments, "lần bốc bi:")
    print("a) Cả ba viên cùng màu:", probability_a)
    print("b) Cả ba viên đều khác màu nhau:", probability_b)
    print("c) Chỉ có hai viên cùng màu:", probability_c)
    print("d) Được 2 bi đỏ và 1 bi trắng:", probability_d)
    print("e) Có 3 viên bi trắng:", probability_e)

ball_experiment_probability(100)