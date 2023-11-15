from datetime import datetime

def main():
    student_notes = {
        "lisa" : 18,
        "jérome" : 14,
        "nael" : 10,
        "johnny" : 17,
        "lory" : 13
    }
    best_student = max(student_notes, key=student_notes.get)
    print("The best student is " + best_student + " with " + str(student_notes[best_student]) + "/20")
    print(sorted(student_notes))
if __name__ == "__main__":
    main()