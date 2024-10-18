import matplotlib.pyplot as plt

Φ = (1 + (5 ** (1 / 2))) / 2

X_square = []
Y_square = []

points = [
    [Φ, Φ],
    [Φ, Φ * 2],
    [Φ * 2, Φ * 2],
    [Φ * 2, Φ],
]
for pair in points:
    X_square.append(pair[0])
    Y_square.append(pair[1])
X_square.append(points[0][0])
Y_square.append(points[0][1])

X_rectangle = []
Y_rectangle = []

points = [
    [Φ - (1 / 2), Φ + ((Φ - 1) / 2)],
    [Φ - (1 / 2), Φ * 2 - ((Φ - 1) / 2)],
    [Φ * 2 + (1 / 2), Φ * 2 - ((Φ - 1) / 2)],
    [Φ * 2 + (1 / 2), Φ + ((Φ - 1) / 2)],
]
for pair in points:
    X_rectangle.append(pair[0])
    Y_rectangle.append(pair[1])
X_rectangle.append(points[0][0])
Y_rectangle.append(points[0][1])

Z_wall = [0, 0, 0, 0, 0]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d", proj_type="ortho")
ax.set_box_aspect(aspect=(1, 1, 1))

ax.plot(X_square, Y_square, Z_wall, c="red")
ax.plot(Z_wall, X_square, Y_square, c="blue")
ax.plot(Y_square, Z_wall, X_square, c="green")

ax.plot(X_rectangle, Y_rectangle, Z_wall, c="red")
ax.plot(Z_wall, X_rectangle, Y_rectangle, c="blue")
ax.plot(Y_rectangle, Z_wall, X_rectangle, c="green")

ax.plot(
    [Φ, Φ * 1.5, Φ * 2],
    [X_square[0], X_rectangle[0], X_square[0]],
    [Y_square[0], Y_rectangle[0], Y_square[0]],
    c="k",
)
ax.plot(2 * [Φ * 1.5], X_rectangle[0:2], Y_rectangle[0:2], c="k")
ax.plot(
    [Φ, Φ * 1.5, Φ * 2],
    [X_square[1], X_rectangle[1], X_square[1]],
    [Y_square[1], Y_rectangle[1], Y_square[1]],
    c="k",
)
ax.plot(
    [Φ, Φ * 1.5, Φ * 2],
    [X_square[2], X_rectangle[2], X_square[2]],
    [Y_square[2], Y_rectangle[2], Y_square[2]],
    c="k",
)
ax.plot(2 * [Φ * 1.5], X_rectangle[2:4], Y_rectangle[2:4], c="k")
ax.plot(
    [Φ, Φ * 1.5, Φ * 2],
    [X_square[3], X_rectangle[3], X_square[3]],
    [Y_square[3], Y_rectangle[3], Y_square[3]],
    c="k",
)

ax.plot(
    [X_square[0], X_rectangle[0], X_square[0]],
    [Y_square[0], Y_rectangle[0], Y_square[0]],
    [Φ, Φ * 1.5, Φ * 2],
    c="k",
)
ax.plot(X_rectangle[0:2], Y_rectangle[0:2], 2 * [Φ * 1.5], c="k")
ax.plot(
    [X_square[1], X_rectangle[1], X_square[1]],
    [Y_square[1], Y_rectangle[1], Y_square[1]],
    [Φ, Φ * 1.5, Φ * 2],
    c="k",
)
ax.plot(
    [X_square[2], X_rectangle[2], X_square[2]],
    [Y_square[2], Y_rectangle[2], Y_square[2]],
    [Φ, Φ * 1.5, Φ * 2],
    c="k",
)
ax.plot(X_rectangle[2:4], Y_rectangle[2:4], 2 * [Φ * 1.5], c="k")
ax.plot(
    [X_square[3], X_rectangle[3], X_square[3]],
    [Y_square[3], Y_rectangle[3], Y_square[3]],
    [Φ, Φ * 1.5, Φ * 2],
    c="k",
)

