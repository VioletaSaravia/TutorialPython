with open("base.txt", "w") as base:
	for note in range(128):
		base.write(f'{note}, 0;\n')