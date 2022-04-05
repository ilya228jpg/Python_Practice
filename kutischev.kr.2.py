Изначально стоит указать то, что только для создания самой структуры list даже пустой
на 32-х битной системе нам потребуется 36 байтов (56 в 64битной). Так же заметим, что при создании пустого
списка не происходит выделения памяти непосредственно под сами элементы. это мы можем прочитать
в документации по питону (https://docs.python.org/3/c-api/list.html)
во время создания списка с 1 элементом и более память под элементы выделяются по формуле:
Py_ssize_t PyList_Size(PyObject *list) = размер * размерОбъекта(объект)
таким образом при добавлении одного int в наш list мы выделяем память под один указатель
следовательно размер должен увеличиваться на 4(8 в 64 бит) байта. но
при добавлении трех интов в список вызывая list_resize выделяется место для 8 указателей,
следовательно размер увеличится на 64 байта в 64битной системе по сравнению с пустым списком.
такова работа list_resize, он вызывается при добавлении первых двух аргументов и добавляет
по 8 байт а при добавлении третьего он оставляет места с запасом, до тех пор, при этом размер
в памяти не меняется пока запас не закончится, в моей системе получается так что при вызове
списка с 5 элементами задействуется 120 байт, но при добавлении 6 задействуется уже 152 байта
так как еще раз вызывается list_resize.

extend()принимает итерируемый объект в качестве аргумента, распаковывает его элементы и
добавляет их в конец вашего целевого списка. Эта операция эквивалентна x[len(x):] = x
Итерируемый объект, переданный в качестве аргумента, добавит каждый из своих элементов в конец списка.
Имеет временную сложность O (k), где k - длина итеребла.
таким образом стоит не забывать о том, что добавляя iterable obj через extend
мы по суди добавляем его элементы без самой структуры, поэтому в памяти не учитывается
занимаемая память структуры(лист напримет и тд) а только память указателей на элементы.

эквивалентен a[len(a):] = [x]. Итерируемый объект, переданный в качестве аргумента, добавляется
 без каких-либо изменений как один элемент в конец списка, Имеет постоянную временную сложность O (1)