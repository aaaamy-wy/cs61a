.read su19data.sql

CREATE TABLE obedience AS
  SELECT seven, instructor from students;

CREATE TABLE smallest_int AS
  SELECT time, smallest from students where smallest > 2 order by smallest asc limit 20;

CREATE TABLE matchmaker AS
  SELECT a.pet, 
    a.song, 
    a.color, 
    b.color 
    from students as a, students as b 
    where a.pet = b.pet and a.song = b.song and a.time < b.time;

CREATE TABLE smallest_int_having AS
  SELECT time, smallest from students group by smallest having count(smallest) = 1 order by smallest asc;
