class StatusComment:
    UNPROCESSED = 1
    IN_WORK = 2
    CLOSED = 3

    TITLES = {
        UNPROCESSED: 'Необработанная',
        IN_WORK: 'В работе',
        CLOSED: 'Закрытая',
    }

    CHOICES = (
        (UNPROCESSED, TITLES[UNPROCESSED]),
        (IN_WORK, TITLES[IN_WORK]),
        (CLOSED, TITLES[CLOSED]),
    )
