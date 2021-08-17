class Error:

    def __init__(self, text='Error'):
        self.text = text

    def __str__(self):
        return self.text


class KillError(Error):

    def __init__(self, text='Ошибка. Вы убили кого-то'):
        super().__init__(text)


class DrunkError(Error):

    def __init__(self, text='Ошибка. Вы напились'):
        super().__init__(text)


class CarCrashError(Error):

    def __init__(self, text='Ошибка. Вы попали в ДТП'):
        super().__init__(text)


class GluttonyError(Error):

    def __init__(self, text='Ошибка. Вы обьелись'):
        super().__init__(text)


class DepressionError(Error):

    def __init__(self, text='Ошибка. Вы приуныли'):
        super().__init__(text)
