class Student:
    """ Создание студета """ 
    instances:list = [] #instances = [] не понятно почему но нерабоатет

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.instances.append(self)

    def __str__(self):
        """ Выводит на экран данные о студенте"""
        return f"""Имя: {self.name} \nФамилия: {self.surname}
Средняя оценка за домашние задания: {self.ave_score()}
Курсы в процессе изучения: {",".join(self.courses_in_progress)}
Завершенные курсы: {",".join(self.finished_courses)}
"""
    def ave_score(self):
        """ Метод подсчета среднего балла """
        sum_total = 0
        count = 0
        for value in self.grades.values():
            if isinstance(value,list):
                sum_total += sum(value[0])
                count += len(value[0])
        score = sum_total / count
        return round(score,1)

    def give_grades(self, lecturer, course, grade):
        """ Метод оценивание лектора """
        if isinstance(lecturer, Lecturer) and course in lecturer.course:
            if course in lecturer.grades :
                lecturer.grades[course] += [grade]
                return f'За лекции по предмету "{course}" поставлена "{grade}"'
            else:
                lecturer.grades[course] = [grade]
                return f'За лекции по предмету "{course}" поставлена "{grade}"'
        else:
            return 'Ошибка'

    def __eq__(self,other): #Магические методы сравнение среднего балла двух студентов
        return self.ave_score() == other.ave_score()
    def __ne__(self,other):
        return self.ave_score() != other.ave_score()
    def __it__(self,other):
        return self.ave_score() < other.ave_score()
    def __gt__(self,other):
        return self.ave_score() > other.ave_score()
    def __le__(self,other):
        return self.ave_score() <= other.ave_score()
    def __ge__(self,other):
        return self.ave_score() >= other.ave_score()
        

class Mentor:
    """ Создает ментора """
    instances:list = []
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        Mentor.instances.append(self)
        
        
class Lecturer(Mentor):
    """ Создает лектора """
    instances:list = []
    def __init__(self, name, surname, course):
        super().__init__(name, surname)
        self.course = course
        self.grades = {}
        Lecturer.instances.append(self)       

    def __str__(self):
        """ Выводит на экран данные о лекторе"""
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.ave_score()}'
        
    def ave_score(self):
        """ Метод подсчета среднего балла """
        sum_total = 0
        count = 0
        for valu in self.grades.values():
            if isinstance(valu,list):
                sum_total += sum(valu[0])
                count += len(valu[0])
        score = sum_total / count
        return round(score,1)
    
    def __eq__(self,other): #Магические методы сравнение среднего балла двух лекторов
        return self.ave_score() == other.ave_score()
    def __ne__(self,other):
        return self.ave_score() != other.ave_score()
    def __it__(self,other):
        return self.ave_score() < other.ave_score()
    def __gt__(self,other):
        return self.ave_score() > other.ave_score()
    def __le__(self,other):
        return self.ave_score() <= other.ave_score()
    def __ge__(self,other):
        return self.ave_score() >= other.ave_score()
        
       
class Reviewer(Mentor):
    """ Создает ментора """
    instances:list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        Reviewer.instances.append(self)

    def __str__(self):
        """ Выводит на экран данные о менторе """
        return f'Имя: {self.name} \nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        """ Метод оценивание студента """
        if isinstance(student, Student):
            if course in student.grades:
                student.grades[course] += [grade]
                return f'За домашнее заданее по предмету "{course}" поставлена "{grade}"'
            else:
                student.grades[course] = [grade]
                return f'За домашнее заданее по предмету "{course}" поставлена "{grade}"'
        else:
            return 'Ошибка'
        
st1 = Student("Павел","Тарасов","муж")
st2 = Student("Алина","Батищева","жен")

lt1 = Lecturer("Ирина","Петровна","OOP")
lt2 = Lecturer("Семен","Белов","Python")

re1 = Reviewer("Анна","Иванова")
re2 = Reviewer("Игорь","Ковалев")

#Класс ментора не создавал так как он все ровно безполезен

st1.give_grades(lt1,"OOP",[6,8,4])
st2.give_grades(lt1,"OOP",[7])


st1.give_grades(lt2,"Python",[7,8,9])
st2.give_grades(lt2,"Python",[4,5])
st1.give_grades(lt1,"Python",[5,1,4])

print(lt1)
print(lt2)

st1.finished_courses += ["Git"]
st1.courses_in_progress += ["Python"]
re1.rate_hw(st1,"Python",[9,9,9,5])
re1.rate_hw(st2,"Python",[8,6,7,5])
re1.rate_hw(st1,"OOP",[3,4,4,5])

print(st1)

print(st1 <= st2)
print(st1 > st2)
print(lt1 < lt2)
print(lt1 == lt2)
print(st1 != st2)

def average_score_curse(classe, course):
    """ Функция подсчета ср. балла у всех представителей класса по выбронному курсу.
     Подходит и для студетов и для лекторов """
    gut = []
    for i in classe.instances:
        if course in i.grades:
            if 1 < len(i.grades[course]):
                for e in i.grades[course]:
                    gut += e
            else:
                gut += i.grades[course][0]
    return(f"По всему курсу {course} средняя оценка {round((sum(gut)/len(gut)),1)}")

print(average_score_curse(Lecturer, "Python"))
print(average_score_curse(Student, "Python"))
print(average_score_curse(Student, "OOP"))
