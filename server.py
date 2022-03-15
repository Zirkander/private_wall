from flask_app import app
from flask_app.controllers import user_controller
from flask_app.controllers import message_controller
from flask_app.controllers import routes_controller
from flask_app.controllers import logReg_controller
# from flask_app.models.user_model import User
# from flask_app.models.message_model import Message


if __name__ == "__main__":
    app.run(debug=True)
