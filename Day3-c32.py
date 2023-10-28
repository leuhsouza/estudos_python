height = float(input('Digite seu peso: '))
weight = int(input('Digite sua altura: '))

bmi = (weight/(height**2))


if bmi <= 18.5:
  print(f'Your Bmi is {bmi:.2f}, you are underweight.')

else :
    print(f"Your bmi is {bmi:.2f}")



    """Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.
"""

"""Your BMI is 18.28678, you are underweight."
"Your BMI is 22.0, you have a normal weight."
"Your BMI is 28.50752, you are slightly overweight."
"Your BMI is 32.56189, you are obese."
"Your BMI is 37.50000, you are clinically obese."""