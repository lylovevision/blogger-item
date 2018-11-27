Open 'bloggerdb/app.py' and set up your database.

You need to enter 'my_flask_blogger'.

Ubuntu performs `pip3 install requirements.txt`

Win performs `pip install requirements.txt`

Access port  [0.0.0.0:9876](0.0.0.0:9876)

There is login,imgs requte

All deletion and modification operations are completed by themselves.

Win is mostly utf8 encoding, whereas in other environments you need to perform the following encoding or appropriate encoding to create a database

```sql
CREATE DATABASE IF NOT EXISTS bloggerdb default character SET utf8 COLLATE utf8_general_ci;
```
`pip uninstall packagename`
packagename = flask-sqlalchemy < 2.2

