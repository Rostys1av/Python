# while loop, do somwthing until conditin exists

bench_press_reps = 10
while bench_press_reps > 0: #As long as condition is True
    print("Rep " + "{}".format(bench_press_reps))
    bench_press_reps -= 1 # - 1 each time
print("rest!")