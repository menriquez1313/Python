# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
#print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
  if n == 0:
    a = student_scores[n]
  elif n > 0: 
    b = student_scores[n]
    if a > b:
      #print("a is greater") #test line
      a = a #keep 
    else:
      #print("b is greater.") #test line
      a = b
  else:
    print("ERROR")
    
print(a)