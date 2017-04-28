select l.manager,e.leader_id,
count(pa.p1) as pa_pra_a1,count(pa.p2) as pa_a1_1,count(pa.p3) as pa_a1_a2,count(pa.p4) as pa_a1_3,
count(pa.p5) as pa_a2_a,count(pa.p6) as pa_a2_b,
count(ak.p1) as ak_pra_a1,count(ak.p2) as ak_a1_1,count(ak.p3) as ak_a1_a2,count(ak.p4) as ak_a1_3,
count(ak.p5) as ak_a2_a,count(ak.p6) as ak_a2_b,
count(bk.bk1) as bk1,count(bk.bk2) as bk2,count(bk.bk3) as bk3
from personalia_employee e
left join (
  select 
  leader_id,decode(grade,1,'1') as p1,decode(grade,2,'2') as p2,decode(grade,3,'3') as p3,
  decode(grade,4,'4') as p4,decode(grade,5,'5') as p5,decode(grade,6,'6') as p6
  from personalia_employee
  where status_active = 'pa'
) pa on pa.leader_id = e.leader_id and e.status_active = 'pa'
left join (
  select 
  leader_id,decode(grade,1,'1') as p1,decode(grade,2,'2') as p2,decode(grade,3,'3') as p3,
  decode(grade,4,'4') as p4,decode(grade,5,'5') as p5,decode(grade,6,'6') as p6
  from personalia_employee
  where status_active = 'ak'
) ak on ak.leader_id = e.leader_id and e.status_active = 'ak'
left join (
select 
  leader_id,decode(status_active,'bk1','bk1') as bk1,decode(status_active,'bk2','bk2') as bk2,
  decode(status_active,'bk3','bk3') as bk3
  from personalia_employee
  where status_active in ('bk1','bk2','bk3')
) bk on bk.leader_id = e.leader_id and status_active in ('bk1','bk2','bk3')
inner join personalia_leader l on l.leader_id = e.leader_id
group by l.manager,e.leader_id
;
