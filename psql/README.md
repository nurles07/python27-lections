# Slash commands
* \l - список всех база данных   бд == (база данных)
* \c - показывает через какого юзера и к какой бд мы подключены
* \c name_of_db - подключение к какой-то бд 
* \du - список всех юзеров в postgres
* \dt - список всех таблиц в текущей бд
* \d+ - более подробная информация  о таблицах в текущей бд
* \d+ name_of_table - более подробная информация о таблице
* \q - выход из субд (psql)       субд - (система управления база данных)


# Создание бд и таблиц
```sql
CREATE DATABASE name_of_db;
-- создание бд 
```

```sql
CREATE TABLE name_of_table(
    column1 data_type1,
    column2 data_type2,
    ...
);
-- создание таблицы с полями 
```

# Удаление бд и таблицы
```sql
DROP DATABASE name_of_db;
-- удаление бд
```

# Заполнение таблиц
```sql
INSERT INTO name_of_db VALUES
(val1, val2),
(val1.2, val2.2);
-- запись данных в таблицу (заполнение всех полей)
```

# Вывод данных из таблицы 
```sql
SELECT * FROM name_of_table; 
-- вывод всех записей со всеми полями
```


```sql
SELECT column1, column3 FROM name_of_table;
-- вывод конкретных полей
```

# Условия 
```sql
DELETE FROM name_of_table WHERE condition;
-- удаление всех записей из таблицы соответсвующих данному условию
```



```sql
SELECT * FROM name_of_table WHERE column = 'hello';
-- строгое равенство
```

```sql
SELECT * FROM name_of_table WHERE column LIKE '%hello%';
-- записи включающие в себя данную строку с учетoм регистра 
-- aaahello
-- hello world
-- hello
-- Hello world - не пройдет (потому что регистр другой)

```

```sql
SELECT * FROM name_of_table WHERE column LIKE '%hello%';
-- записи включающие в себя данную строку без учета регистра 
-- aaahello
-- hello world
-- hello
-- Hello world 
-- HeLLo
```

```sql
SELECT * FROM name_of_table ORDER BY column;
-- сортировка записей по данному полю в порядке возрастания
```


```sql
SELECT * FROM name_of_table ORDER BY column DESC;
-- сортировка записей по данному полю в порядке убывания
```

```sql
SELECT * FROM name_of_table LIMIT 10;
-- вывод первых 10 записей
```

```sql
SELECT * FROM name_of_table OFFSET 10;
-- пропускаем первые 10 записей
```

```sql
SELECT * FROM name_of_table LIMIT 10 OFFSET 5;
-- пропускаем первые 5 записей
-- вытаскиваем 10 записей 
```

# Обновление таблицы
```sql
ALTER TABLE name_of_table ADD COLUMN col_name col_type constraint;
-- добовляем новую колонку в таблицу
```

```sql
ALTER TABLE name_of_table DROP COLUMN col_name;
-- удаляем колонку из таблицы
```

```sql
ALTER TABLE name_of_table RENAME COLUMN col_name TO new_col_name;
-- переменновывание колонки
```

```sql
ALTER TABLE name_of_table ALTER COLUMN col_name SET DATA TYPE new_type;
-- изминение типа данных у поля
```

# Ограничение (constraints)
* `UNIQUE` - не разрешает дубликаты
* `NOT NULL` - требует обязательного заполнение поля
* `PRIMARY KEY` - как UNIQUE и NOT NULL + строит binary tree для быстрого поиска
* `FOREIGN KEY` - ссылается на pk  в другой таблице и проверяет, существует ли такое id


# СВЯЗИ
## Виды связей
> Один к одному(one 2 one)
* один человек - один профиль 
* один автор - одна автобиография 

> Один ко многим (one to many)
* один блоггер - много постов
* одна марка - много модолей
* одна страна - много областей
* один продукт - много комментариев

> Многие ко многим (many to many)
* один разработчик - много проектовю один проект - много

## реализация one2many в postgres
```sql
CREATE TABLE blogger(
    id serial PRIMARY KEY,
    name varchar(50),
    age int
);

CREATE TABLE post (
    id serial PRIMARY KEY,
    title varchar(100),
    body text,
    blogger_id int,

    CONSTRAINT fk_post_blogger
    FOREIGN KEY (blogger_id) REFERENCES blogger (id)
);
```

# JOINS
> **JOIN** - инструкция, которая позваляет одним SELECT, брать данные из двух таблиц (у которых есть связанные поля)

> **INNER JOIN (JOIN)** - достаются записи у которых есть данные в обоих таблицах
>**FULL JOIN** - достаются все записи и спервой таблицы и со второй  