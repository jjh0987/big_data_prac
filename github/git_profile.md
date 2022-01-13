# profile 웹페이지 생성

## 1. 템플릿 홈페이지

- [https://startbootstrap.com/](https://startbootstrap.com/)

- [https://html5up.net/](https://html5up.net/)

## 2. 압축파일 받은후, 압축폴더를 원하는 디렉터리에 풀기

```bash 
git init git add . 
git commit -m "Upload profile template" 
git remote add origin (hub URL) 
git push -u origin master
```

- 그 후, github (repository) -> setting -> pages
- 브랜치 선택 후 저장하면 홈페이지 URL 발급.
- 혹시나 웹사이트를 열었는데 404 에러가 나타난다면? 로컬 저장소에 .nojekyll 파일을 생성 (빈파일)