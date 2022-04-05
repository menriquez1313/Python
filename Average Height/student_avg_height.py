student_add = 0 

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  # 🚨 Don't change the code above 👆
  #Write your code below this row 👇
  
  student_add += student_heights[n]

#print(student_add) test
  
n += 1 #Does not account for the first loop so add 1
student_avg = student_add / n
print(round(student_avg))