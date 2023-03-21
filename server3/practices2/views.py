from django.shortcuts import render
from .models import Article
guestbook = []

def index(request):
  guestbook = Article.objects.all()
  # Select =  From Articles
  return render(request, 'practices2/index.html', {'guestbook' : guestbook})
  # 이것도 게스트북 대신 DB에서 가져오면 됨
  

def create(request):
  
  content = request.GET.get('content')
  #우측부터 읽자! content라는게 날아오니, 그것을 content로 정의하겠다.
  # guestbook.append(content)
  #이걸 영영 저장하려면 append가 아니고 DB에 저장을 해야됨.
  Article.objects.create(content=content)
  # 방명록 넣기, 이걸 글에서 보여주려면? 위에 다른페이지에 지정해보자
  return render(request, 'practices2/create.html', {'content' : content} )
  #그리고 content를 create에서 content로 사용하려고 한다! ( {{ content }} )

# 이렇게 하면 (어플이 여러개일때, 동일한 이름의 html 파일이 있으면 프로젝트 settings.py INSTALLED_APPS에 등록되어진 어플 순서중 가장 먼저 등록된
# 어플의 html파일이 열린다 !!)
# 그러므로 base.html도 굳이 여러개 만들필요 없다 (대신 겹치게만들면 먼저 등록된 앱이 실행됨)
# 그러니 저렇게 폴더를 구분해서 지정해주면 (각 어플의 templates 폴더내부에 어플이름과 동일한 폴더를 만들어주면 된다), 겹치는 문제가 발생하지않음!!

# 하지만 기준이되는 base.html (부모템플릿) 은 템플릿폴더 최상단에 놔둬줘야함 혹은 프로젝트의 Settings.py의 Templates-> DIRS에 폴더지정을 따로할수있다.