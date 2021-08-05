from numpy import exp, array, random, dot, square, sin, pi, tanh

random.seed(1)

original_input = random.uniform(low = -2 * pi, high = 2 * pi, size = 1000)
original_output = sin(original_input)

weight = 2 * random.random() - 1

for i in range(20000):
	output = tanh(dot(original_input, weight))
	d_output = 1 - square(output)
	error = original_output - output
	weight += dot(original_input, error * d_output) * 0.002

print("45° ", tanh(pi/4 * weight), " ≈ ", 0.707)
print("60° ", tanh(pi/3 * weight), " ≈ ", 0.866)
print("90° ", tanh(pi/2 * weight), " ≈ ", 1.0)
print("30° ", tanh(pi/6 * weight), " ≈ ", 0.5)
print("20° ", tanh(pi/9 * weight), " ≈ ", 0.342)
print("180° ", tanh(pi * weight), " ≈ ", 0.0) ### it's supposed to  be near zero
