import matplotlib.pyplot as plt
import csv

# parameter
x = 0.1
v = 0.0
t = 0.0

k = 0.2
c = 0.1
m = 1.0

dt = 0.1

# graph data array
gt = []
gx = []
gv = []

# csv file
outfile = open('output.csv','w', newline='')
writer = csv.writer(outfile)
writer.writerow(['i', 't', 'x', 'v'])

# time loop
for i in range(1000):
    fx = v
    fv = (-k * x - c * v) / m
    x = x + dt * fx
    v = v + dt * fv
    t = t + dt

    print('i: {0:4d}, t: {1:6.2f}, x: {2:9.6f}, v: {3:9.6f}'.format(i, t, x, v))

    gt.append(t)
    gx.append(x)
    gv.append(v)

    writer.writerow([i, t, x, v])

outfile.close()

# graph plot
plt.subplot(2,1,1)
plt.plot(gt, gx)
plt.ylabel('x')
plt.legend(['x'])
plt.grid()

plt.subplot(2,1,2)
plt.plot(gt, gv)
plt.xlabel('Time')
plt.ylabel('v')
plt.legend(['v'])
plt.grid()

plt.show()