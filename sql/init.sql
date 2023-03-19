CREATE DATABASE chatbot;
GO


CREATE TABLE chatbot.dbo.users (
    id int IDENTITY(1,1) PRIMARY KEY,
    name varchar(max),
    surname varchar(max),
    cif varchar(max)   
);
GO

insert into chatbot.dbo.users(name, surname, cif)
values ('Monika', 'Łukowska', '12345');

commit;
GO