#!/usr/bin/env python3

def main():
    with open("../input.txt") as input:
        datas = [x.replace("\n", "") for x in input.readlines()]

    print("========== part1 ==========")
    for stream in datas:
        for idx, packet in enumerate(stream):
            # start of packet marker is 4 unique chars
            if idx <= 2:
                continue
            else:
                total_packet = []
                total_packet.append(packet)
                total_packet.append(stream[idx-1])
                total_packet.append(stream[idx-2])
                total_packet.append(stream[idx-3])
                if (len(set(total_packet)) == 4):
                    print(f"Packet: {idx+1} {total_packet[::-1]}")
                    break

    print("========== part2 ==========")
    for stream in datas:
        for idx, packet in enumerate(stream):
            # start of message marker is 14 unique chars
            if idx <= 12:
                continue
            else:
                total_packet = []
                total_packet.append(packet)
                total_packet.append(stream[idx-1])
                total_packet.append(stream[idx-2])
                total_packet.append(stream[idx-3])
                total_packet.append(stream[idx-4])
                total_packet.append(stream[idx-5])
                total_packet.append(stream[idx-6])
                total_packet.append(stream[idx-7])
                total_packet.append(stream[idx-8])
                total_packet.append(stream[idx-9])
                total_packet.append(stream[idx-10])
                total_packet.append(stream[idx-11])
                total_packet.append(stream[idx-12])
                total_packet.append(stream[idx-13])
                if (len(set(total_packet)) == 14):
                    print(f"Packet: {idx+1} {total_packet[::-1]}")
                    break


if __name__ == "__main__":
    main()