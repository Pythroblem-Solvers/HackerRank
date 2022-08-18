def run(students=None):

    if students is None:
        
        students = [["Harry", 37.21],
                    ["Berry", 37.21],
                    ["Tina", 37.2],
                    ["Akriti", 41],
                    ["Harsh", 39]]

    # Calificación de los estudiantes en una lista
    scores = [score[1] for score in students]

    # Minima calificacion de la lista
    minim = min(scores)

    # Eliminando el minimo de la lista
    scores.remove(minim)

    # Obteniendo ahora el nuevo minimo que es en realidad el segundo puntaje mas bajo
    minim_second = min(scores)

    # Lista con los nombres de los estudiantes con el segundo puntaje mas bajo
    stu_slg = [student[0] for student in students if student[1] == minim_second]
    # Ordenando alfabeticamente
    stu_slg.sort()
    # Longitud de la lista es el numero de estudiantes
    N = len(students)

    for student in stu_slg:
        print(student)

    # a = map(lambda student: print(student), stu_slg)
    # return a
if __name__ == "__main__":

    #students = []
    #for _ in range(int(input())):
    #    name = input()
    #    score = float(input())
    #    students.append([name, score])

    run()

