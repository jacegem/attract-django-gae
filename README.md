# attract project

## 프로젝트 생성

```sh
pip install django
django-admin.py startproject --template https://github.com/potatolondon/djangae-scaffold/zipball/master --extension py,yaml,md [PROJECTNAME]
cd [PROJECTNAME]
python install_deps
python manage.py check --deploy --settings=[PROJECTNAME].settings_live
python manage.py runserver
```

Node 모듈 설치

```sh
npm install
```


포트 지정 실행

```sh
python manage.py runserver 0.0.0.0:9000
```


firebase 추가 테스트

python-docs-samples\appengine\standard\firebase\firetactoe 내용 참고

```
flask==0.12
requests==2.13.0
requests_toolbelt==0.7.1
oauth2client==4.0.0
functools32==3.2.3.post2; python_version < "3"
```

추가하였으니, 다시 설치 

```sh
python install_deps
```

배포 테스트를 해본다. 
```sh
gcloud app deploy
```
문제없이 실행된다면, app engine 에서 사용할 수 있다. 


미러 프로젝트로 생성한다. 
전달해주는 정보를 바탕으로 데이터를 저장한다. 
JSON 타입. 테이블명, 컬럼명, 데이터


앱생성

```sh
python2.bat manage.py startapp stock
```



### 출처 

- https://github.com/potatolondon/djangae
- http://i5on9i.blogspot.kr/2016/09/google-app-engine-django.html
- python-docs-samples\appengine\standard\firebase\firetactoe