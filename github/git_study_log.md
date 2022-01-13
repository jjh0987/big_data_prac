# Git,Github day1



## 1. notion web

- 실시간으로 자료를 공유할 수 있는 플랫폼

## 2. CLI

- git 설치 후 ls,cd,mv,touch,rm 과 각 옵션 숙지
- cd .. 상위폴더
- rm -rf (디렉토리명) : 디렉토리 제거

## 3. typora

- md 파일을 이용한 워드작성. 

## 4. git(UI 차원에서 vscode terminal 이용)

- git config --global user.name (personal_name)

- git config --global user.email personal_name.(personal_email)

- 타깃 경로로 cd 

- git init -> (master)

- .gitignore 파일 작성

  - [gitignore.io](https://gitignore.io/) : each flatform of .gitignore form 
  - 프로젝트 만든 후, .gitignore 할 파일을 적어두고 git add 를 진행해야 한다. 그렇지 않으면 해당파일은 추적된다.
  - 추적파일과 raw 파일 잘 고려해서 git add, git add . 할 경우 바로 디렉토리내 파일들을 추적하기 때문에 고려 해야한다.
  - git push 경우, ignore file 은 업로드 되지 않는다.

- ls -a 로 .git/ 으로 관리권한이 할당됨을 확인할 수 있다.

- touch a.txt : 더미파일 (untracked)

- git add a.txt : 상태 indexed -> remove?

- git status (vscode)

- git commit -m "file commit" : '내에 커밋 메세지'  -> 커밋 후 로그제거?

- 수정시 modified 마크 -> 다시 git add file , git status 확인 , git commit -m 'comment'

- git log 로 수정자,수정시점 기록확인 가능

  - git log --reverse

  - git log --oneline
  - git log -p

- tip : git add . : 폴더내 모든 변경사항 add

- 모두 출력 불가능시 (git log 시 대량인 경우), 마지막 줄 (end)로 표시 후 반응이 없는 이슈 : q 로 탈출

## 5. github

- 깃허브 셋팅에서 저장소에서 브랜치 이름 설정

- git remote add (attribute_name) (git_hub_local_URL) 

  - git remote add origin https://github.com/jjh0987/TIL.git

    local 저장소 naming # URL : 깃허브 원격 저장소 (로컬)

- git remote remove (attribute_name)

- git remote -v 로 확인 

- git push (local_reposit_name) (hub_branch_name)

  - git push origin master # github setting 에서 hub branch name 설정

- git push -u (local_reposit_name) (hub_branch_name) 이후 git push 는 자동으로 해당 저장소에서 브랜치로 push 됨.

- git clone (repo URL) : setting -> manager access 팀원 설정. 팀원은 저장소 수정,관리 권한 부여. (Public) 의 경우. private 저장소의 경우 git clone 시 불가능.

- 클론에서 add -> commit 진행하면 github에 변경사항 등록이 되고, 그후 origin 폴더에서 git pull 하면 clone 에서 변경사항이 로컬 pc에 반영된다.