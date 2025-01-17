# Модули

Как можно использовать код повторно, помещая его в функции, мы уже видели. А что, если нам понадобится повторно использовать различные функции в других наших программах? Как вы уже, наверное, догадались, ответ – модули.

Существуют разные способы составления модулей, но самый простой – это создать файл с расширением `.py`, содержащий функции и переменные.

Другой способ – написать модуль на том языке программирования, на котором написан сам интерпретатор Python. Например, можно писать модули на [языке программирования C](http://docs.python.org/3/extending/), которые после компиляции могут использоваться стандартным интерпретатором Python.

Модуль можно *импортировать* в другую программу, чтобы использовать функции из него. Точно так же мы используем стандартную библиотеку Python. Сперва посмотрим, как использовать модули стандартной библиотеки.

Пример (сохраните как `module_using_sys.py`):

<pre><code class="lang-python">{% include "./programs/module_using_sys.py" %}</code></pre>

Вывод:

<pre><code>{% include "./programs/module_using_sys.txt" %}</code></pre>

**Как это работает**

В начале мы *импортируем* модуль `sys` командой `import`. Этим мы говорим Python, что хотим использовать этот модуль. Модуль `sys` содержит функции, относящиеся к интерпретатору Python и его среде, т.е. к системе (**sys**tem).

Когда Python выполняет команду `import sys`, он ищет модуль `sys`. В данном случае это один из встроенных модулей, и Python знает, где его искать.

Если бы это был не скомпилированный модуль, т.е. модуль, написанный на Python, тогда интерпретатор Python искал бы его в каталогах, перечисленных в переменной `sys.path`. Если модуль найден, выполняются команды в теле модуля, и он становится *доступным*. Обратите внимание, что инициализация[^1] происходит только при *первом* импорте модуля.

Доступ к переменной `argv` в модуле `sys` предоставляется при помощи точки, т.е. `sys.argv`. Это явно показывает, что это имя является частью модуля `sys`. Ещё одним преимуществом такого обозначения является то, что имя не конфликтует с именем переменной `argv`, которая может использоваться в вашей программе.

Переменная `sys.argv` является *списком* строк (списки будут детально обсуждаться в одной из [последующих глав](./data_structures.md#data-structures)). Она, `sys.argv`, содержит список *аргументов командной строки*, т.е. аргументов, переданных программе из командной строки.

Если вы используете среду разработки[^2] для написания и запуска программ, поищите где-нибудь в её меню возможность передавать параметры командной строки.

В нашем примере, когда мы запускаем `python module_using_sys.py we are arguments`, мы запускаем модуль `module_using_sys.py` командой `python`, а всё, что следует далее – аргументы, передаваемые программе[^3]. Python сохраняет аргументы командной строки в переменной `sys.argv` для дальнейшего использования.

Помните, что имя запускаемого сценария[^4] всегда является первым аргументом в списке `sys.argv`. Так что в приведённом примере `'module_using_sys.py'` будет элементом `sys.argv[0]`, `'we'` – `sys.argv[1]`, `'are'` – `sys.argv[2]`, а `'arguments'` – `sys.argv[3]`. Помните, что в Python нумерация начинается с 0, а не с 1.

`sys.path` содержит список имён каталогов, откуда импортируются модули. Заметьте, что первая строка в `sys.path` пуста; эта пустая строка показывает, что текущая директория также является частью `sys.path`, которая совпадает со значением переменной окружения `PYTHONPATH`. Это означает, что модули, расположенные в текущем каталоге, можно импортировать напрямую. В противном случае придётся поместить свой модуль в один из каталогов, перечисленных в `sys.path`.

Помните, что текущий каталог – это каталог, в котором была запущена программа. Выполните `import os; print(os.getcwd())`, чтобы узнать текущий каталог программы.

## Файлы байткода .pyc {#pyc}

Импорт модуля – относительно дорогостоящее мероприятие, поэтому Python предпринимает некоторые трюки для ускорения этого процесса. Один из способов – создать *байт-компилированные* файлы (или байткод) с расширением `.pyc`, которые являются некой промежуточной формой, в которую Python переводит программу (помните раздел [Введение](./about_python.md#interpreted) о том, как работает Python?). Такой файл `.pyc` полезен при импорте модуля в следующий раз в другую программу – это произойдёт намного быстрее, поскольку значительная часть обработки, требуемой при импорте модуля, будет уже проделана. Этот байткод также является платформо-независимым.

ПРИМЕЧАНИЕ: Обычно файлы `.pyc` создаются в том же каталоге, где расположены и соответствующие им файлы `.py`. Если Python не может получить доступ для записи файлов в этот каталог, файлы `.pyc` созданы _не_ будут.

## Оператор from ... import ... {#from-import-statement}

Чтобы импортировать переменную `argv` прямо в программу и не писать всякий раз `sys.` при обращении к ней, можно воспользоваться выражением `from sys import argv`.

> ВНИМАНИЕ: В общем случае, *избегайте* использования оператора `from..import`, вместо него используйте оператор `import`. Это связано с тем, что ваша программа избежит столкновения имен и будет более читабельной.

Пример:

```python
from math import sqrt
print("Квадратный корень из 16 равен", sqrt(16))
```

## Имя модуля – `__name__` {#module-name}

У каждого модуля есть имя, и команды в модуле могут узнать имя их модуля. Это полезно, когда нужно знать, запущен ли модуль как самостоятельная программа или импортирован. Как уже упоминалось выше, когда модуль импортируется впервые, содержащийся в нём код исполняется. Мы можем воспользоваться этим для того, чтобы заставить модуль вести себя по-разному в зависимости от того, используется ли он сам по себе или импортируется в другую программа. Этого можно достичь с применением атрибута модуля под названием `__name__`.

Пример (сохраните как `module_using_name.py`):

<pre><code class="lang-python">{% include "./programs/module_using_name.py" %}</code></pre>

Вывод:

<pre><code>{% include "./programs/module_using_name.txt" %}</code></pre>

**Как это работает**

В каждом модуле Python определено его имя – `__name__`[^5] . Если оно равно `'__main__'`, это означает, что модуль запущен самостоятельно пользователем, и мы можем выполнить соответствующие действия.

## Создание собственных модулей

Создать собственный модуль очень легко. Да вы всё время делали это! Ведь каждая программа на Python также является и модулем. Необходимо лишь убедиться, что у неё установлено расширение `.py`. Следующий пример объяснит это.

Пример (сохраните как `mymodule.py`):

<pre><code class="lang-python">{% include "./programs/mymodule.py" %}</code></pre>

Выше приведён простой *модуль*. Как видно, в нём нет ничего особенного по сравнению с обычной программой на Python. Далее посмотрим, как использовать этот модуль в других наших программах.

Помните, что модуль должен находиться либо в том же каталоге, что и программа, в которую мы импортируем его, либо в одном из каталогов, указанных в `sys.path`.

Ещё один модуль (сохраните как `mymodule_demo.py`):

<pre><code class="lang-python">{% include "./programs/mymodule_demo.py" %}</code></pre>

Вывод:

<pre><code>{% include "./programs/mymodule_demo.txt" %}</code></pre>

**Как это работает**

Обратите внимание, что мы используем всё то же обозначение точкой для доступа к элементам модуля. Python повсеместно использует одно и то же обозначение точкой, придавая ему таким образом характерный 'Python-овый' вид и не вынуждая нас изучать всё новые и новые способы делать что-либо.

Вот версия, использующая синтаксис `from..import` (сохраните как `mymodule_demo2.py`):

<pre><code class="lang-python">{% include "./programs/mymodule_demo2.py" %}</code></pre>

Вывод `mymodule_demo2.py` такой же, как и `mymodule_demo.py`.

Обратите внимание, что если в модуле, импортирующем данный модуль, уже было объявлено имя `__version__`, возникнет конфликт. Это весьма вероятно, так как объявлять версию любого модуля при помощи этого имени – общепринятая практика. Поэтому всегда рекомендуется отдавать предпочтение оператору `import`, хотя это и сделает вашу программу немного длиннее.

Вы могли бы также использовать:

```python
from mymodule import *
```

Это импортирует все публичные имена, такие как `say_hi`, но не импортирует `__version__`, потому что оно начинается с двойного подчёркивания

> ВНИМАНИЕ: Помните, что вы должны избегать использования import-star, то есть `from mymodule import *`.

<!-- -->

> **Дзэн Python**
>
> Одним из руководящих принципов в Python является "Явное лучше Неявного". Выполните команду `import this`, чтобы узнать больше, а также просмотрите это обсуждение, в котором приводятся примеры по каждому из принципов.

## Функция `dir` {#dir-function}

Встроенная функция `dir()` возвращает список имён, определяемых объектом. 
Например, для модуля в этот список входят функции, классы и переменные, определённые в этом модуле.

Эта функция может принимать аргументы.
Если в качестве аргумента указано имя модуля, она возвращает список имён, определённых в этом модуле. 
Если никакого аргумента не передавать, она вернёт список имён, определённых в текущем модуле.

Пример:

```python
$ python
>>> import sys

# получим список атрибутов модуля sys
>>> dir(sys)
['__displayhook__', '__doc__',
'argv', 'builtin_module_names',
'version', 'version_info']
# здесь представлены только некоторые записи

# получим список атрибутов текущего модуля
>>> dir()
['__builtins__', '__doc__',
'__name__', '__package__', 'sys']

# создадим новую переменную 'a'
>>> a = 5

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys', 'a']

# удалим имя 'a'
>>> del a

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys']
```

**Как это работает**

Сперва мы видим результат применения `dir` к импортированному модулю `sys`. Видим огромный список атрибутов, содержащихся в нём.

Затем мы вызываем функцию `dir`, не передавая ей параметров. По умолчанию, она возвращает список атрибутов текущего модуля. Обратите внимание, что список импортированных модулей также входит туда.

Чтобы пронаблюдать за действием `dir`, мы определяем новую переменную `a` и присваиваем ей значение, а затем снова вызываем `dir`. Видим, что в полученном списке появилось дополнительное значение. Удалим переменную/атрибут из текущего модуля при помощи оператора `del`, и изменения вновь отобразятся на выводе функции `dir`.

Замечание по поводу `del`: этот оператор используется для *удаления* переменной/имени, и после его выполнения, в данном случае – `del a`, к переменной `a` больше невозможно обратиться – её как будто никогда и не было.

Обратите внимание, что функция `dir()` работает для *любого* объекта. Например, выполните `dir(str)`, чтобы увидеть атрибуты класса `str`.

Существует также функция [`vars()`](http://docs.python.org/3/library/functions.html#vars), которая потенциально может дать вам атрибуты и их значения, но она работает не во всех случаях.

## Пакеты

К настоящему времени вы, вероятно, начали наблюдать некоторую иерархию в организации ваших программ. Переменные обычно находятся в функциях. Функции и глобальные переменные обычно находятся в модулях. А что, если возникнет необходимость как-то организовать модули? Вот здесь-то и выходят на сцену пакеты.

Пакеты – это просто каталоги с модулями и специальным файлом `__init__.py`, который показывает Python, что этот каталог особый, так как содержит модули Python.

Представим, что мы хотим создать пакет под названием 'world' с субпакетами 'asia', 'africa' и т.д., которые, в свою очередь, будут содержать модули 'india', 'madagascar' и т.д.

Для этого следовало бы создать следующую структуру каталогов:

```
- <some folder present in the sys.path>/
    - world/
        - __init__.py
        - asia/
            - __init__.py
            - india/
                - __init__.py
                - foo.py
        - africa/
            - __init__.py
            - madagascar/
                - __init__.py
                - bar.py
```

Пакеты – это удобный способ иерархически организовать модули. Такое часто встречается в [стандартной библиотеке](./stdlib.md#stdlib).

## Резюме

Точно так же, как функции являются многократно используемыми фрагментами программ, модули являются многократно используемыми программами. Пакеты – это способ иерархической организации модулей. Стандартная библиотека Python является примером такого набора пакетов и модулей.

Мы увидели, как пользоваться этими модулями и создавать свои.

Далее мы познакомимся с некоторыми интересными концепциями, называемыми “структуры данных”.

## Примечания

[^1]: Инициализация – ряд действий, производимых при начальной загрузке (прим. перев.)

[^2]: IDE – от англ. "Integrated Development Environment" – "интегрированная среда разработки" (прим. перев.)

[^3]: "we are arguments" – англ. "мы аргументы" (прим. перев.)

[^4]: Программу на интерпретируемом языке программирования также называют сценарием или скриптом (прим. перев.)

[^5]: name - англ. "имя" (прим. перев.)
