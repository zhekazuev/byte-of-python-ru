# Объектно-ориентированное программирование {#oop}

До сих пор наши программы состояли из функций, т.е. блоков выражений, которые манипулируют данными. Это называется _процедурно-ориентированным_ стилем программирования. Существует и другой способ организации программ: объединять данные и функционал внутри некоего объекта. Это называется _объектно-ориентированной_ парадигмой программирования. В большинстве случаев можно ограничиться процедурным программированием, а при написании большой программы или если решение конкретной задачи того требует, можно переходить к техникам объектно-ориентированного программирования.

Два основных аспекта объектно-ориентированного программирования – классы и объекты. **Класс** создаёт новый _тип_, а **объекты** являются **экземплярами** класса. Аналогично, когда мы говорим о переменных типа `int`, это означает, что переменные, которые хранят целочисленные значения, являются экземплярами (объектами) класса `int`.

> **Замечание для Программистов на Статических Языках**
> 
> Обратите внимание, что даже целые числа рассматриваются как объекты (класса `int`), в отличие от C++ и Java (до версии 1.5), где целые числа являются примитивами.
>
> См. `help(int)` для более детального описания этого класса.
> 
> Программисты на C# и Java 1.5 могут заметить сходство с концепцией _упаковки и распаковки_(boxing and unboxing).

Объекты могут хранить данные в обычных переменных, которые _принадлежат_ объекту. Переменные, принадлежащие объекту или классу, называют **полями**. Объекты могут также обладать функционалом, т.е. иметь функции, _принадлежащие_ классу. Такие функции принято называть **методами** класса. Эта терминология важна, так как она помогает нам отличать независимые функции и переменные от тех, что принадлежат классу или объекту. Всё вместе (поля и методы) принято называть **атрибутами** класса.

Поля бывают двух типов: они могут принадлежать каждому отдельному экземпляру объекта класса или всему классу. Они называются **переменными экземпляра** и **переменными класса** соответственно.

Класс создаётся ключевым словом `class`. Поля и методы класса записываются в блоке кода с отступом.

## Параметр `self` {#self}

Методы класса имеют одно отличие от обычных функций: они должны иметь дополнительно имя, добавляемое к началу списка параметров. Однако, при вызове метода никакого значения этому параметру присваивать **не нужно** – его укажет Python. Эта переменная указывает на _сам_ объект экземпляра класса, и по традиции она называется `self`.

Хотя этому параметру можно дать любое имя, _настоятельно рекомендуется_ использовать только имя `self`; использование любого другого имени не приветствуется. Есть много достоинств использования стандартного имени: во-первых, любой человек, просматривающий вашу программу, легко узнает его; во-вторых, некоторые специализированные Интегрированные среды разработки (IDE - Integrated Development Environment) изначально рассчитаны на использование `self`.

> **Замечание для Программистов на C++, Java и C#**
> 
> `self` в Python эквивалентно указателю `this` в C++ и ссылке this в Java и C#.

Вы, должно быть, удивляетесь, как Python присваивает значение `self `и почему вам не нужно указывать это значение самостоятельно. Поясним это на примере. Предположим, у нас есть класс с именем `MyClass` и экземпляр этого класса с именем `myobject`. При вызове метода этого объекта, например, `myobject.method(arg1, arg2)`, Python автоматически превращает это в `MyClass.method(myobject, arg1, arg2)` – в этом и состоит смысл `self`.

Это также означает, что если какой-либо метод не принимает аргументов, у него всё равно будет один аргумент – `self`.

## Классы {#classes}

Простейший класс показан в следующем примере (сохраните как `oop_simplestclass.py`).

<pre><code class="lang-python">{% include "./programs/oop_simplestclass.py" %}</code></pre>

Вывод:

<pre><code>{% include "./programs/oop_simplestclass.txt" %}</code></pre>

**Как это работает**

Мы создаём новый класс при помощи оператора `class` и имени класса. За этим следует блок выражений, формирующих тело класса. В данном случае блок у нас пуст, на что указывает оператор `pass`.

