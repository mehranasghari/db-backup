CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    stars INTEGER NOT NULL,
    age INTEGER NOT NULL,
    gender VARCHAR(255) NOT NULL
);

INSERT INTO users (name, email, stars, age, gender) VALUES
('John Doe', 'john.doe@example.com', 5, 30, 'male'),
('Jane Smith', 'jane.smith@example.com', 4, 25, 'female'),
('Alice Green', 'alice.green@example.com', 3, 27, 'female'),
('Bob Brown', 'bob.brown@example.com', 2, 35, 'male'),
('Charlie Black', 'charlie.black@example.com', 4, 40, 'male'),
('David White', 'david.white@example.com', 5, 22, 'male'),
('Eva Gray', 'eva.gray@example.com', 4, 33, 'female'),
('Frank Blue', 'frank.blue@example.com', 2, 28, 'male'),
('Grace Red', 'grace.red@example.com', 5, 26, 'female'),
('Henry Gold', 'henry.gold@example.com', 3, 32, 'male');
