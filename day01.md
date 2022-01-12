# Git,Github day1



## 1. notion web

- 실시간으로 자료를 공유할 수 있는 플랫폼

## 2. CLI

- git 설치 후 ls,cd,mv,rm 과 각 옵션 숙지

## 3. typora

- md 파일을 이용한 워드작성. 

## 4.git(UI 차원에서 vscode terminal 이용)

- git config --global user.name (personal_name)
- git config --global user.email personal_name.(personal_email)
- 타깃 경로로 cd 
- git init -> (master)
- ls -a 로 .git/ 으로 관리권한이 할당됨을 확인할 수 있다.
- touch a.txt : 더미파일 (untracked)
- git add a.txt : 상태 indexed -> remove?
- git status (vscode)
- git commit -m "file commit" : '내에 커밋 메세지'  -> 커밋 후 로그제거?
- 수정시 modified 마크 -> 다시 git add file , git status 확인 , git commit -m 'comment'
- git log 로 수정자,수정시점 기록확인 가능
  - git log --oneline
  - git log -p
- tip : git add . : 폴더내 모든 변경사항 add
- 모두 출력 불가능시 (git log 시 대량인 경우), 마지막 줄 (end)로 표시 후 반응이 없는 이슈 : q 로 탈출
- git remote add (attribute_name) (git hub URL) 
- git remote remove (attribute_name)
- git remote -v 로 확인