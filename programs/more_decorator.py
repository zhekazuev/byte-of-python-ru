from time import sleep
from functools import wraps
import logging
logging.basicConfig()
log = logging.getLogger("retry")


def retry(f):
    @wraps(f)
    def wrapper_function(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return f(*args, **kwargs)
            except Exception:
                log.exception("Попытка %s/%s не удалась : %s",
                              attempt,
                              MAX_ATTEMPTS,
                              (args, kwargs))
                sleep(10 * attempt)
        log.critical("Все %s попытки не удались : %s",
                     MAX_ATTEMPTS,
                     (args, kwargs))
    return wrapper_function


counter = 0


@retry
def save_to_database(arg):
    print("Запись в базу данных, сетевой вызов и т.д.")
    print("При возникновении исключения попытка будет автоматически повторена.")
    global counter
    counter += 1
    # Это приведет к исключению при первом вызове.
    # И будет работать нормально во втором вызове (т.е. при повторной попытке)
    if counter < 2:
        raise ValueError(arg)


if __name__ == '__main__':
    save_to_database("Некоторое плохое значение")
