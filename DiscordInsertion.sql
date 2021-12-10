\c discord;

insert into D_USER values('U613700','DaenerysT123','DaenerysT42@gmail.com','/Avatar/DaenerysT.jpg','F','*^%*(%$(*^&','DaenerysT_GOT');
insert into D_USER values('U613701','TheonGreyJoy123','TheonGreyJoy42@gmail.com','/Avatar/TheonGreyJoy.jpg','M','*%83&%(%^(&^','TheonGreyJoy_GOT');
insert into D_USER values('U613702','TyrionLan123','TyrionLan42@gmail.com','/Avatar/TyrionLan.jpg','M','#$%^45&*&^%','TyrionLan_GOT');
insert into D_USER values('U613703','CerseiLan123','CerseiLan42@gmail.com','/Avatar/CerseiLan.jpg','F','@9876$&^#*)$@','CerseiLan_GOT');
insert into D_USER values('U613704','AryaStark123','AryaStark42@gmail.com','/Avatar/AryaStark.jpg','F','$%^&*4567$%','AryaStark_GOT');
insert into D_USER values('U613705','SansaStark123','SansaStark42@gmail.com','/Avatar/SansaStark.jpg','F','$%^*(657(^&$^','SansaStark_GOT');
insert into D_USER values('U613706','JaimeLan123','JaimeLan42@gmail.com','/Avatar/JaimeLan.jpg','M','#$7654635#$^*','JaimeLan_GOT');
insert into D_USER values('U613707','BranStark123','BranStark42@gmail.com','/Avatar/BranStark.jpg','M',')*&%450996^%$','BranStark_GOT');
insert into D_USER values('U613708','JoffreyBarath123','JoffreyBarath42@gmail.com','/Avatar/JoffreyBarath.jpg','M','867%^&)(&987','JoffreyBarath_GOT');

insert into GUILD values('G100201', '*/icons/Targaryen.jpeg', 'Targaryen', 'U613700');
insert into GUILD values('G100202', '*/icons/Tyrell.jpeg', 'Tyrell', 'U613705');
insert into GUILD values('G100203', '*/icons/Baratheon.jpeg', 'Baratheon', 'U613708');
insert into GUILD values('G100204', '*/icons/Martell.jpeg', 'Martell', 'U613702');
insert into GUILD values('G100205', '*/icons/Stark.jpeg', 'Stark', 'U613705');
insert into GUILD values('G100206', '*/icons/Lannister.jpeg', 'Lannister', 'U613703');
insert into GUILD values('G100207', '*/icons/Tully.jpeg', 'Tully', 'U613704');
insert into GUILD values('G100208', '*/icons/Greyjoy.jpeg', 'Greyjoy', 'U613701');
insert into GUILD values('G100209', '*/icons/Arryn.jpeg', 'Arryn', 'U613704');

insert into CHANNEL values('CH210500','Westeros','Westeros is a channel',0,'Location',0,'G100201');
insert into CHANNEL values('CH210501','Dorne','Dorne is a channel',1,'Location',0,'G100204');
insert into CHANNEL values('CH210502','TheEyrie','TheEyrie is a channel',1,'Location',0,'G100209');
insert into CHANNEL values('CH210503','Riverrun','Riverrun is a channel',1,'Location',0,'G100207');
insert into CHANNEL values('CH210504','CasterlyRock','CasterlyRock is a channel',1,'Location',0,'G100206');
insert into CHANNEL values('CH210505','IronIslands','IronIslands is a channel',1,'Location',0,'G100208');
insert into CHANNEL values('CH210506','KingsLanding','KingsLanding is a channel',1,'Location',0,'G100206');
insert into CHANNEL values('CH210507','HighGarden','HighGarden is a channel',1,'Location',0,'G100202');
insert into CHANNEL values('CH210508','Winterfell','Winterfell is a channel',1,'Location',0,'G100205');

insert into THREAD values('TH310700','Baelor','CH210500');
insert into THREAD values('TH310701','Stormborn','CH210501');
insert into THREAD values('TH310702','TheDanceofDrgs','CH210502');
insert into THREAD values('TH310703','TheBattleofB','CH210504');
insert into THREAD values('TH310704','BeyondTWall','CH210507');
insert into THREAD values('TH310705','TheLongNight','CH210508');

