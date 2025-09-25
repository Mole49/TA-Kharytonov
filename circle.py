import math
import msvcrt

R = float(input("Enter circle radius R: "))

if R < 0:
    print("R не може бути від'ємним")
else:
    L = 2 * math.pi * R
    S = math.pi * R**2
    print(f"Length of circle: {L:.2f}")
    print(f"Area of circle: {S:.2f}")

print("\nPress any key to exit...")
msvcrt.getch()