ax.plot(
    [Y_square[0], Y_rectangle[0], Y_square[0]],
    [Φ, Φ * 1.5, Φ * 2],
    [X_square[0], X_rectangle[0], X_square[0]],
    c="k",
)
ax.plot(Y_rectangle[0:2], 2 * [Φ * 1.5], X_rectangle[0:2], c="k")
ax.plot(
    [Y_square[1], Y_rectangle[1], Y_square[1]],
    [Φ, Φ * 1.5, Φ * 2],
    [X_square[1], X_rectangle[1], X_square[1]],
    c="k",
)
ax.plot(
    [Y_square[2], Y_rectangle[2], Y_square[2]],
    [Φ, Φ * 1.5, Φ * 2],
    [X_square[2], X_rectangle[2], X_square[2]],
    c="k",
)
ax.plot(Y_rectangle[2:4], 2 * [Φ * 1.5], X_rectangle[2:4], c="k")
ax.plot(
    [Y_square[3], Y_rectangle[3], Y_square[3]],
    [Φ, Φ * 1.5, Φ * 2],
    [X_square[3], X_rectangle[3], X_square[3]],
    c="k",
)

scale_factor = 0.5
X_cube = []
Y_cube = []
Z_cube = []
points = [
    [Φ * 2.5 * scale_factor, Φ * 2.5 * scale_factor, Φ * 2.5 * scale_factor],
    [Φ * 2.5 * scale_factor, Φ * 3.5 * scale_factor, Φ * 2.5 * scale_factor],
    [Φ * 3.5 * scale_factor, Φ * 3.5 * scale_factor, Φ * 2.5 * scale_factor],
    [Φ * 3.5 * scale_factor, Φ * 2.5 * scale_factor, Φ * 2.5 * scale_factor],
    [Φ * 2.5 * scale_factor, Φ * 2.5 * scale_factor, Φ * 3.5 * scale_factor],
    [Φ * 2.5 * scale_factor, Φ * 3.5 * scale_factor, Φ * 3.5 * scale_factor],
    [Φ * 3.5 * scale_factor, Φ * 3.5 * scale_factor, Φ * 3.5 * scale_factor],
    [Φ * 3.5 * scale_factor, Φ * 2.5 * scale_factor, Φ * 3.5 * scale_factor],
]
for pair in points:
    X_cube.append(pair[0])
    Y_cube.append(pair[1])
    Z_cube.append(pair[2])

ax.set_box_aspect(aspect=(1, 1, 1))

ax.plot([X_cube[0], X_cube[1]], [Y_cube[0], Y_cube[1]], [Z_cube[0], Z_cube[1]], c="gray")
ax.plot([X_cube[1], X_cube[2]], [Y_cube[1], Y_cube[2]], [Z_cube[1], Z_cube[2]], c="gray")
ax.plot([X_cube[2], X_cube[3]], [Y_cube[2], Y_cube[3]], [Z_cube[2], Z_cube[3]], c="gray")
ax.plot([X_cube[3], X_cube[0]], [Y_cube[3], Y_cube[0]], [Z_cube[3], Z_cube[0]], c="gray")

ax.plot([X_cube[4], X_cube[5]], [Y_cube[4], Y_cube[5]], [Z_cube[4], Z_cube[5]], c="gray")
ax.plot([X_cube[5], X_cube[6]], [Y_cube[5], Y_cube[6]], [Z_cube[5], Z_cube[6]], c="gray")
ax.plot([X_cube[6], X_cube[7]], [Y_cube[6], Y_cube[7]], [Z_cube[6], Z_cube[7]], c="gray")
ax.plot([X_cube[7], X_cube[4]], [Y_cube[7], Y_cube[4]], [Z_cube[7], Z_cube[4]], c="gray")

ax.plot([X_cube[0], X_cube[4]], [Y_cube[0], Y_cube[4]], [Z_cube[0], Z_cube[4]], c="gray")
ax.plot([X_cube[1], X_cube[5]], [Y_cube[1], Y_cube[5]], [Z_cube[1], Z_cube[5]], c="gray")
ax.plot([X_cube[2], X_cube[6]], [Y_cube[2], Y_cube[6]], [Z_cube[2], Z_cube[6]], c="gray")
ax.plot([X_cube[3], X_cube[7]], [Y_cube[3], Y_cube[7]], [Z_cube[3], Z_cube[7]], c="gray")

ax.set_box_aspect(aspect=(1, 1, 1))
ax.view_init(elev=35, azim=45)
plt.tight_layout()
plt.axis("off")
plt.show()
