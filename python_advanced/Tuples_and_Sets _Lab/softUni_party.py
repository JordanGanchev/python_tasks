# number_of_guests = int(input())
#
# set_vip = set()
# set_regular = set()
#
# for _ in range(number_of_guests):
#     reservation_code = input()
#     if reservation_code[0].isdigit():
#         set_vip.add(reservation_code)
#     else:
#         set_regular.add(reservation_code)
#
# while True:
#     reservation_code = input()
#     if reservation_code == 'END':
#         break
#     if reservation_code[0].isdigit():
#         if reservation_code in set_vip:
#             set_vip.remove(reservation_code)
#     else:
#         if reservation_code in set_regular:
#             set_regular.remove(reservation_code)
# number = len(set_vip) + len(set_regular)
# print(number)
#
#
# for i in set_vip:
#     print(i)
# for j in set_regular:
#     print(j)

def is_vip(guest):
    return guest[0].isdigit()


n = int(input())

vip = set()
regular = set()

for _ in range(n):
    reservation = input()
    if is_vip(reservation):
        vip.add(reservation)
    else:
        regular.add(reservation)

while True:
    guest = input()
    if guest == 'END':
        break
    if is_vip(guest):
        vip.remove(guest)
    else:
        regular.remove(guest)

print(len(vip) + len(regular))
[print(guest) for guest in sorted(vip)]
[print(guest) for guest in sorted(regular)]