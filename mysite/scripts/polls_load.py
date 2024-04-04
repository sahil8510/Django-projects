import csv   # https://docs.python.org/3/library/csv.html

from polls.models import Question, Choice

def run():
    print("=== Polls Loader")

    # Choice.objects.all().delete()
    # Question.objects.all().delete()
    # print("=== Objects deleted")

    fhand = open('scripts/dj4e_batch.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header


    Choice.objects.all().delete()
    Question.objects.all().delete()
    print("=== Objects deleted")


    for row in reader:

        q, created= Question.objects.get_or_create(question_text=row[0])


        # q.save()

        # Breed.objects.get_or_create(name=row[1])

        print(q)
        for i in row[1:]:
            print(i)

            # c, created=Choice.objects.get_or_create(choice_text=i)
            # print(c)
            d=Choice(choice_text=i, question=q)
            d.save()






        # Make a new Question and save it

        # Loop through the choice strings in row[1:] and add each choice,
        # connect it to the question and save it

    print("=== Load Complete")