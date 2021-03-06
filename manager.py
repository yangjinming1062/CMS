# encoding:utf-8
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import createApp
from extends import db
from apps.admin import models as admin_models
from apps.common import models as common_models  # 导入了才可以通过Migrate创建、更新
from apps.front import models as front_models

app = createApp()
db.init_app(app)
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
@manager.option('-t', '--phone', dest='phone')
def create_user(username, password, phone, email):
    user = admin_models.Users(username=username, password=password, phone=phone, email=email)
    db.session.add(user)
    db.session.commit()
    print(f'添加用户成功：{user.uid}')


if __name__ == '__main__':
    manager.run()
