import random

bases = ["A", "T", "C", "G"]

standart = random.choices(bases, k = 20)

dna = {key: [val, ("T" if val == "A" else "A" if val == "T" else "C" if val == "G" else "G")] for (key, val) in enumerate(standart, 1)}
print(f"Dna is {dna}")

