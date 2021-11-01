r1 = int(input('Persons in 1st class? '))
r2 = int(input('Persons in 2nd class?  '))
r3 = int(input('Persons in 3rd class? '))

q1 = (r1 // 2) + (r1 % 2)
q2 = (r2 // 2) + (r2 % 2)
q3 = (r3 // 2) + (r3 % 2)

q_total = q1 + q2 + q3

print('Desk q-ty ', q_total, ' pcs.')
