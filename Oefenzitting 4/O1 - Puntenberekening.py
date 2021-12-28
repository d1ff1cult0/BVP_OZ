"""
Een beginnende programmeur heeft een programmaatje geschreven dat als invoer
twee scores op 20 verwacht en hiervan het gemiddelde teruggeeft als procent.
Er zijn echter vier foutjes in de code geslopen. Gebruik de debugger om na te
gaan waar het misloopt. Corrigeer ook de fouten.
"""

grade1 = int(input('Grade /20: '))
grade2 = int(input('Grade /20: '))

grade_sum = grade1 + grade2
result_scale_100 = (grade_sum / 40)*100
result_string = f"Grade /100 = {result_scale_100}"
print(result_string)
