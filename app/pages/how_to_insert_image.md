title: FAQ позагрузке изображений
subject: Туториал

К сожалению для того, чтобы не нагружать сервер лишними байтами картинок, видео и всего такого, то было приянто решение подгружать медиа с других сайтов. В частности, чтобы загрузить изображение в блог сначала нужно загрузить его на какой-нибудь хостинг изображений, например [imgur](https://imgur.com/upload) или [imgbb](https://ru.imgbb.com/). И только потом вставить ссылку на картинку с помощью конструкций
```
Картинка без `alt` текста

![](//placehold.it/150x100)

Картинка с альтом и тайтлом:

![Alt text](//placehold.it/150x100 "Можно задать title")

Запомнить просто: синтаксис как у ссылок, только перед открывающей квадратной скобкой ставится восклицательный знак.

Картинки «сноски»:

![Картинка][image1]
![Картинка][image2]
![Картинка][image3]
```