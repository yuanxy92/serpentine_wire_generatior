import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def draw_connected_lines_and_arcs(line_lengths, arc_angles, line_widths, arc_radii):
    fig, ax = plt.subplots()
    current_x = 0
    current_y = 0

    for length, angle, width, radius in zip(line_lengths, arc_angles, line_widths, arc_radii):
        # Draw a line
        end_x = current_x + length
        end_y = current_y
        ax.plot([current_x, end_x], [current_y, end_y], linewidth=width)

        # Draw an arc
        arc = Arc((current_x, current_y), 2 * radius, 2 * radius, angle=0, theta1=0, theta2=angle, linewidth=width)
        ax.add_patch(arc)

        # Update current position
        current_x = end_x
        current_y = end_y

    ax.set_aspect('equal')
    plt.show()

def draw_line(ax, start_point, direction_angle, line_length, line_width):
    current_x = start_point[0]
    current_y = start_point[1]
    direction_angle_arc = direction_angle / 180 * math.pi
    dx = line_length * math.cos(direction_angle_arc)
    dy = line_length * math.sin(direction_angle_arc)
    ax.plot([current_x, current_x + dx], [current_y, current_y + dy], linewidth=line_width, color='#FFD700')
    return [current_x + dx, current_y + dy, direction_angle]

def draw_arc(ax, start_point, direction_angle, arc_angle, radius, line_width):
    current_x = start_point[0]
    current_y = start_point[1]
    direction_angle_arc = direction_angle / 180 * math.pi
    arc_angle_arc = arc_angle / 180 * math.pi
    # calculate center x,y position
    if direction_angle > 0:
        direction_angle_arc_to_center = - (math.pi / 2 - direction_angle_arc)
    else:
        direction_angle_arc_to_center = math.pi / 2 + direction_angle_arc
    dx = radius * math.cos(direction_angle_arc_to_center)
    dy = radius * math.sin(direction_angle_arc_to_center)
    center_x = current_x + dx
    center_y = current_y + dy
    # calculate arc parameters
    if direction_angle > 0:
        theta1 = (180 - arc_angle) / 2
        theta2 = theta1 + arc_angle
    else:
        theta2 = -(180 - arc_angle) / 2
        theta1 = theta2 - arc_angle
    arc = Arc((center_x, center_y), 2 * radius, 2 * radius, angle=theta1, theta1=0, theta2=arc_angle, linewidth=line_width, color='#FFD700')
    ax.add_patch(arc)
    # calculate end point
    if direction_angle > 0:
        direction_angle_arc_to_end = math.pi / 2 - direction_angle_arc
    else:
        direction_angle_arc_to_end = -(math.pi / 2 + direction_angle_arc)
    dx2end = radius * math.cos(direction_angle_arc_to_end)
    dy2end = radius * math.sin(direction_angle_arc_to_end)
    end_x = center_x + dx2end
    end_y = center_y + dy2end
    return [end_x, end_y, -direction_angle]


# Start point
start_point = [0, 0]
# arc angle in degrees
arc_angle = 180
direction_angle0 = arc_angle / 2
line_width = 3
line_length = 4
radius = 2
gap = 0.4

fig, ax = plt.subplots()

# for i in range(4):
#     [current_x, current_y, direction_angle] = draw_line(ax, [current_x, current_y], direction_angle, line_length, line_width)
#     print([current_x, current_y, direction_angle])
#     [current_x, current_y, direction_angle] = draw_arc(ax, [current_x, current_y], direction_angle, arc_angle, radius, line_width)
#     print([current_x, current_y, direction_angle])

scale_factor = [0, 1, -1]
scale_factor = [0]
for scale in scale_factor:
    current_x = start_point[0]
    current_y = start_point[1]
    direction_angle = direction_angle0
    direction_angle_arc = direction_angle / 180 * math.pi
    direction_angle_arc_shift = - (math.pi / 2 - direction_angle_arc)
    dx = scale * gap * math.cos(direction_angle_arc_shift)
    dy = scale * gap * math.sin(direction_angle_arc_shift)
    current_x = current_x + dx
    current_y = current_y + dy

    for i in range(12):
        # 1
        [current_x, current_y, direction_angle] = draw_line(ax, [current_x, current_y], direction_angle, line_length, line_width)
        print([current_x, current_y, direction_angle])
        [current_x, current_y, direction_angle] = draw_arc(ax, [current_x, current_y], direction_angle, arc_angle, radius - gap * scale, line_width)
        print([current_x, current_y, direction_angle])
        # 2
        [current_x, current_y, direction_angle] = draw_line(ax, [current_x, current_y], direction_angle, line_length, line_width)
        print([current_x, current_y, direction_angle])
        [current_x, current_y, direction_angle] = draw_arc(ax, [current_x, current_y], direction_angle, arc_angle, radius + gap * scale, line_width)
        print([current_x, current_y, direction_angle])

ax.set_aspect('equal')
# Set the x and y ranges
plt.xlim(-1, 100)  # Set the x range from 1 to 5
plt.ylim(-5, 7.5)  # Set the y range from 0 to 12
plt.show()

a=1




