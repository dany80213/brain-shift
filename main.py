import random
from generator import generate_trial
rng = random.Random(42)
trial_di_test = generate_trial(rng)
print(trial_di_test)