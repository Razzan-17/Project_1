from wtforms import Form, StringField, EmailField, PasswordField, validators


class RegisterForm(Form):
    name = StringField('Как к вам обращаться?', [validators.Length(min=2, max=30)])
    email = EmailField('E-mail:', [validators.Length(min=6, max=35),
                                   validators.InputRequired()])
    password = PasswordField('Пароль:', [
                        validators.Length(min=8),
                        validators.DataRequired(),
                        validators.EqualTo('confirm', message='Пароли должны совпадать')])
    confirm = PasswordField('Повторите пароль:', [validators.DataRequired()])


class LoginForm(Form):
    email = EmailField('email:', [validators.Length(min=6, max=35),
                                  validators.InputRequired()])
    password = PasswordField('password:', [validators.Length(min=8, max=16),
                                           validators.InputRequired()])
