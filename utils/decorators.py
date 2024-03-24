def input_error(old_func):
    def inner(*args, **kwargs):
        try:
            return old_func(*args, **kwargs)
        except (ValueError, IndexError):
            return 'Enter the argument for the command'
        except Exception as e:
            return e

    return inner
