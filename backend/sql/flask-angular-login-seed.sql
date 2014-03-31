
insert into `menu`(id, name, groupid) values(1, 'Home', 1);
insert into `menu`(id, name, groupid) values(2, 'Getting Start', 1);
insert into `menu`(id, name, groupid) values(3, 'CSS', 1);
insert into `menu`(id, name, groupid) values(4, 'Component', 1);
insert into menuuser(userid, menuid) select user.id, menu.id from user, menu where not exists (select 'e' from menuuser a where a.menuid = menu.id and a.userid = user.id);