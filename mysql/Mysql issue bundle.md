# MySQL issue bundle

```mysql
brew install mysql
cd < db-dir>
mysql.server start
# 계정 생성
source < db_name >.sql
mysql -u root -p


# model diagram
# model -> add diagram
# 스키마,테이블 등 생성가능하다.
# 서버와 다이어그램간 import/export 가능
# databses -> forward engineer : diagram -> local
# database -> reverse engineer : local -> diagram
# diagram으로 테이블 생성 시 : 테이블 생성 버튼 클릭시 상단에 스키마 지정을 해주어야 한다. 그리고나서 형식에 맞게 생성
# table output 에서 data export 가능.
```

