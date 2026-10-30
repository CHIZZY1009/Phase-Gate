amount_of_classes = int(input("How many classes do you have?: "))
students = int(input("How many students do you have in your class?: "))
subjects = int(input("How many subjects do they offer?: "))


def collect_scores():
    
    scores = {}

    for index in range(amount_of_classes):
        class_name = input(("Enter a class name: "))
        scores[class_name] = {}
            
        for indexTwo in range(students):

            student_name = input("Enter a students name:  ")
            scores[class_name][student_name] = {}


            for indexThree in range(subjects):

                subject_name = input("Enter a students subject: ")
                score = int(input("Enter a score: "))

                scores[class_name][student_name][subject_name] = score
            

                while score < 0 or score > 100:
                    print("Invalid score! please enter a score between 0 and 100:  ")
                    score = int(input("Enter score again: "))
    
                    
    return scores
student_scores = collect_scores()
print(student_scores)
       
 
def collation_of_scores(scores):
    results = {}

    for class_name in scores:
        results[class_name] = {}

        for student_name in scores[class_name]:
            
            total = 0
	
            for subject in scores[class_name][student_name]:

                total = total + scores[class_name][student_name][subject]

                average = total / len(scores[class_name][student_name])

                results[class_name][student_name] = {

                "Total": total,
                "Average": average
                }

    return results
results = collation_of_scores(student_scores)


def display_scores(scores, results):

    for class_name in scores:

        print("CLASS:", class_name)
        print("Student     Subject Scores     Total     Average")

        for student_name in scores[class_name]:

            subject_scores = scores[class_name][student_name]
            total = results[class_name][student_name]["Total"]
            average = results[class_name][student_name]["Average"]

            print(student_name, subject_scores, total, average)


display_scores(student_scores, results)







































        
    
