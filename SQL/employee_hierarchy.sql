create table employee (id string, manager_id string);
insert into employee 
values (10001, 10002), (10002, 10005), (10003, 10002), (10004, 10007), (10005, 10007), (10006, 10007), (10007, 10001), (10008, 10005), (10009, 10007);

  --  id   | manager_id
  ---------+------------
  -- 10001 | 10002
  -- 10002 | 10005
  -- 10003 | 10002
  -- 10004 | 10007
  -- 10005 | 10007
  -- 10006 | 10007
  -- 10007 | 10001
  -- 10008 | 10005
  -- 10009 | 10007

-- Find all employees reporting directly or indirectly to employee 10002
-- Solution: Use recursive CTE
with recursive emp_h as (
    select id, manager_id from employee where manager_id = '10002' 
    union 
    select e.id, e.manager_id from employee e join emp_h on e.manager_id = emp_h.id
) select * from emp_h;

  -- |  id   | manager_id
  -- |-------+------------
  -- | 10001 | 10002
  -- | 10003 | 10002
  -- | 10007 | 10001
  -- | 10004 | 10007
  -- | 10005 | 10007
  -- | 10006 | 10007
  -- | 10009 | 10007
  -- | 10002 | 10005
  -- | 10008 | 10005
