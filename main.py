text = input("Ievadi tekstu: " ) #Lūdzam lietotājam ievadīt tekstu
def deleteCombo(text): #arguments = teksts
  if text.count("abc")>0: #pārbaudām, vai ir kada kombinācija "abc"
    text = text.replace("abc","") #aizvietojam "abc" ar ""
  else: #pretējā gadījumā
    text = "Meklējamā kombonācija netika atrasta!" #aizvietojam tekstu ar paziņojumu
  print(text) #printējam rezultātu
  return text #atgriežam vertību
deleteCombo(text) #Izsaucam funkciju