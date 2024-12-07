# Домашнее задание по теме "Интроспекция"

def introspection_info(obj):
    result = {"type": obj.__class__.__name__,
              "attributes": dir(obj),
              "methods": [func for func in dir(obj) if callable(getattr(obj, func))],
              "module": obj.__class__.__module__,
              "callable": callable(obj)
              }
    return result


if __name__ == '__main__':
    number_info = introspection_info(42)
    print(number_info)
