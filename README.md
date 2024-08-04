# Тестовое задание

Телеграм бот как одно из составляющих тестового задания.  
Подробное описание тестового задания: https://github.com/vggog/test_task_deploy/blob/master/README.md  
Родительский репозиторий: https://github.com/vggog/test_task_deploy  

### Деплой
Если есть желание запустить проект обособленно от родительсокго проекта, то необходимо: 
1) Заполнить .env файл в родительском каталоге репозитория(заполнить также как и .env_example).
2) Сбилдить docker:  
   ```docker build -t test_task_bot_image .```
4) Запустить docker:  
   ```docker run -it --rm --env-file .env --name test_task_bot test_task_bot_image```
