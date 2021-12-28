x1 = int(input('Give the x value of vector u'))
y1 = int(input('Give the y value of vector u'))
x2 = int(input('Give the x value of vector v'))
y2 = int(input('Give the y value of vector v'))

#formula: u*v = x1*x2 + y1*y2
inner_product_x = x1*x2
inner_product_y = y1*y2
sum_inner_product = inner_product_x + inner_product_y

print(f'The inner product of vector u and v is: u*v = {sum_inner_product}')
