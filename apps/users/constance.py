class TypeTeacherInfo:

    WORK_EXPERIENCE = 'experience'
    ACHIEVEMENT = 'achievement'
    TALENTS = 'talents'
    ABOUT_ME = 'about_me'

    TITLES = {
        WORK_EXPERIENCE: 'Опыт работы',
        ACHIEVEMENT: 'Достижения',
        TALENTS: 'Таланты',
        ABOUT_ME: 'Обо мне'
    }

    CHOICES_TYPES = (
        (WORK_EXPERIENCE, TITLES[WORK_EXPERIENCE]),
        (ACHIEVEMENT, TITLES[ACHIEVEMENT]),
        (TALENTS, TITLES[TALENTS]),
        (ABOUT_ME, TITLES[ABOUT_ME])
    )
