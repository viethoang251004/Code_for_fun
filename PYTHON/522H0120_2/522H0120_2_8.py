import math

white_balls = 8
blue_balls = 6
red_balls = 9

total_balls_selected = 6

probability = (math.comb(white_balls, 2) * math.comb(blue_balls, 2) * math.comb(red_balls, 2)) / math.comb(white_balls + blue_balls + red_balls, total_balls_selected)

print("Probability:", probability)
