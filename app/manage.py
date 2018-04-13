from app import create_app


app = create_app('development')

manager = Manager(app)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User = User, Role = Role)
if __name__ == '__main__':
    manager.run()
