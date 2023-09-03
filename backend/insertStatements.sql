-- These statements are used as dummy data into the database to extensively test and develop.

-- User --
INSERT INTO [User](Username, [Password], Email, Active, Phone)
VALUES('testUser','123456','testuser@gmail.com',0,'9163688200')

-- Reviews --
INSERT INTO Reviews(Username, ReviewDate, MovieId, Score)
VALUES ('testUser', '8/31/2023', 1, 5.0)

INSERT INTO Reviews(Username, ReviewDate, MovieId, Score)
VALUES ('testUser2', '8/31/2023', 1, 4.0)

-- Movies --
INSERT INTO Movies(MovieId, MovieName, MovieYear)
VALUES(MovieID,'MovieName',MovieYear)

-- MovieGenre --
INSERT INTO MovieGenre(MovieId,Genre)
VALUES('MovieID','MovieGenre')

-- Friends --
INSERT INTO Friends(User1Username,User2Username,FriendshipStarted)
VALUES('User1Username','User2Username', MovieYear)

-- Favorites -- 
INSERT INTO Favorites(Username, MovieId)
VALUES('Username', 'MovieId')