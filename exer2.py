from datetime import datetime
print("******** Idade em dias, horas e segundos ********")

years = int(input("Digite sua idade em anos: "))

yearsInDays = (years * 365)
now = datetime.now()
mouthsInDays = ((now.month) - 1) * 30
days = (now.day) - 1
yearsInDays += mouthsInDays + days

print(
      yearsInDays,"dias \n",
      now.hour, "horas \n",
      now.minute,"minutos \n",
      now.second," segundos"
)