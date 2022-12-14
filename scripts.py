import random
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation

COMMENDATIONS = [
    'Неожиданно!'
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!',
]


def find_schoolkid(schoolkid_name):
    try:
        return Schoolkid.objects.get(full_name=schoolkid_name)
    except Schoolkid.DoesNotExist:
        print('Студента {} не существует'.format(schoolkid_name))
        print('Формат ввода: Фамилия-Имя-Отчество!')
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено более одного ученика. Проверьте ФИО!')


def fix_marks(schoolkid):
    badmarks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    badmarks.update(points="5")


def delete_chastisement(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(subject, schoolkid):
    year_of_study, group_letter = 6, "А"
    commendation = random.choice(COMMENDATIONS)
    lessons = Lesson.objects.filter(
        year_of_study=year_of_study,
        group_letter=group_letter,
        subject__title=subject,
    ).order_by('subject')
    if not lessons.exists():
        exit('Предмет не найден!!!')
    lesson = random.choice(lessons)
    Commendation.objects.create(
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher,
        created=lesson.date,
        text=commendation,
    )
