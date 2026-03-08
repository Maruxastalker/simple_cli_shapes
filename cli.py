from storage import ShapeStorage

HELP_TEXT = """
Доступные команды:
  point  x y
  segment x1 y1 x2 y2
  circle x y r
  square x y a

  delete id
  list
  help
  exit
""".strip()


def parse_floats(args, expected_count):
    if len(args) != expected_count:
        return None
    try:
        return [float(a) for a in args]
    except ValueError:
        return None


def main():
    storage = ShapeStorage()
    print("Простой векторный редактор. Введите 'help' для списка команд.")

    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not line:
            continue

        parts = line.split()
        cmd, args = parts[0].lower(), parts[1:]

        if cmd in ("exit", "quit"):
            break

        if cmd == "help":
            print(HELP_TEXT)
            continue

        if cmd == "list":
            shapes = storage.list_all()
            if not shapes:
                print("Фигур нет.")
            else:
                for s in shapes:
                    print(s)
            continue

        if cmd == "delete":
            if len(args) != 1:
                print("Использование: delete id")
                continue
            try:
                id_ = int(args[0])
            except ValueError:
                print("id должен быть целым числом")
                continue

            if storage.delete(id_):
                print(f"Фигура {id_} удалена.")
            else:
                print(f"Фигура с id={id_} не найдена.")
            continue


        if cmd == "point":
            nums = parse_floats(args, 2)
            if nums is None:
                print("Использование: point x y")
                continue
            shape = storage.add_point(*nums)
            print(shape)
            continue

        if cmd == "segment":
            nums = parse_floats(args, 4)
            if nums is None:
                print("Использование: segment x1 y1 x2 y2")
                continue
            shape = storage.add_segment(*nums)
            print(shape)
            continue

        if cmd == "circle":
            nums = parse_floats(args, 3)
            if nums is None:
                print("Использование: circle x y r")
                continue
            shape = storage.add_circle(*nums)
            print(shape)
            continue

        if cmd == "square":
            nums = parse_floats(args, 3)
            if nums is None:
                print("Использование: square x y a")
                continue
            shape = storage.add_square(*nums)
            print(shape)
            continue

        print("Неизвестная команда. Введите 'help'.")


if __name__ == "__main__":
    main()