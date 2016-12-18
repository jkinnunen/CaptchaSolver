# Captcha Solver

Captcha Solver - это дополнение для программы экранного доступа NVDA, предоставляющее удобный способ распознавания капчи посредством сервиса rucaptcha.com

## Настройка и использование
После установки дополнения выполните следующие действия:

1. Зарегистрируйтесь на сайте [rucaptcha.com](https://rucaptcha.com/) и пополните там баланс аккаунта любым удобным способом.
2. Со странице [https://rucaptcha.com/setting] скопируйте ваш 32-х значный ключ API.
3. Откройте меню NVDA/Сервис/Настройки Captcha Solver... и в появившимся диалоговом окне настроек в поле "Ключ API" вставте полученый на предыдущем шаге ключ и нажмите кнопку "OK".
4. Откройте меню NVDA/Параметры/Жесты ввода и в разделе "Captcha Solver" назначте любой свободный жест (комбинацию клавиш, сенсорный жест и т.д.) на команду "Начать решение капчи". Также рекомендуется назначить жест на команду "Сообщить баланс аккаунта" для контроля расходов.

Теперь следует используя объектную навигацию NVDA, установить навигатор на объект с изображением капчи (как правило это объект типа "графика") и настроенным ранее жестом запустить процесс распознавания.
После сообщения об успешной отправки изображения капчи следует 10-15 секунд подождать результат распознавания и если всё пройдёт хорошо, то NVDA сообщит об этом, а в буфере обмена появится распознанный текст.
Дополнение предназначено для распознавания классической капчи с одной строкой символов на изображении. Кириллические капчи также распознаются без проблем.

## Дополнительные настройки

Флажок "Учитывать регистр при распознавании" в диалоге настроек CaptchaSolver определяет, должен ли работник решающий капчу вводить ответ с учётом регистра символов на изображении. В большинстве случаев регистр символов при ответе на капчу значения не имеет.
Флажок "Использовать HTTPS" указывает, должен ли CaptchaSolver шифровать все запросы к серверу rucaptcha.com. Полезно в незащищённых сетях для защиты от сниффинга.
