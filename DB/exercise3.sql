-- ### Exerxise 3
-- use DM;

-- select * from sailor;
-- select * from boat;
-- select * from reserve;

-- ### 1. Find all Boat ID’s which is reserved by Sailors who have rating more than the average rating in reserves table.
-- select distinct r.bid from reserve as r, sailor as s where r.sid=s.sid and s.rating >(select avg(rating) from sailor);

-- ### 2. Find the color’s of boats which is reserved by Sailors who have rating more than the average rating in reserves table.
-- select distinct b.color from boat as b,reserve as r,sailor as s where b.bid=r.bid and s.sid=r.sid and s.rating > (select avg(rating) from sailor);

-- ### 3. Retrieve the color of boat reserved by the Sailor having 2nd highest ranking.
-- select distinct b.color from boat as b,reserve as r,sailor as s where b.bid=r.bid and s.sid=r.sid and s.rating = (select distinct rating from sailor order by rating desc limit 1 offset 1);

-- ### 4. How many reservations are done in the month of Nov by Lubber.
-- select count(*) from reserve as r where r.day like "%-11-%";

-- ### 5. Sailors will be supervised by someone who has a higher rating and is older. Retrieve all possible pairs of sailor and supervisor.
-- select *,s1.sname,s2.sname from sailor as s1,sailor s2 where s1.rating<s2.rating and s1.age<s2.age;

-- ### 6. Find the age of all the sailors having the lowest rating who have reserved for at least one boat.
-- select s.age from sailor as s,reserve as r where s.sid=r.sid  group by r.sid having count(r.bid)>=1 order by s.rating asc limit 1;

-- ### 7. Find the rating of the youngest sailor who has reserved the red color boat.
-- select s.rating from sailor as s,reserve as r,boat as b where b.bid=r.bid and s.sid=r.sid and b.color="red" order by s.age asc limit 1;
