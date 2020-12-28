from app import app
from app.models import Person, Administrator, User

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'Person':Person, 'Administrator':Administrator, 'User':User}