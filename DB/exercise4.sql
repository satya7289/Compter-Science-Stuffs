-- ## Exerices 3

-- use DM;

-- select * from sailor;
-- select * from boat;
-- select * from reserve;

-- ### 1. Find the name of sailors start with same character.
-- select s1.sname from sailor as s1,sailor as s2 where left(s1.sname,1)=left(s2.sname,1) and s1.sname <> s2.sname;

-- ### 2. Find the Boat's name whose Id is completely divided by any sailors age.
-- select b.bname from boat as b,sailor as s,reserve as r where b.bid=r.bid and s.sid=r.sid and (b.bid mod s.age) =0;

-- ### 3. Find the number of booking of red boat's in sep and oct month
-- select * from reserve as r where r.day like "%-9-%" or r.day like "%-10-%";

-- ### 4. Find the name of sailor's who booked more than one and less than four number of boats.
-- select s.sname from sailor as s,reserve as r where r.sid=s.sid group by r.sid having count(r.bid)>1 and count(r.bid)<4;
