

def sortScore(students):
  copied = students.copy()
  for i in range(len(copied) - 1):
    for j in range(i + 1, len(copied)):
      if copied[i]["score"] < copied[j]["score"]:
        temp = copied[i]
        copied[i] = copied[j]
        copied[j] = temp

  for item in copied:
    print(item["name"], '-', item["score"], item["grade"])


def calc_avg(students):
  sum = 0
  for student in students:
    sum += student["score"]

  return sum / len(students)

def show_above_avg(students, avg):
  print("Siswa di atas rata2:")
  for student in students:
    if student["score"] > avg:
      print(student["name"], " ")

def grade(score):
  if score >= 85 and score <= 100:
    return '(A)'
  elif score >= 70 and score <= 84:
    return '(B)' 
  elif score >= 60 and score <= 69:
    return '(C)'
  else:
    return '(D)'
  
def add_grade(students):
  for student in students:
    student["grade"] = grade(student["score"])


if __name__ == "__main__":
  students = [
    { "name": "Andi", "score": 85 },
    { "name": "Budi", "score": 72 },
    { "name": "Cici", "score": 90 },
    { "name": "Doni", "score": 60 },
    { "name": "Eka", "score": 75 },
  ]

  add_grade(students)
  sortScore(students)
  avg = calc_avg(students)
  print("nilai rata2: ", avg)
  show_above_avg(students, avg)
  
  

