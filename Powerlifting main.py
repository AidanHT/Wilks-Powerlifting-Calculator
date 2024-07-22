import csv 
import supporting_file as sfile
import PowerliftingScoreClass as p

def create_pl_object(filename):

    collection_lifters = sfile.CollectionObjects()

    with open(filename, "r", encoding='utf-8', errors = 'ignore') as file_in:   
        reader = csv.reader(file_in)

        file_in.readline()

        for line in reader:
            if line[4] != "":
                name = line[1]
                sex = line[2]
                equipment = line[3]
                age = float(line[4])
                bw = float(line[5])
                squat = float(line[6])
                dl = float(line[7])

                newPowerlifter = p.PowerliftingScore(name, sex, equipment, age, bw, squat, dl)
                collection_lifters.add_object(newPowerlifter, name)

    return collection_lifters

def writeTestCases(filename):

    with open(filename, 'w', encoding='utf-8') as pointer:

        s = ""

        powerLifter1 = p.PowerliftingScore("Jennifer Thompson","F","Raw",37.0,59.76,140.0,175.0)
        powerLifter2 = p.PowerliftingScore("Vasiliy Omelchenko","M","Single-ply",35.5,120.05,400.0,355.0)
        powerLifter3 = p.PowerliftingScore("Hana McFarlane","F","Wraps",16.5, 50.0, 60.0, 80.0)

        testCase = callAllTestsCases(powerLifter1, powerLifter2, powerLifter3)

        pointer.write(testCase)

def callAllTestsCases(powerLifter1, powerLifter2, powerLifter3):
        
        s = ""

        s += informalStringTestCase(powerLifter1, powerLifter2, powerLifter3)
        s += formalStringTestCase(powerLifter1, powerLifter2, powerLifter3)
        s += valuationTestCase(powerLifter1, powerLifter2, powerLifter3)
        s += gtLtTestCase(powerLifter1, powerLifter2, powerLifter3)
        s += geLeTestCase(powerLifter1, powerLifter2, powerLifter3)
        s += equalityTestCase(powerLifter1, powerLifter2, powerLifter3)
        s += divisionTestCase(powerLifter1, powerLifter2, powerLifter3)
        s += sumTestCase(powerLifter1, powerLifter2, powerLifter3)
        s += differenceTestCase(powerLifter1, powerLifter2, powerLifter3)

        return s
        
def informalStringTestCase(powerLifter1, powerLifter2, powerLifter3):

    s = ""

    s += f'Test Case 1 - Powerlifter Object Informal String Representation Accuracy\n'
        
    s += str(str(powerLifter1) == f'Jennifer Thompson\n * Sex: F\n * Age: 37.0 years\n * Bodyweight: 59.76kg\n * Squat: 140.0kg\n * Deadlift: 175.0kg\n * Equipment: Raw') + '\n'
    s += str(str(powerLifter2) == f'Vasiliy Omelchenko\n * Sex: M\n * Age: 35.5 years\n * Bodyweight: 120.05kg\n * Squat: 400.0kg\n * Deadlift: 355.0kg\n * Equipment: Single-ply') + '\n'
    s += str(str(powerLifter3) == f'Hana McFarlane\n * Sex: F\n * Age: 16.5 years\n * Bodyweight: 50.0kg\n * Squat: 60.0kg\n * Deadlift: 80.0kg\n * Equipment: Wraps') + '\n'
  
    s += str((str(powerLifter1) == f'Vasiliy Omelchenko\n * Sex: M\n * Age: 35.5 years\n * Bodyweight: 120.05kg\n * Squat: 400.0kg\n * Deadlift: 355.0kg\n * Equipment: Single-ply') == False) + '\n'
    s += str((str(powerLifter2) == f'Jennifer Thompson\n * Sex: F\n * Age: 37.0 years\n * Bodyweight: 59.76kg\n * Squat: 140.0kg\n * Deadlift: 175.0kg\n * Equipment: Raw') == False) + '\n'
    s += str((str(powerLifter3) == f'Jennifer Thompson\n * Sex: F\n * Age: 37.0 years\n * Bodyweight: 59.76kg\n * Squat: 140.0kg\n * Deadlift: 175.0kg\n * Equipment: Raw') == False) + '\n'

    return s 

def formalStringTestCase(powerLifter1, powerLifter2, powerLifter3):

    s = ""

    s += f'\nTest Case 2 - Powerlifter Object Formal String Representation Accuracy\n'
    s+= str(powerLifter1.__repr__() == f'PowerliftingScore(Name = Jennifer Thompson, Sex = F, Age = 37.0, Bodyweight = 59.76, Squat = 140.0, Deadlift = 175.0, Equipment = Raw)') + '\n'
    s+= str(powerLifter2.__repr__() == f'PowerliftingScore(Name = Vasiliy Omelchenko, Sex = M, Age = 35.5, Bodyweight = 120.05, Squat = 400.0, Deadlift = 355.0, Equipment = Single-ply)') + '\n'
    s+= str(powerLifter3.__repr__() == f'PowerliftingScore(Name = Hana McFarlane, Sex = F, Age = 16.5, Bodyweight = 50.0, Squat = 60.0, Deadlift = 80.0, Equipment = Wraps)') + '\n'

    s+= str((powerLifter2.__repr__() == f'PowerliftingScore(Name = Jennifer Thompson, Sex = F, Age = 37.0, Bodyweight = 59.76, Squat = 140.0, Deadlift = 175.0, Equipment = Raw)') == False) + '\n'
    s+= str((powerLifter1.__repr__() == f'PowerliftingScore(Name = Vasiliy Omelchenko, Sex = M, Age = 35.5, Bodyweight = 120.05, Squat = 400.0, Deadlift = 355.0, Equipment = Single-ply)') == False) + '\n'
    s+= str((powerLifter3.__repr__() == f'PowerliftingScore(Name = Vasiliy Omelchenko, Sex = M, Age = 35.5, Bodyweight = 120.05, Squat = 400.0, Deadlift = 355.0, Equipment = Single-ply)') == False) + '\n'

    return s

