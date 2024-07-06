    Drop table if exists exercise;

    Create Table if not exists exercise(
        ID int not null primary key,
        exercise var(255) not null);

    insert into exercise
    values(1, 'Bicep Curl'),(2, 'Jackknife Situps'),(3, 'Swimming'),
          (4, 'Jogging'),(5, 'Hiking'), (6, 'Table Tennis')