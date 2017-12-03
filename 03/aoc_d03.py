def calc(target):
    ring = 1
    n = 1

    square = 1

    while square < target:
        ring += 1
        n += 2
        square = n * n

    # print(ring)
    # print(n)
    # print(square)


    right = square
    left = square - n + 1

    if left <= target <= right:

        mid = (right + left) / 2.0
        # print(mid)

        distance_to_mid = target - mid
        # print(distance_to_mid)

        distance_to_one = distance_to_mid + ring - 1
        # print(distance_to_one)
        return distance_to_one

    else:

        top_left = left - n + 1
        if top_left <= target <= left:
            mid = (top_left + left) / 2.0
            # print(mid)

            distance_to_mid = target - mid
            # print(distance_to_mid)

            distance_to_one = distance_to_mid + ring - 1
            # print(distance_to_one)
            return distance_to_one

        else:
            top_right = top_left - n + 1

            if top_right <= target <= top_left:
                mid = (top_left + top_right) / 2.0
                # print(mid)

                distance_to_mid = target - mid
                # print(distance_to_mid)

                distance_to_one = distance_to_mid + ring - 1
                # print(distance_to_one)
                return distance_to_one

            else:
                bottom_right = top_right - n + 1

                if bottom_right <= target <= top_right:
                    mid = (top_right + bottom_right) / 2.0
                    # print(mid)

                    distance_to_mid = target - mid
                    # print(distance_to_mid)

                    distance_to_one = distance_to_mid + ring - 1
                    # print(distance_to_one)
                    return distance_to_one

                else:
                    raise


if __name__ == '__main__':
    print(calc(12))
    print(calc(23))
    print(calc(1024))
    print(calc(265149))
