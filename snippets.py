# Сортируем модули по алфавиту

s = """import bar
import baz
import foo"""

print(
    "\n".join(
        sorted(
            s.splitlines()
        )
    )
)

# Создаем строку документации из списка аргументов

s = """foo=None,
        bar='baz',
        quix=42
"""

print('"""Description goes here\n\n{}\n:returns:\n:rtype:\n"""'.format(
    '\n'.join([
        ":param {0}:\n:type {0}:".format(line.split("=")[0].strip(" ,"))
        for line in s.splitlines()
    ])
))


print(s.replace("\t", " " * 4))
