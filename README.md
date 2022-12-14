# Круглый отличник.

В репо представлены скрипты с помощью которых вы можете
изменять данные электронного дневника ученика. Теперь не составит труда удалить замечания учителей, изменять
оценки и писать вместо учителя похвалы себе или своим друзьям.

### Что понадобится:

Скачать репо электронного дневника можно по [ссылке.](https://github.com/AleksandrBara/e-diary)

База данных находится по этой [ссылке](https://dvmn.org/filer/canonical/1562234129/166/)

### Как работают скрипты:

- `find_schoolkid`  - функция берет ФИО ученикаи и возвращает его объект из базы данных
- `fix_marks` - исправляет все двойки и тройки на пятерки
- `delete_chastisements` - удаляет все замечания ученика
- `create_commendation` - выбирает случайный урок и создает похвалу от учителя.

#### Запуск кода.

- Скачайте код
- Перенесите файл `scriptc.py` в папку с проектом электронного дневника
- Запустите `Django shell`
  ```bash
  python manage.py shell
  ```
- Чтобы запустить скрипт можно его целиком “копипастнуть” в shell, 
а можно положить файл с кодом рядом с manage.py и подключить через import. 
Второй путь удобнее и надёжнее.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).