# 抽籤網站
這是一個讓人上傳照片，抽籤後顯示中獎者照片的網站，已抽中的中獎者將不會再被抽中

# Dependencies
1. Crispy forms
網站利用第三方套件 Django Crispy Forms 來 render，可以使用 pip 安裝
```
pip install django-crispy-forms
```

# 說明
1. 由於並未部署網站，取用照片的機制必須透過在```urls.py```中設定 ```MEDIA_ROOT ```路徑以達成
```
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
因此目前也暫時設定 ``` DEBUG = True ```

2. 暫時尚未實作一次上傳多組人以及刪除成員的機制
