def calculate_lrc(data):
    lrc = 0
    for row in data:
        row_parity = sum(row) % 2
        lrc ^= row_parity
    return lrc

def calculate_vrc(data):
    vrc = [0] * len(data[0])
    for row in data:
        for i, bit in enumerate(row):
            vrc[i] ^= bit
    return vrc

def main():
    data = [
        [1, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 0, 0]
    ]

    lrc = calculate_lrc(data)
    vrc = calculate_vrc(data)

    print("Original Data:")
    for row in data:
        print(row)

    print("LRC: ", lrc)
    print("VRC: ", vrc)

    print("Transmitted Data:")
    for row in data:
        row.append(lrc)
        print(row)
    vrc_parity = [bit for bit in vrc]
    vrc_parity.append(sum(vrc) % 2)
    print(vrc_parity)


main()
