CREATE TABLE friends(
	id INTEGER,
  name TEXT,
  birthday DATE
);

INSERT INTO friends (id, name, birthday)
VALUES (1, 'Jane Doe', '1990-05-30');
INSERT INTO friends (id, name, birthday)
VALUES (2, 'Device', '1995-03-12');
INSERT INTO friends (id, name, birthday)
VALUES (3, 'Ropz', '2000-09-21');

UPDATE friends
SET name = 'Jane Smith'
WHERE id = 1;

ALTER TABLE friends
ADD COLUMN email TEXT;

UPDATE friends
SET email = 'jane@codecademy.com'
WHERE id = 1;
UPDATE friends
SET email = 'device@astralis.gg'
WHERE id = 2;
UPDATE friends
SET email = 'ropz@mouz.sport'
WHERE id = 3;

DELETE FROM friends
WHERE id = 1;

SELECT *
FROM friends;
