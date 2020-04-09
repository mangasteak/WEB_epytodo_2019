CREATE DATABASE IF NOT EXISTS epytodo;
USE epytodo;

CREATE TABLE IF NOT EXISTS user
    (
        user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        username CHAR(50) NOT NULL,
        password TEXT(1000) NOT NULL
    );

CREATE TABLE IF NOT EXISTS task
    (
        task_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        title CHAR(60) NOT NULL,
        begin DATE,
        end DATE,
        status INT
    );

CREATE TABLE IF NOT EXISTS user_has_task
    (
        fk_user_id INT NOT NULL,
        fk_task_id INT NOT NULL,
        INDEX (fk_user_id),
        FOREIGN KEY (fk_user_id)
            REFERENCES user(user_id),
        INDEX (fk_task_id),
        FOREIGN KEY (fk_task_id)
            REFERENCES task(task_id),
        PRIMARY KEY (fk_task_id, fk_user_id)
    );