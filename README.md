<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
<h1>Сайт поиска вакансий и резюме</h1>
  <div><p>Установка (для пользователей операционных систем семейства MacOs/Linux):</p>
<p>Открыть терминал или консоль и перейти в нужную Вам директорию<br>
Прописать команду<br>
<pre><code>git clone https://github.com/evgeny50/job_site.git</code></pre></p>
<p>Прописать следующие команды:</p>
<pre><code>python3 -m venv env
</code></pre>
<p>Активировать виртуальное окружение</p>
<pre><code>source/env/bin/activate
</code></pre>
<p>Перейти в директорию job</p>
<pre><code>pip install -r requirements.txt
</code></pre>
<p>Выполнить миграции</p>
<pre><code>python manage.py migrate
</code></pre>
<p>Запустить сервер</p>
<pre><code>python manage.py runserver
</code></pre>
</div>
</body>

</html>
