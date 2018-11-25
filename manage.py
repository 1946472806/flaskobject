from flask_migrate import MigrateCommand
from flask_script import Manager

from app import create_app

app = create_app()

#实例化manager
manager = Manager(app)
#迁移文件
manager.add_command('db',MigrateCommand)



if __name__ == '__main__':
    # app.run(debug=True) #开启debug模式，可以实时刷新页面
    manager.run()  # 开启debug模式，可以实时刷新页面
