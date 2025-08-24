def magic(*args, **kwargs):
    print("unnamed args", args)
    print("keyword args", kwargs)

magic(1, 2, name="furqat", age=12)