def valuationTestCase(powerLifter1, powerLifter2, powerLifter3):

    s = ""

    s+= f'\nTest Case 3 - Powerlifter Object Valuation Accuracy\n'
        
    s+= str(powerLifter1.value() == 535.15) + '\n'
    s+= str(powerLifter2.value() == 637.38) + '\n'
    s+= str(powerLifter3.value() == 324.46) + '\n'
        
    s+= str((powerLifter1.value() == "535,15") == False) + '\n'
    s+= str((powerLifter2.value() == 637.39) == False) + '\n'
    s+= str((powerLifter3.value() == 324.4) == False) + '\n'

    return s

def gtLtTestCase(powerLifter1, powerLifter2, powerLifter3):
        
    s = ""

    s+= f'\nTest Case 4 - Comparing Powerlifter Object Values using Greater Than and Less Than Operators\n'

    s+= str(powerLifter1 < powerLifter2) + '\n'
    s+= str((powerLifter1 > powerLifter2) == False) + '\n'
    s+= str(powerLifter3 < powerLifter1) + '\n'

    return s

def geLeTestCase(powerLifter1, powerLifter2, powerLifter3):

    s = ""        

    s += f'\nTest Case 5 - Comparing Powerlifter Object Values using Greater Than and Equal To and Less Than and Equal Than Operators\n'

    s+= str(powerLifter1 <= powerLifter2) + '\n'
    s+= str((powerLifter1 >= powerLifter2) == False) + '\n'
    s+= str(powerLifter3 <= powerLifter1) + '\n'
        
    s+= str(powerLifter1 >= powerLifter1) + '\n'
    s+= str(powerLifter2 <= powerLifter2) + '\n'    
    s+= str(powerLifter3 >= powerLifter3) + '\n'

    return s     

def equalityTestCase(powerLifter1, powerLifter2, powerLifter3):
        
    s = ""

    s+= f'\nTest Case 6 - Equality Between Powerlifter Object Values\n'
        
    s+= str(powerLifter1 == powerLifter1) + '\n'
    s+= str((powerLifter1 == powerLifter2) == False) + '\n'

    s+= str(powerLifter2 != powerLifter3) + '\n'
    s+= str((powerLifter3 != powerLifter3) == False) + '\n'

    return s

def divisionTestCase(powerLifter1, powerLifter2, powerLifter3):
        
    s = ""

    s += f'\nTest Case 7 - Ratio between Powerlifter Object Values\n'
    s+= str(powerLifter1 / powerLifter2 == 0.84) + '\n'
    s+= str(powerLifter2 / powerLifter3 == 1.964) + '\n'
    s+= str(powerLifter3 / powerLifter1 == 0.606) + '\n'

    s+= str((powerLifter2 / powerLifter1 == 0.84) == False) + '\n'
    s+= str((powerLifter3 / powerLifter2 == 1.964) == False) + '\n'
    s+= str((powerLifter1 / powerLifter3 == 0.606) == False)+ '\n'

    return s

def sumTestCase(powerLifter1, powerLifter2, powerLifter3):
     
    s = ""

    s += f'\nTest Case 8 - Sum between Powerlifter Object \n'

    s+= str(powerLifter1 + powerLifter2 == 1172.53) + '\n'
    s+= str(powerLifter2 + powerLifter3 == 961.84) + '\n'
    s+= str(powerLifter3 + powerLifter1 == 859.61) + '\n'

    s+= str((powerLifter1 + powerLifter2 == 961.84) == False)+ '\n'
    s+= str((powerLifter2 + powerLifter3 == 859.61) == False)+ '\n'
    s+= str((powerLifter3 + powerLifter1 == 1172.53) == False)+ '\n'

    return s

def differenceTestCase(powerLifter1, powerLifter2, powerLifter3):
     
    s = ""

    s += f'\nTest Case 9 - Difference between Powerlifter Object Values\n'

    s+= str(powerLifter1 - powerLifter2 == -102.23) + '\n'
    s+= str(powerLifter2 - powerLifter3 == 312.92) + '\n'
    s+= str(powerLifter3 - powerLifter1 == -210.69) + '\n'

    s+= str((powerLifter1 + powerLifter2 == -210.69) == False)+ '\n'
    s+= str((powerLifter1 + powerLifter2 == -102.23) == False)+ '\n'
    s+= str((powerLifter1 + powerLifter2 == 312.92) == False)+ '\n'

    return s

def main():
    powerlifting_data = create_pl_object('Power Lifting Competition Data.csv')

    writeTestCases('PowerliftingTestCases.txt')

#MAIN
main()