Далее мы создаём объект-экземпляр класса, записывая имя класса со скобками. (Мы узнаем [больше о реализации](#init) в следующем разделе). Для проверки мы выясняем тип переменной, просто выводя её на экран. Так мы видим, что у нас есть экземпляр класса `Person` в модуле `__main__`.

Обратите внимание, что выводится также и адрес в памяти компьютера, где хранится ваш объект. На вашем компьютере адрес будет другим, так как Python хранит объекты там, где имеется свободное место.

## Методы

Итак, мы выяснили что классы/объекты могут иметь методы, представляющие собой функции, за исключением дополнительной переменной `self`. А теперь давайте рассмотрим пример (сохраните как `oop_method.py`).

<pre><code class="lang-python">{% include "./programs/oop_method.py" %}</code></pre>

Вывод:

<pre><code>{% include "./programs/oop_method.txt" %}</code></pre>

**Как это работает**

Здесь мы видим `self` в действии. Обратите внимание, что метод `say_hi` не принимает параметров, но тем не менее, имеет `self` в определении функции.

## Метод `__init__` {#init}

Существует много методов, играющих специальную роль в классах Python. Сейчас мы увидим значительность метода `__init__`.

Метод `__init__` запускается, как только объект класса реализуется (т.е. создан). Этот метод полезен для осуществления разного рода *инициализации* (т.е. передача начальных значений вашему объекту), необходимой для данного объекта. Обратите внимание на двойные подчёркивания в начале и в конце имени.

Пример (сохраните как `oop_init.py`):

<pre><code class="lang-python">{% include "./programs/oop_init.py" %}</code></pre>

Вывод:

<pre><code>{% include "./programs/oop_init.txt" %}</code></pre>

**Как это работает**

Здесь мы определяем метод `__init__` так, чтобы он принимал параметр `name` (наряду с обычным `self`). Далее мы создаём новое поле с именем `name`. Обратите внимание, что это две разные переменные, даже несмотря на то, что они обе названы 'name'. Это не проблема, так как точка в выражении `self.name` обозначает, что существует нечто с именем "name", являющееся частью объекта "self", и другое `name` – локальная переменная. Поскольку мы в явном виде указываем, к которому имени мы обращаемся, путаницы не возникнет.

Для создания нового экземпляра `p` класса `Person` мы указываем имя класса, после которого – аргументы в скобках: `p = Person('Swaroop')`.

Метод `__init__` мы при этом не вызываем явным образом. В этом и заключается специальная роль данного метода.

После этого мы получаем возможность использовать поле `self.name` в наших методах, что и продемонстрировано в методе `say_hi`.

## Переменные класса и объекта {#class-obj-vars}

Функциональную часть классов и объектов (т.е. методы) мы обсудили, теперь давайте ознакомимся с частью данных. Данные, т.е. поля, являются не чем иным, как обычными переменными, _заключёнными_ в **пространствах имён** классов и объектов. Это означает, что их имена действительны только в контексте этих классов или объектов. Отсюда и название _пространство имён_.

Существует два типа _полей_: переменные класса и переменные объекта, которые различаются в зависимости от того, _принадлежит_ ли переменная классу или объекту соответственно.

**Переменные класса** разделяемы – доступ к ним могут получать все экземпляры этого класса. Переменная класса существует только одна, поэтому когда любой из объектов изменяет переменную класса, это изменение отразится и во всех остальных экземплярах того же класса.

**Переменные объекта** принадлежат каждому отдельному экземпляру класса. В этом случае у каждого объекта есть своя собственная копия поля, т.е. не разделяемая и никоим образом не связанная с другими такими же полями в других экземплярах. Это легко понять на примере (сохраните как `oop_objvar.py`):

<pre><code class="lang-python">{% include "./programs/oop_objvar.py" %}</code></pre>

Вывод:

<pre><code>{% include "./programs/oop_objvar.txt" %}</code></pre>

**Как это работает**

Это длинный пример, но он помогает продемонстрировать природу переменных класса и объекта. Здесь `population` принадлежит классу `Robot`, и поэтому является переменной класса. Переменная `name` принадлежит объекту (ей присваивается значение при помощи `self`), и поэтому является переменной объекта.

Таким образом, мы обращаемся к переменной класса `population` как `Robot.population`, а не `self.population`. К переменной же объекта name во всех методах этого объекта мы обращаемся при помощи обозначения `self.name`. Помните об этой простой разнице между переменными класса и объекта. Также имейте в виду, что переменная объекта с тем же именем, что и переменная класса, сделает недоступной ("спрячет") переменную класса!

Вместо `Robot.population` мы могли бы также использовать `self.__class__.Population`, потому что каждый объект ссылается на свой класс через атрибут `self.__class__`.

Метод `how_many` принадлежит классу, а не объекту. Это означает, что мы можем определить его как `classmethod` или `staticmethod`, в зависимости от того, нужно ли нам знать, в каком классе мы находимся. Поскольку нам не нужна такая информация, мы воспользуемся `staticmethod`.

Мы пометили метод `how_many` как метод класса, использующий [декоратор](./more.md#decorator).

<pre><code class="lang-python">{% include "./programs/oop_staticmethod.py" %}</code></pre>

Декораторы можно считать неким упрощённым способом вызова явного оператора, как мы видели в этом примере.
Декораторы можно представить как ярлык для вызова функции-оболочки (т.e. функция, которая "оборачивает" другую функцию, чтобы она могла что-то делать до или после внутренней функции), поэтому применение декоратора `@classmethod` аналогично вызову:

```python
how_many = classmethod(how_many)
```

Пронаблюдайте, как метод `__init__` используется для инициализации экземпляра `Robot` с именем. В этом методе мы увеличиваем счётчик `population` на 1, так как добавляем ещё одного робота. Также заметьте, что значения `self.name` для каждого объекта свои, что указывает на природу переменных объекта.

Помните, что к переменным и методам самого объекта нужно обращаться, пользуясь *только* `self`. Это называется *доступом к атрибутам*.

В этом примере мы также наблюдали применение *строк документации* для классов, равно как и для методов. Во время выполнения мы можем обращаться к строке документации класса при помощи `Robot.__doc__`, а к строке документации метода – при помощи `Robot.say_hi.__doc__`.

В методе `die` мы просто уменьшаем `Robot.population` на 1.

Все члены класса являются публичными (public). Исключение: если имя переменной начинается с _двойного подчёркивания_, как, например, `__privatevar`, Python делает эту переменную приватной (private).

Поэтому принято имя любой переменной, которая должна использоваться только внутри класса или объекта, начинать с подчёркивания, а все остальные имена являются публичными, и могут использоваться в других классах/объектах. Помните, что это лишь соглашение и Python вовсе не обязывает делать именно так (кроме двойного подчёркивания).

> **Примечание для программистов на C++/Java/C#**
> 
> В Python все члены класса (включая данные) являются _публичными_ (public), а все методы – _виртуальными_ (virtual).

## Inheritance

One of the major benefits of object oriented programming is **reuse** of code and one of the ways this is achieved is through the **inheritance** mechanism. Inheritance can be best imagined as implementing a **type and subtype** relationship between classes.

Suppose you want to write a program which has to keep track of the teachers and students in a college. They have some common characteristics such as name, age and address. They also have specific characteristics such as salary, courses and leaves for teachers and, marks and fees for students.

You can create two independent classes for each type and process them but adding a new common characteristic would mean adding to both of these independent classes. This quickly becomes unwieldy.

A better way would be to create a common class called `SchoolMember` and then have the teacher and student classes _inherit_ from this class, i.e. they will become sub-types of this type (class) and then we can add specific characteristics to these sub-types.

There are many advantages to this approach. If we add/change any functionality in `SchoolMember`, this is automatically reflected in the subtypes as well. For example, you can add a new ID card field for both teachers and students by simply adding it to the SchoolMember class. However, changes in the subtypes do not affect other subtypes. Another advantage is that you can refer to a teacher or student object as a `SchoolMember` object which could be useful in some situations such as counting of the number of school members. This is called **polymorphism** where a sub-type can be substituted in any situation where a parent type is expected, i.e. the object can be treated as an instance of the parent class.

Also observe that we reuse the code of the parent class and we do not need to repeat it in the different classes as we would have had to in case we had used independent classes.

The `SchoolMember` class in this situation is known as the **base class** or the **superclass**. The `Teacher` and `Student` classes are called the **derived classes** or **subclasses**.

We will now see this example as a program (save as `oop_subclass.py`):

<pre><code class="lang-python">{% include "./programs/oop_subclass.py" %}</code></pre>

Output:

<pre><code>{% include "./programs/oop_subclass.txt" %}</code></pre>

**How It Works**

To use inheritance, we specify the base class names in a tuple following the class name in the class definition (for example, `class Teacher(SchoolMember)`).   Next, we observe that the `__init__` method of the base class is explicitly called using the  `self`  variable so that we can initialize the base class part of an instance in the subclass. This is very important to remember- Since we are defining a  `__init__`  method in `Teacher`  and  `Student`  subclasses, Python does not automatically call the constructor of the base class  `SchoolMember`, you have to explicitly call it yourself.

In contrast, if we have not defined an  `__init__`  method in a subclass, Python will call the constructor of the base class automatically.

While we could treat instances of `Teacher` or `Student` as we would an instance of `SchoolMember` and access the `tell` method of `SchoolMember` by simply typing `Teacher.tell` or `Student.tell`, we instead define another `tell` method in each subclass (using the `tell` method of `SchoolMember` for part of it) to tailor it for that subclass.  Because we have done this, when we write `Teacher.tell` Python uses the `tell` method for that subclass vs the superclass.  However, if we did not have a `tell` method in the subclass, Python would use the `tell` method in the superclass.  Python always starts looking for methods in the actual subclass type first, and if it doesnt find anything, it starts looking at the methods in the subclasss base classes, one by one in the order they are specified in the tuple (here we only have 1 base class, but you can have multiple base classes) in the class definition.

A note on terminology - if more than one class is listed in the inheritance tuple, then it is called **multiple inheritance**.

The `end` parameter is used in the `print` function in the superclass's `tell()` method to print a line and allow the next print to continue on the same line. This is a trick to make `print` not print a `\n` (newline) symbol at the end of the printing.


## Summary

We have now explored the various aspects of classes and objects as well as the various terminologies associated with it. We have also seen the benefits and pitfalls of object-oriented programming. Python is highly object-oriented and understanding these concepts carefully will help you a lot in the long run.

Next, we will learn how to deal with input/output and how to access files in Python.
