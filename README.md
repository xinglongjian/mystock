# mystock
learn python meachine learning and stock

#数据库脚本变更
##使用flask_migrate，flask_script脚本更新
>1、flask db init
>2、flask db migrate
>3、flask db upgrade
注意：如果报alembic.util.exc.CommandError: Target database is not up to date.把migrations里versions中文件删掉
重新执行2，3