import math


def angle(point, antenna):
    """Angle of a ray from antenna to point in degrees [0, 360)."""
    x = point[0] - antenna[0]
    y = point[1] - antenna[1]
    return math.degrees(math.atan2(y, x)) % 360


def reflect_point(point, a, b):
    """Reflect point across the line through a and b."""
    px, py = point
    ax, ay = a
    bx, by = b

    vx = bx - ax
    vy = by - ay

    t = ((px - ax) * vx + (py - ay) * vy) / (vx * vx + vy * vy)

    proj_x = ax + t * vx
    proj_y = ay + t * vy

    return (
        2 * proj_x - px,
        2 * proj_y - py,
    )


def main():
    # Antenna
    A = (20, 20)

    # Building B
    B1 = (80, 160)
    B2 = (95, 180)
    B3 = (175, 120)
    B4 = (160, 100)

    # Building A: the relevant reflecting facade edge
    A1 = (-40, 100)
    A2 = (0, 200)

    # 1. Directions blocked directly by absorbing building B.
    direct_left = angle(B4, A)
    direct_right = angle(B1, A)
    direct_blocked = direct_right - direct_left

    # 2. Directions that hit reflecting building A and then B.
    #
    # Reflect B across the reflecting edge A1-A2.
    reflected_B2 = reflect_point(B2, A1, A2)

    reflected_boundary = angle(reflected_B2, A)
    building_A_boundary = angle(A1, A)

    reflected_blocked = building_A_boundary - reflected_boundary

    blocked_angle = direct_blocked + reflected_blocked
    answer = blocked_angle / 360 * 100

    print(f"{answer:.2f}")


if __name__ == "__main__":
    main()