insert into MESSAGE values('ME2310800','',1, '2019-10-11 10:10:25-07','Lorem ipsum dolor sit amet','');
insert into MESSAGE values('ME2310801','',0, '2019-10-11 10:11:22-01','consectetur adipiscing elit','/Image/Wargs.jpg');
insert into MESSAGE values('ME2310802','',0, '2019-10-11 10:13:21-10','Ut malesuada egestas est','');
insert into MESSAGE values('ME2310803','ME2310802',0, '2019-10-11 10:15:26-07','Suspendisse elementum','');
insert into MESSAGE values('ME2310804','',1, '2019-10-11 10:20:12-02','sed suscipit arcu volutpat','/Image/Wights.jpg');
insert into MESSAGE values('ME2310805','',0, '2019-10-11 10:21:25-07','Fusce luctus augue','');
insert into MESSAGE values('ME2310806','ME2310805',0, '2019-10-11 10:22:12-07','quis sodales arcu','');
insert into MESSAGE values('ME2310807','',1, '2019-10-11 10:22:55-07','amet tellus vitae','');
insert into MESSAGE values('ME2310808','',0,'2019-10-11 10:23:25-07','eget nibh sodales','/Image/Direwolves.jpg');

insert into EMOJI values('EM710900','U613700','/Image/Giants.jpg',0,'Giants');
insert into EMOJI values('EM710901','U613700','/Image/Dragons.jpg',0,'Dragons');
insert into EMOJI values('EM710902','U613708','/Image/Whitewalkers.jpg',0,'Whitewalkers');
insert into EMOJI values('EM710903','U613707','/Image/GreenSeers.jpg',0,'GreenSeers');
insert into EMOJI values('EM710904','U613708','/Image/Wights.jpg',0,'Wights');
insert into EMOJI values('EM710905','U613700','/Image/ChildrenOfTheForest.jpg',0,'ChildrenOfTheForest');
insert into EMOJI values('EM710906','U613705','/Image/Direwolves.jpg',0,'Direwolves');
insert into EMOJI values('EM710907','U613707','/Image/Wargs.jpg',0,'Wargs');
insert into EMOJI values('EM710908','U613705','/Image/Witches.jpg',0,'Witches');

insert into ROLE values('Clergyman','G100201',0,0,0,0);
insert into ROLE values('Banker','G100206',0,0,0,1);
insert into ROLE values('Outlaw','G100208',0,0,0,0);
insert into ROLE values('Page','G100201',0,0,0,0);
insert into ROLE values('Guard','G100206',0,0,0,0);
insert into ROLE values('Historian','G100204',0,0,0,0);
insert into ROLE values('FacelessMan','G100205',0,0,0,1);
insert into ROLE values('Seer','G100205',0,0,0,1);
insert into ROLE values('Owner','G100201',1,1,1,1);
insert into ROLE values('Owner','G100202',1,1,1,1);
insert into ROLE values('Owner','G100203',1,1,1,1);
insert into ROLE values('Owner','G100204',1,1,1,1);
insert into ROLE values('Owner','G100205',1,1,1,1);
insert into ROLE values('Owner','G100206',1,1,1,1);
insert into ROLE values('Owner','G100207',1,1,1,1);
insert into ROLE values('Owner','G100208',1,1,1,1);
insert into ROLE values('Owner','G100209',1,1,1,1);

insert into AUDIT_LOG values('E_ID3610700','2019-10-11 10:50:25-07','U613700',5,'Event:0','G100203');
insert into AUDIT_LOG values('E_ID3610701','2019-10-11 10:50:26-04','U613701',5,'Event:1','G100205');
insert into AUDIT_LOG values('E_ID3610702','2019-10-11 10:50:27-01','U613702',5,'Event:2','G100204');
insert into AUDIT_LOG values('E_ID3610703','2019-10-11 10:50:28-06','U613703',5,'Event:3','G100202');
insert into AUDIT_LOG values('E_ID3610704','2019-10-11 10:50:29-08','U613704',5,'Event:4','G100203');
insert into AUDIT_LOG values('E_ID3610705','2019-10-11 10:50:30-02','U613705',5,'Event:5','G100202');
insert into AUDIT_LOG values('E_ID3610706','2019-10-11 10:50:31-09','U613706',5,'Event:6','G100205');
insert into AUDIT_LOG values('E_ID3610707','2019-10-11 10:50:32-01','U613707',5,'Event:7','G100203');
insert into AUDIT_LOG values('E_ID3610708','2019-10-11 10:50:33-07','U613708',5,'Event:8','G100201');

