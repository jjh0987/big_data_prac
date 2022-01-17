# Git,Github day1



## 1. notion web

- 실시간으로 자료를 공유할 수 있는 플랫폼

## 2. CLI

- git 설치 후 ls,cd,mv,touch,rm 과 각 옵션 숙지
- cd .. 상위폴더
- rm -rf (디렉토리명) : 디렉토리 제거 또한 .git 제거 가능 (init     해제 시킨다.)

## 3. typora

- md file editor 

## 4. git(UI 차원에서 vscode terminal 이용)

### 1. git init 설정, 설정할 파일

- git config --global user.name (personal_name)

- git config --global user.email personal_name.(personal_email)

- 타깃 경로로 cd 

- git init -> (master)

- .gitignore 파일 작성

  - [gitignore.io](https://gitignore.io/) : each flatform of .gitignore form 

  - 프로젝트 만든 후, .gitignore 할 파일을 적어두고 git add 를 진행해야 한다. 그렇지 않으면 해당파일은 추적된다.

  - 추적파일과 raw 파일 잘 고려해서 git add, git add . 할 경우 바로 디렉토리내 파일들을 추적하기 때문에 고려 해야한다.

  - git push 경우, ignore file 은 업로드 되지 않는다.

  - .gitignore을 커밋, 리포지터리 랑 연결후 ignorencce 작성 하는 경우, 캐시를 모두 지우고 다시 add 한 후 commit 한다.

  - ```bash
    git rm -r --cached .
    git add .
    git commit -m "fixed untracked files"
    ```

### 2. git basic

- ls -a 로 .git/ 으로 관리권한이 할당됨을 확인할 수 있다.
- touch a.txt : 더미파일 (untracked)
- git add a.txt : 상태 indexed -> staging area
- git status (vscode)
- git commit -m "file commit" : '내에 커밋 메세지' 
- 수정시 modified 마크 -> 다시 git add file , git status 확인 , git commit -m 'comment'
- git log 로 수정자,수정시점 기록확인 가능

  - git log --reverse
  - git log --oneline
  - git log -p
  - git log --graph --oneline
  - git log --branches --not --remotes : 푸시 되지 않은 커밋
- tip : git add . : 폴더내 모든 변경사항 add
- 모두 출력 불가능시 (git log 시 대량인 경우), 마지막 줄 (end)로 표시 후 반응이 없는 이슈 : q 로 탈출

### 3. git reset : cancle commit - local

- 커밋 로그의 지정된 시점으로 돌아간다.

- git reset --soft (hash)
  - 생성된 파일이 있다면 해당커밋으로 돌아거서 add 상태로 진행.
  - 커밋시점으로만 돌아간다. 
  - 파일내용은  기존 head 시점과 그대로.
  - 커밋만 해주면 된다.

- git reset --mixed (hash)
  - 생성된 파일이 있다면 해당커밋으로 돌아가서 untracked 상태로 진행.
  - 수정된 파일이 있다면 해당파일 untracked 상태로 진행.
  - add 후 커밋해주어야 한다.

- git reset --hard (hash)
  - 생성된 파일이 있다면 제거된 상태로 (초기상태로) 진행.
  - 변경내용이 있다면 제거된 상태로 진행.

- git reflog

  - 현재까지 이루어진 모든 로그를 열람한다.
  - reset으로 인해 지워진 해시값도 열람할 수 있다.
  - git reset <option> <hash> 로 해당시점으로 다시 복구 할 수 있다.

- reset 후 push 주의점 

  ```bash
  git reset --hard <hash>
  git push -f origin master
  ```

  - 혼자 사용하는 경우 <=> 팀원이 pull 하지 않은 경우 이용한다.
  - repository 에서와 팀원의 local pc 에서 차이가 생긴다.
  - 팀원이 이러한 사항을 모르고 푸시하는 경우 다시 repository에 추가 되게 된다.
  - collaborator 가 있는 경우, 일관성을 위해 일괄적으로 push 후 일괄적으로 pull 해야한다.
  - 단점 극복위한 git revert 이용. 사라진 내용을 팀원도 commit을 통해 알 수 있다.

### 4. git revert

- 원하는 commit 만 없앨 수 있다.

```bash
git revert <commit_Id>
git revert --no-commit HEAD~<number>
git revert --no-commit master~<number>
git revert <commit_Id>..<commit_Id>
```

- 커밋 시점에 파일(수정사항) 이 있다면 working dir 에 파일이 사라진다. 
- esc , :q 로 탈출
- 'i' 누를 시 디폴트 revert 커밋 메시지를 수정할 수 있다. esc 후 :qw
- 이전 커밋 버전은 모두 살아있고 head에 Revert 기록이 새로 커밋된다. (reset 과 다른점)
- revert 로그를 revert 하면 다시 파일을 살릴 수 있다.

```bash
# revert test
git log --oneline
debebb0 (HEAD -> master) Revert "add a.txt"
a5536f4 Revert "1"
ffbd701 add a.txt
8a3fea7 1
```

- git reset --hard <hash> 시 다시 파일이 복구 된다. 대신 revert 기록은 사라진다.
- 범위 revert 시, 단점은 개별의 revert 된 커밋들이 모두 개별횟수마다 revert 커밋이 남는다.
- git checkpoint 이용한 파일 복구법

```bash
# 특정 커밋으로 돌아가서 복사해올 수 있다.
# 하지만 어떤파일이 얼마나 바뀌었는지는 알기 힘들다.
git reflog # 모든 커밋해시 열람 
git checkpoint <hash> # 해시로 진입
# 가져올 파일 복사해서 복구 혹은 전체 가져오기
git checkpoint master # 탈출
```

- collaborator 가 있는 경우, 일관성을 위해 일괄적으로 push 후 일괄적으로 pull 해야한다.

### 5. git branch

- 마스터 브랜치와 완전 분리된 독립적인 공간
- 해당 브랜치의 헤드 (특정 커밋의 위치)를 이용가능

```bash
git branch # 브랜치 목록
git branch -r # 저장소 브랜치 목록
git branch <branch name> # 브랜치 생성
git branch <branch name> <commit id (hash)> # 특정 커밋 기준 브랜치 생성
git branch -d <branch name> # 병합된 브랜치 삭제
git branch -D <branch name> # 병합되지 않은 브랜치도 삭제
```

### 6. git switch

- 브랜치의 헤드를 이동시킨다. (브랜치 이동)

```bash
git switch <branch name> # 브랜치 이동
git switch -c <branch name> # 브랜치 생성 후 이동
git switcg -c <branch name> <commit id> # 특정 커밋 기준으로 브랜치 생성 후 이동 
```

### 7. git merge

- 브랜치를 합친다. 합치고 싶은 주 브랜치로 switch 한 후 merge 한다. 다음 코드에서 branch1에 헤드가 있다고 가정해본다.
- branch1 과 branch2가 있다고 가정한다.

```bash
git merge branch2
or 
git switch branch2
git merge branch1
```

#### case1

![img](../../Desktop/big_data/typora_md/image/git_study_log/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F454c4f14-e3f0-44b7-8395-1bc9d0365dec%2FUntitled.png)

- 마스터 브랜치에서 선택해야하는 상황이다.

```bash
git switch master
git merge hotfix # hotfix로 결정
git branch -d hotfix # master의 헤드가 hotfix와 같으므로 hotfix 브랜치를 제거해준다.
```

#### case2

![img](../../Desktop/big_data/typora_md/image/git_study_log/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F11ffb183-4b65-41c9-8c40-058e681564e6%2FUntitled.png)

```bash
git switch master
git merge iss53
```

![img](../../Desktop/big_data/typora_md/image/git_study_log/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fa76a9563-95f0-4cc8-abb9-ab2b8366682e%2FUntitled.png)

- C6 : merge branch 'branch name' 으로 설정이 된다. 
- C3 과 C4는 시간순으로 정렬된다.

```bash
git branch -d iss53 # 상위 헤드가 있으므로 제거해준다.
```

#### case3 : conflict experiment

- 상황 : master 과 hotfix branch 에서 같은위치의 내용을 수정하는 경우 conflict error 와 마주친다.

```bash
* 3170247 (HEAD -> master) master test 3
| * ad045fa (hotfix) hotfix test 1
|/
*   ac0e971 Merge branch 'signout'
|\
| * bcade83 signout test 1
* | 48bd5a6 master test 2
|/
* df231d0 login test 1
* 1e62b4c master test 1
```

```bash
git switch master
git merge hotfix
```

![img](../../Desktop/big_data/typora_md/image/git_study_log/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F072a8eb0-4fa6-4759-806e-6ae38069eb8e%2FUntitled.png)

- accept current change, incoming change, both 클릭 시 바로 변환.

```bash
git add . # 위 그림에서 수정할 부분을 선택하거나 새로작성 후 add 
git commit -m 'merge branch hotfix' # merge complete.
```

- git commit 만 할 경우, vim 창이 나온다 (blue text). 
- 'i' 누를 시 -> -- 끼워넣기 -- 상태에서 orange text 수정가능
- 'esc' 입력모드 탈출 
- :wq (write and quit) or :q 탈출 하고 MERGING 상태 해제.

### 8. git show

- `git show` : 현재 브랜치의 가장 최근 커밋 정보를 확인함
- `git show <hash>` : 특정 커밋 정보를 확인함
- `git show HEAD` : HEAD 포인터가 가리키는 커밋정보를 확인함

- `git show <hash> 또는 HEAD^`:
  - 마지막에 `^`표시가 있다.
  - `^`표시 한 개면 한 개전 두 개면 두 개전, 갯수로 얼마나 이전 값인지 알수 있음
  - git show HEAD~3

### 9. git commit --amend

- ```bash
  git commit --amend
  ```

  - 가장 최근 커밋을 수정합니다.
  - 파일을 추가적으로 수정 및 추가 하고 `git add` 명령어 이후 `git commit --amend` 명령어를 입력하면 커밋 메세지 또한 수정 됩니다.
  - 이미 해당 커밋을 push 하였다면 에러가 발생합니다.
  - `git push --force` 옵션으로 푸시가 가능합니다
  - **하지만 이미 push한 커밋을 수정하여 강제로 push하는 것은 코드를 공유해 작업하는 동료들에게 오류를 일으킬 수 있으니 금하도록 합니다.**

## 5. github

### 1. git push process

- git add . , git commit -m 'message'

- git add 제거 : git rm --cached <file_name>

- 깃허브 셋팅에서 저장소에서 브랜치 이름 설정

- git remote add (attribute_name) (git_hub_local_URL) 

  - git remote add origin https://github.com/jjh0987/TIL.git

    local 저장소 naming # URL : 깃허브 원격 저장소 (로컬)

- git remote remove (attribute_name)

- git remote -v 로 확인 

- git push (local_reposit_name) (hub_branch_name)

  - git push origin master # github setting 에서 hub branch name 설정

- git push -u (local_reposit_name) (hub_branch_name) 이후 git push 는 자동으로 해당 저장소에서 브랜치로 push 됨.

### 2. git clone,pull

- git pull origin master : 저장소의 변경내용을 로컬 pc에 반영한다. git clone (repo URL) 은 완전히 로컬 pc 에 복제해온다.
- git clone (repo URL) (dir name) : setting -> manager access 팀원 설정. 팀원은 저장소 수정,관리 권한 부여. (Public) 의 경우. private 저장소의 경우 git clone 시 불가능.
- 위 (dir name) 옵션에서는 clone directory 의 이름을 바로 설정 가능하다 (동일 url을 여러번 clone 하는 경우). 
- 클론에서 add -> commit 진행하면 github에 변경사항 등록이 되고, 그후 origin 폴더에서 git pull 하면 clone 에서 변경사항이 로컬 pc에 반영된다.

### 3. git collaborator 설정

![git](../../Desktop/big_data/typora_md/image/git_study_log/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff6753eae-a269-481c-97c5-c68e2e0ba39e%2F그림1.png)

- collaborator 은 clone을 받아서 commit,push,pull 할 수 있다.

### 4. 원격저장소의 사용

#### case1 : repository의 소유권이 있는 경우 framework

```bash
git clone <url> # 저장소 복제
git switch -c feature/login # feature/login 브랜치 생성 후 이동
git push origin feature/login # 업무완료 후 push
# 깃허브에서 pull request 작성
# master 권한을 가진 관리자가 git merge feature/login 
git switch master 
git pull origin master # 로컬 pc를 최신화 시킨다.
git branch -d feature/login # 완료된 브랜치 제거
```

#### case2 : repository의 소유권이 없는 경우 framework

- github 에서 fork를 진행한다. -> 복제 원격 repository 가 생성된다.

```bash
git clone <url> # url 은 fork 된 복제 url
git init
git remote add origin <url> # 복제 url
git remote add upstream <url> # 원본 url 은 upstream 이 관례적
git switch -c feature/login 
git push origin feature/login # 복제 url 에서 브랜치를 생성해서 기능 구현
# 복제 url 을 깃허브에서 pull request
# master 권한을 가진 관리자가 merge한 경우, 로컬 pc 최신화
git pull upstream master # 원본 url 을 통해 로컬 pc 최신화 
git branch -d feature/login # 로컬 pc 에서 브랜치 삭제
```

- 로컬 pc 에서 파일삭제를 원할 시 git init 을 없애기 위해서 CLI 환경에서 rm -rf .git 으로 init을 없애준다. 그 후 삭제 할 수 있다. 

### 5. git branch push

```bash
git switch -c <branch>
# 수정 후 커밋
git commit -m 'branch_test'
git push origin <branch>
# 깃 허브에서 관리자에게 pr 메세지가 온다.
# pr comment, 수정사항, reject 을 결정한다.
# if admin merge <branch> to master branch in github, refreshing local pc.
# delete easily <branch> from github
git switch master
git pull origin master
git branch -d <branch>
```

- github 에서 커밋된 사항들은 github 에서 verified 마크를 받는다. (직접수정, merge from github)
