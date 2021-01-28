create database email_sender;

\c email_sender

create table emails (
  id SERIAL PRIMARY KEY,
  data TIMESTAMP NOT NULL DEFAULT current_timestamp,
  subject VARCHAR(100) NOT NULL,
  message VARCHAR(100) NOT NULL
);