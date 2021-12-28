inch_to_mm = 25.4

height_US = 8.5
lenght_US = 11

height_in_mm = height_US*inch_to_mm
lenght_in_mm = lenght_US*inch_to_mm

print(f'The height of american briefpaper is {height_in_mm}mm, and the lenght is {lenght_in_mm}mm.')
# afronden
print(f'The height of american briefpaper is {round(height_in_mm, 2)}mm, and the lenght is {round(lenght_in_mm, 2)}mm.')
