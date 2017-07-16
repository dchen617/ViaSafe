#insert into countries (countryname) values('United States');
#select * from countries;
#insert into states (statename, countryid) values ('Maine', (SELECT countryid FROM countries where countryname='United States'));
#select * from states
insert into locations