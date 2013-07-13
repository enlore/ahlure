from flask.ext.script import Manager
from ahlure import create_app


app = create_app()
manager = Manager(app)

@manager.command
def run():
    app.run()

def debug():
    app.debug = True
    app.run(port=9001)

@manager.command
def d():
    debug()

if __name__ == '__main__':
    manager.run()
