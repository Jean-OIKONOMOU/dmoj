infectedQuota = int(input())
patientZero = int(input())
infectedPerDay = int(input())

days = 0
totalInfected = patientZero

while totalInfected <= infectedQuota:  
    patientZero = patientZero * infectedPerDay
    totalInfected = totalInfected + patientZero
    days = days + 1
    
print(days)