insert into MESSAGE_SENT_IN_CHANNEL values('ME2310800', 'CH210500', 'U613700' );
insert into MESSAGE_SENT_IN_CHANNEL values('ME2310802', 'CH210502', 'U613704' );
insert into MESSAGE_SENT_IN_CHANNEL values('ME2310803', 'CH210502', 'U613704' );
insert into MESSAGE_SENT_IN_CHANNEL values('ME2310804', 'CH210503',  'U613704');
insert into MESSAGE_SENT_IN_CHANNEL values('ME2310805', 'CH210504',  'U613706');
insert into MESSAGE_SENT_IN_CHANNEL values('ME2310806', 'CH210504',  'U613702');


insert into MESSAGE_SENT_IN_THREAD values('ME2310801', 'TH310700', 'U613700' );
insert into MESSAGE_SENT_IN_THREAD values('ME2310807', 'TH310701',  'U613702');
insert into MESSAGE_SENT_IN_THREAD values('ME2310808', 'TH310703',  'U613703');


insert into USER_HAS_ROLE_IN_GUILD values('U613700','Owner','G100201');
insert into USER_HAS_ROLE_IN_GUILD values('U613701','Owner','G100208');
insert into USER_HAS_ROLE_IN_GUILD values('U613702','Banker','G100206');
insert into USER_HAS_ROLE_IN_GUILD values('U613703','Owner','G100206');
insert into USER_HAS_ROLE_IN_GUILD values('U613704','FacelessMan','G100205');
insert into USER_HAS_ROLE_IN_GUILD values('U613705','Owner','G100205');
insert into USER_HAS_ROLE_IN_GUILD values('U613706','Banker','G100206');
insert into USER_HAS_ROLE_IN_GUILD values('U613707','Seer','G100205');
insert into USER_HAS_ROLE_IN_GUILD values('U613708','Owner','G100203');
insert into USER_HAS_ROLE_IN_GUILD values('U613705','Owner','G100202');
insert into USER_HAS_ROLE_IN_GUILD values('U613702','Owner','G100204');
insert into USER_HAS_ROLE_IN_GUILD values('U613704','Owner','G100207');
insert into USER_HAS_ROLE_IN_GUILD values('U613704','Owner','G100209');


insert into ROLE_GIVEN_ACCESS_TO_CHANNEL values('Owner', 'G100204', 'CH210501');
insert into ROLE_GIVEN_ACCESS_TO_CHANNEL values('Owner', 'G100209', 'CH210502');
insert into ROLE_GIVEN_ACCESS_TO_CHANNEL values('Owner', 'G100207', 'CH210503');
insert into ROLE_GIVEN_ACCESS_TO_CHANNEL values('Owner', 'G100206', 'CH210504');
insert into ROLE_GIVEN_ACCESS_TO_CHANNEL values('Owner', 'G100208', 'CH210505');
insert into ROLE_GIVEN_ACCESS_TO_CHANNEL values('Owner', 'G100206', 'CH210506');
insert into ROLE_GIVEN_ACCESS_TO_CHANNEL values('Owner', 'G100202', 'CH210507');
insert into ROLE_GIVEN_ACCESS_TO_CHANNEL values('Owner', 'G100205', 'CH210508');
insert into ROLE_GIVEN_ACCESS_TO_CHANNEL values('Banker', 'G100206', 'CH210504');
insert into ROLE_GIVEN_ACCESS_TO_CHANNEL values('FacelessMan', 'G100205', 'CH210508');
insert into ROLE_GIVEN_ACCESS_TO_CHANNEL values('Seer', 'G100205', 'CH210508');

insert into MESSAGE_HAS_EMOJI values('ME2310801','EM710907');
insert into MESSAGE_HAS_EMOJI values('ME2310804','EM710904');
insert into MESSAGE_HAS_EMOJI values('ME2310808','EM710906');


