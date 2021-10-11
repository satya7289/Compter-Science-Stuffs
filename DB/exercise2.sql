-- # Exercise 3
-- use DM;

-- select * from sailor;
-- select * from boat;
-- select * from reserve;

-- #### 1. Find the colors of boats reserved by Dustin.
-- select distinct b.color from sailor as s join reserve as r on r.sid=s.sid join boat as b on b.bid=r.bid where s.sname="Dustin";
-- # other way
-- select distinct b.color from boat as b,reserve as r,sailor as s where s.sname="Dustin" and s.sid=r.sid and b.bid=r.bid;

-- #### 2. Find all IDs of sailors who have a rating of at least 8 or have reserved boat 103.
-- -- select distinct s.sid from sailor as s join reserve as r on r.sid=s.sid where s.rating>=8 or r.bid=103;  -- wrong query failes because all s.sid!=r.sid on joining
-- (select s.sid from sailor as s where s.rating>=8) union (select r.sid from reserve as r where r.bid=103);

-- #### 3. Find the names of sailors who have not reserved a red boat.
-- select s.sname from sailor as s where s.sid not in (select r.sid from reserve as r,boat as b,sailor as s where r.sid=s.sid and r.bid=b.bid and b.color like "red");

-- #### 4. Find the IDs of sailors with age over 20 who have not reserved a red boat.
-- select *,s.sid from sailor as s where s.age>20 and s.sid not in (select r.sid from reserve as r,boat as b,sailor as s where r.sid=s.sid and r.bid=b.bid and b.color like "red");

-- #### 5. Find the names of sailors who have reserved at least two boats.
-- select s.name from sailor as s, reserve as r where r.sid=s.sid group by r.sid having count(r.bid)>=2; 

-- #### 6. Find the names of sailors who have reserved all boats.
-- select s.sname from sailor as s, reserve as r where r.sid=s.sid group by r.sid having count(r.bid) = (select count(*) from boat); 

-- #### 7. Find the names of sailors who have reserved all boats called Interlake. --left
-- -- select s.sname from sailor as s, reserve as r where r.sid=s.sid group by r.sid ;

-- #### 8. Find the IDs of sailors whose rating is better than some sailor called Andy.
-- select s.sid from sailor as s where s.rating > any(select rating from sailor where sname="Andy");

-- #### 9. Find the IDs of sailors whose rating is better than every sailor called Andy.
-- select s.sid from sailor as s where s.rating > all(select rating from sailor where sname="Andy");

-- #### 10. Find the IDs of sailors with the highest rating.
-- select s.sid from sailor as s where s.rating >= all(select rating from sailor);

-- #### 11. Find the name and age of the oldest sailor
-- select s.sname,s.age from sailor as s where s.age >=all(select age from sailor);
