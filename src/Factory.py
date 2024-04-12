def Factory(name):
    unsafe = name[0] == '_'
    if unsafe:
        name = name[1:]

    name = name.capitalize()

    try:
        module = __import__(f'applications.{name}')
        app_file = getattr(module, name)
        app = getattr(app_file, name)()

        if unsafe:
            app.set_is_unsafe(True)
        return app

    except ModuleNotFoundError:
        raise ModuleNotFoundError(f"unsupported application {name}")
