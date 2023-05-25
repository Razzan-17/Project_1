from wtforms import Form, StringField, PasswordField, validators


class RegisterForm(Form):
    name = StringField('Как к вам обращаться?', [validators.Length(min=2, max=30)])
    email = StringField('Адрес e-mail:', [validators.Length(min=6, max=35)])
    password = PasswordField('Пароль:', [
                        validators.DataRequired(),
                        validators.EqualTo('confirm', message='Пароли должны совпадать')
    ])
    confirm = PasswordField('Повторите пароль:')
